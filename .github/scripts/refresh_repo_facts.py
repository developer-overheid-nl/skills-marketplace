#!/usr/bin/env python3
"""Refresh per-plugin facts in marketplace.json from the upstream repositories.

Three things in the marketplace entry are facts about the upstream repo rather
than editorial choices, and each of them has gone stale before:

- `skills`: the number of skills the plugin ships
- `maintainer`: the owner of the source repo, with its display name
- `source.repo`: the canonical owner/name, which changes when a repo is
  transferred or renamed. GitHub keeps redirecting the old path, so a stale
  entry keeps working and nothing surfaces the move.

generate_readme_table.py renders the README table from these fields, so a
refresh is what keeps the table honest. Writing them into marketplace.json
rather than fetching at render time keeps the validate workflow offline.

Usage:
    python refresh_repo_facts.py          # write the facts into marketplace.json
    python refresh_repo_facts.py --check  # report drift, write nothing
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SOURCE_PATH = ROOT_DIR / "marketplace.json"

SUBPROCESS_TIMEOUT = 60


def gh_api(endpoint: str, jq: str) -> str | None:
    """Run a gh api call and return its trimmed stdout, or None on failure."""
    try:
        result = subprocess.run(
            ["gh", "api", endpoint, "--jq", jq],
            capture_output=True,
            text=True,
            timeout=SUBPROCESS_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        print(f"WAARSCHUWING: timeout bij {endpoint}")
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def fetch_repo_facts(repo: str) -> dict | None:
    """Fetch canonical name, owner and skill count for a repo.

    The canonical name comes back from the API even when `repo` is an old path
    that GitHub still redirects, which is how a transfer gets detected.
    """
    info = gh_api(f"repos/{repo}", "[.full_name, .owner.login] | @tsv")
    if not info:
        return None
    parts = info.split("\t")
    if len(parts) != 2:
        return None
    full_name, owner_login = parts

    owner_name = gh_api(f"users/{owner_login}", ".name") or ""
    if owner_name == "null":
        owner_name = ""

    count = gh_api(
        f"repos/{full_name}/contents/skills",
        '[.[] | select(.type == "dir")] | length',
    )

    facts = {
        "full_name": full_name,
        "maintainer": {"login": owner_login, "name": owner_name or owner_login},
    }
    if count and count.isdigit():
        facts["skills"] = int(count)
    return facts


def apply_facts(plugin: dict, facts: dict) -> list[str]:
    """Apply fetched facts to a plugin entry. Returns a list of change strings."""
    changes = []
    source = plugin.get("source", {})

    if source.get("source") == "github":
        old_repo = source.get("repo", "")
        if old_repo and old_repo != facts["full_name"]:
            changes.append(f"source.repo: {old_repo} -> {facts['full_name']}")
            source["repo"] = facts["full_name"]

    if plugin.get("maintainer") != facts["maintainer"]:
        old = plugin.get("maintainer", {}).get("name", "(geen)")
        changes.append(f"maintainer: {old} -> {facts['maintainer']['name']}")
        plugin["maintainer"] = facts["maintainer"]

    if "skills" in facts and plugin.get("skills") != facts["skills"]:
        changes.append(f"skills: {plugin.get('skills', '(geen)')} -> {facts['skills']}")
        plugin["skills"] = facts["skills"]

    return changes


def main() -> None:
    if not SOURCE_PATH.exists():
        print(f"FOUT: {SOURCE_PATH} niet gevonden")
        sys.exit(1)

    with open(SOURCE_PATH) as f:
        data = json.load(f)

    plugins = data.get("plugins", [])
    all_changes = []
    failures = 0

    for plugin in plugins:
        source = plugin.get("source", {})
        repo = source.get("repo")
        if source.get("source") != "github" or not repo:
            continue

        facts = fetch_repo_facts(repo)
        if facts is None:
            print(f"WAARSCHUWING: kon {repo} niet ophalen")
            failures += 1
            continue

        for change in apply_facts(plugin, facts):
            all_changes.append(f"{plugin['name']}: {change}")

    if failures and failures == len(plugins):
        print(f"FOUT: alle {failures} fetches zijn mislukt")
        sys.exit(1)

    if not all_changes:
        print("Alle repo-gegevens in marketplace.json zijn actueel")
        sys.exit(0)

    for change in all_changes:
        print(change)

    if "--check" in sys.argv:
        print("\nmarketplace.json is niet actueel. Draai: python refresh_repo_facts.py")
        sys.exit(1)

    with open(SOURCE_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\nmarketplace.json bijgewerkt: {len(all_changes)} wijzigingen")


if __name__ == "__main__":
    main()
