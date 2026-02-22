#!/usr/bin/env python3
"""Check upstream plugin versions and create a PR if drift is detected.

Compares plugin versions and descriptions in marketplace.json against their
upstream plugin.json files on GitHub. Creates a PR when drift is detected.

Version normalization: leading 'v' prefixes and trailing '.0' segments are
ignored during comparison (e.g. "v1.2.0" == "1.2"), so cosmetic differences
don't trigger false-positive updates.
"""

import base64
import binascii
import hashlib
import json
import os
import re
import subprocess
import sys

MARKETPLACE_PATH = ".claude-plugin/marketplace.json"

SUBPROCESS_TIMEOUT = 60

# Matches 'org/repo' with valid GitHub characters
REPO_PATTERN = re.compile(r"^[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+$")


def normalize_version(version: str) -> str:
    """Normalize a version string for comparison.

    Strips leading 'v', trailing '.0' segments for comparison purposes.
    Returns lowercased, stripped version.

    Examples:
        "v1.2.0" -> "1.2"
        "1.0.0"  -> "1"
        "1.2.3"  -> "1.2.3"
    """
    v = version.strip().lower()
    if v.startswith("v"):
        v = v[1:]
    # Normalize trailing .0 segments: 1.2 == 1.2.0
    parts = v.split(".")
    while len(parts) > 1 and parts[-1] == "0":
        parts.pop()
    return ".".join(parts)


def versions_equal(a: str, b: str) -> bool:
    """Compare two version strings with normalization."""
    return normalize_version(a) == normalize_version(b)


def sanitize_branch(s: str) -> str:
    """Remove invalid git branch characters and prevent path traversal."""
    sanitized = re.sub(r"[^a-zA-Z0-9_-]", "-", s)
    # Collapse consecutive dashes and strip leading/trailing dashes
    sanitized = re.sub(r"-{2,}", "-", sanitized)
    sanitized = sanitized.strip("-")
    # Reject empty result
    return sanitized or "unknown"


def validate_repo(repo: str) -> bool:
    """Validate that a repo string is a safe 'org/name' format."""
    return bool(REPO_PATTERN.match(repo))


def resolve_repo(plugin: dict) -> str | None:
    """Extract the GitHub repo from a plugin's source config.

    Returns repo string like 'org/name' or None if not resolvable.
    Validates the result against a safe pattern to prevent injection.
    """
    source = plugin.get("source", {})
    if not isinstance(source, dict):
        return None

    repo = None
    source_type = source.get("source")
    if source_type == "github":
        repo = source.get("repo")
    elif source_type == "url":
        url = source.get("url", "")
        if "github.com/" in url:
            # Extract exactly org/name from the URL path
            path = url.split("github.com/", 1)[-1]
            # Remove .git suffix and any trailing path segments
            path = path.replace(".git", "")
            segments = [s for s in path.split("/") if s]
            if len(segments) >= 2:
                repo = f"{segments[0]}/{segments[1]}"

    if repo and validate_repo(repo):
        return repo
    return None


def fetch_upstream_plugin(repo: str) -> dict | None:
    """Fetch and parse the upstream plugin.json from a GitHub repo.

    Returns parsed dict or None on failure.
    """
    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{repo}/contents/.claude-plugin/plugin.json",
            "--jq",
            ".content",
        ],
        capture_output=True,
        text=True,
        timeout=SUBPROCESS_TIMEOUT,
    )
    if result.returncode != 0:
        return None

    try:
        content = base64.b64decode(result.stdout.strip()).decode("utf-8")
        return json.loads(content)
    except (json.JSONDecodeError, ValueError, binascii.Error):
        return None


def detect_updates(
    plugins: list[dict],
) -> tuple[list[dict], list[str], int]:
    """Compare local plugins against upstream and return updates, summary, and failure count.

    Returns:
        updates: list of update dicts for plugins that need updating
        summary_lines: human-readable status per plugin
        fetch_failures: count of plugins where upstream fetch failed
    """
    updates = []
    summary_lines = []
    fetch_failures = 0

    for plugin in plugins:
        name = plugin.get("name", "?")
        local_version = plugin.get("version", "")
        local_description = plugin.get("description", "")

        repo = resolve_repo(plugin)
        if repo is None:
            msg = f"SKIP: {name} - kan geen GitHub repo bepalen"
            print(msg)
            summary_lines.append(msg)
            continue

        upstream = fetch_upstream_plugin(repo)
        if upstream is None:
            fetch_failures += 1
            msg = f"WAARSCHUWING: {name} - kan plugin.json niet ophalen uit {repo}"
            print(msg)
            summary_lines.append(msg)
            continue

        upstream_version = upstream.get("version", "")
        upstream_description = upstream.get("description", "")

        version_changed = bool(
            upstream_version and not versions_equal(upstream_version, local_version)
        )
        description_changed = bool(
            upstream_description and upstream_description != local_description
        )

        if version_changed or description_changed:
            changes = []
            if version_changed:
                changes.append(f"versie {local_version} -> {upstream_version}")
            if description_changed:
                changes.append("description gewijzigd")
            msg = f"UPDATE: {name} ({', '.join(changes)})"
            print(msg)
            summary_lines.append(msg)
            updates.append(
                {
                    "name": name,
                    "repo": repo,
                    "old_version": local_version,
                    "new_version": upstream_version if version_changed else local_version,
                    "old_description": local_description,
                    "new_description": (
                        upstream_description
                        if description_changed
                        else local_description
                    ),
                    "version_changed": version_changed,
                    "description_changed": description_changed,
                }
            )
        else:
            msg = f"OK: {name} v{local_version}"
            print(msg)
            summary_lines.append(msg)

    return updates, summary_lines, fetch_failures


def write_job_summary(summary_lines: list[str], extra: str = "") -> None:
    """Write GitHub Actions job summary if running in CI."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY", "")
    if not summary_file:
        return

    with open(summary_file, "a") as f:
        f.write("## Plugin versie-check resultaten\n\n")
        for line in summary_lines:
            if line.startswith("OK:"):
                emoji = "\u2705"
            elif line.startswith("UPDATE:"):
                emoji = "\U0001f504"
            else:
                emoji = "\u26a0\ufe0f"
            f.write(f"- {emoji} {line}\n")
        f.write("\n")
        if extra:
            f.write(f"{extra}\n")


def check_existing_bump_pr() -> dict | None:
    """Check for an existing open bump PR with the automated-bump label.

    Returns the first matching PR dict or None.
    """
    result = subprocess.run(
        [
            "gh",
            "pr",
            "list",
            "--state",
            "open",
            "--label",
            "automated-bump",
            "--json",
            "number,title,headRefName",
        ],
        capture_output=True,
        text=True,
        timeout=SUBPROCESS_TIMEOUT,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None

    try:
        prs = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None

    # Any PR with the automated-bump label counts as an existing bump PR
    return prs[0] if prs else None


def apply_updates(data: dict, updates: list[dict]) -> None:
    """Apply version/description updates to the marketplace data in-place."""
    for update in updates:
        for plugin in data["plugins"]:
            if plugin["name"] == update["name"]:
                if update["version_changed"]:
                    plugin["version"] = update["new_version"]
                if update["description_changed"]:
                    plugin["description"] = update["new_description"]


def build_branch_and_title(updates: list[dict]) -> tuple[str, str]:
    """Generate branch name and PR title for the updates."""
    if len(updates) == 1:
        u = updates[0]
        safe_name = sanitize_branch(u["name"])
        changes = []
        if u["version_changed"]:
            changes.append(f"v{u['new_version']}")
        if u["description_changed"]:
            changes.append("description")
        safe_changes = sanitize_branch("-".join(changes))
        branch = f"automated/bump-{safe_name}-{safe_changes}"
        title = f"Update {u['name']} plugin: {', '.join(changes)}"
    else:
        names_hash = hashlib.sha256(
            "-".join(
                sorted(f"{u['name']}-{u['new_version']}" for u in updates)
            ).encode()
        ).hexdigest()[:8]
        branch = f"automated/bump-plugins-{names_hash}"
        title = f"Update {len(updates)} plugins"
    return branch, title


def build_pr_body(updates: list[dict]) -> str:
    """Build the PR body with update table and review checklist."""
    lines = ["## Automatische plugin-update\n"]
    lines.append("| Plugin | Veld | Oud | Nieuw | Repo |")
    lines.append("|--------|------|-----|-------|------|")

    for u in updates:
        repo_url = f"https://github.com/{u['repo']}"
        changelog_url = f"{repo_url}/releases"
        if u["version_changed"]:
            lines.append(
                f"| {u['name']} | versie | {u['old_version']} | "
                f"[{u['new_version']}]({changelog_url}) | "
                f"[{u['repo']}]({repo_url}) |"
            )
        if u["description_changed"]:
            old_desc = u["old_description"]
            new_desc = u["new_description"]
            if len(old_desc) > 60:
                old_desc = old_desc[:60] + "..."
            if len(new_desc) > 60:
                new_desc = new_desc[:60] + "..."
            lines.append(
                f"| {u['name']} | description | {old_desc} | "
                f"{new_desc} | "
                f"[{u['repo']}]({repo_url}) |"
            )

    lines.append("")
    lines.append("### Review checklist")
    lines.append("- [ ] Versie-nummers kloppen met upstream")
    lines.append("- [ ] Geen breaking changes in de nieuwe versies")
    lines.append("- [ ] Changelog upstream bekeken")
    lines.append("- [ ] Plugin-inhoud in marketplace komt overeen met upstream")
    lines.append("")
    lines.append(
        "> **Let op:** Deze PR werkt alleen versienummer en description in "
        "marketplace.json bij. Controleer of de overige plugin-inhoud "
        "(skills, commands, etc.) ook actueel is."
    )
    lines.append("")
    lines.append("---")
    lines.append(
        "*Deze PR is automatisch aangemaakt door de "
        "[check-versions workflow]"
        "(.github/workflows/check-versions.yml).*"
    )
    return "\n".join(lines)


def create_pr(
    marketplace_path: str,
    data: dict,
    updates: list[dict],
    branch: str,
    title: str,
    body: str,
) -> str:
    """Create branch, commit changes, push, and create PR. Returns PR URL."""
    # Write updated marketplace.json
    with open(marketplace_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Validate the JSON we just wrote is still valid
    with open(marketplace_path) as f:
        json.load(f)

    # Git configuration
    subprocess.run(
        ["git", "config", "user.name", "github-actions[bot]"],
        check=True,
        timeout=SUBPROCESS_TIMEOUT,
    )
    subprocess.run(
        [
            "git",
            "config",
            "user.email",
            "github-actions[bot]@users.noreply.github.com",
        ],
        check=True,
        timeout=SUBPROCESS_TIMEOUT,
    )

    # Create branch and commit
    subprocess.run(
        ["git", "checkout", "-b", branch],
        check=True,
        timeout=SUBPROCESS_TIMEOUT,
    )
    subprocess.run(
        ["git", "add", marketplace_path],
        check=True,
        timeout=SUBPROCESS_TIMEOUT,
    )

    if len(updates) == 1:
        commit_msg = title
    else:
        names = ", ".join(u["name"] for u in updates)
        commit_msg = f"Update plugins: {names}"

    subprocess.run(
        ["git", "commit", "-m", commit_msg],
        check=True,
        timeout=SUBPROCESS_TIMEOUT,
    )

    push_result = subprocess.run(
        ["git", "push", "-u", "origin", branch],
        capture_output=True,
        text=True,
        timeout=SUBPROCESS_TIMEOUT,
    )
    if push_result.returncode != 0:
        print(f"FOUT: git push mislukt: {push_result.stderr}")
        sys.exit(1)

    # Ensure label exists
    subprocess.run(
        [
            "gh",
            "label",
            "create",
            "automated-bump",
            "--description",
            "Automatische versie-bump PR",
            "--color",
            "0e8a16",
            "--force",
        ],
        capture_output=True,
        text=True,
        timeout=SUBPROCESS_TIMEOUT,
    )

    # Create PR
    result = subprocess.run(
        [
            "gh",
            "pr",
            "create",
            "--title",
            title,
            "--body",
            body,
            "--label",
            "automated-bump",
        ],
        capture_output=True,
        text=True,
        timeout=SUBPROCESS_TIMEOUT,
    )
    if result.returncode != 0:
        print(f"FOUT: PR aanmaken mislukt: {result.stderr}")
        sys.exit(1)

    return result.stdout.strip()


def main() -> None:
    with open(MARKETPLACE_PATH) as f:
        data = json.load(f)

    plugins = data.get("plugins", [])
    resolvable_count = sum(1 for p in plugins if resolve_repo(p) is not None)

    updates, summary_lines, fetch_failures = detect_updates(plugins)

    # If all resolvable plugins failed to fetch, something is wrong (auth, network)
    if resolvable_count > 0 and fetch_failures == resolvable_count:
        msg = (
            f"FOUT: Alle {fetch_failures} upstream fetches zijn mislukt. "
            "Mogelijk een netwerk- of authenticatieprobleem."
        )
        print(f"\n{msg}")
        write_job_summary(summary_lines, f"**{msg}**")
        sys.exit(1)

    if not updates:
        print("\nAlle plugin versies zijn actueel")
        write_job_summary(summary_lines, "**Geen updates nodig.**")
        sys.exit(0)

    # Check for existing open bump PR
    existing_pr = check_existing_bump_pr()
    if existing_pr:
        print(
            f"\nEr is al een open bump PR: #{existing_pr['number']} "
            f"({existing_pr['title']})"
        )
        print("Geen nieuwe PR aangemaakt")
        write_job_summary(
            summary_lines,
            f"**Bestaande open PR gevonden: #{existing_pr['number']}** "
            "- geen nieuwe PR aangemaakt.",
        )
        sys.exit(0)

    # Apply updates and create PR
    apply_updates(data, updates)
    branch, title = build_branch_and_title(updates)
    body = build_pr_body(updates)
    pr_url = create_pr(MARKETPLACE_PATH, data, updates, branch, title, body)

    print(f"\nPR aangemaakt: {pr_url}")
    write_job_summary(summary_lines, f"**PR aangemaakt:** {pr_url}")


if __name__ == "__main__":
    main()
