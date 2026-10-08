#!/usr/bin/env python3
"""Generate the plugin table in README.md from marketplace.json.

The table between the BEGIN/END markers in README.md is generated, not written
by hand. Every column comes from marketplace.json, so a plugin that moves to
another organisation or gains a skill cannot leave a stale row behind.

The skill count and the maintainer display name are not inherent to the
marketplace entry; they are facts about the upstream repository. refresh_repo_facts.py
fetches them from GitHub and writes them into marketplace.json, which keeps this
script (and therefore the validate workflow) free of network calls.

Usage:
    python generate_readme_table.py          # rewrite the table in README.md
    python generate_readme_table.py --check  # verify the table is up to date
"""

import json
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SOURCE_PATH = ROOT_DIR / "marketplace.json"
README_PATH = ROOT_DIR / "README.md"

BEGIN_MARKER = "<!-- BEGIN PLUGIN TABLE -->"
END_MARKER = "<!-- END PLUGIN TABLE -->"

HEADER = (
    "| Plugin | Skills | Beschrijving | Maintainer |\n"
    "|--------|--------|-------------|------------|\n"
)

# Descriptions in marketplace.json mirror the upstream plugin.json and are
# written for a plugin detail view, so they run long and sometimes carry a
# status prefix. The table needs one scannable sentence per row.
STATUS_PREFIX = re.compile(r"^(CONCEPT|BETA|ALPHA)\s*[—-]\s*", re.IGNORECASE)


def escape_cell(text: str) -> str:
    """Escape characters that would break out of a markdown table cell."""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def summarize(description: str) -> str:
    """Reduce a plugin description to its first sentence.

    Splits on a period that ends a sentence rather than one inside an
    abbreviation or a version number, so "publiccode.yml" and "v1.2.3" survive.
    """
    text = STATUS_PREFIX.sub("", description.strip())
    match = re.search(r"\.(?=\s+[A-Z(])", text)
    if match:
        text = text[: match.start()]
    return text.rstrip(".").strip()


def repo_url(plugin: dict) -> str:
    """Return the browsable URL for a plugin's source."""
    source = plugin.get("source", {})
    if source.get("source") == "github" and source.get("repo"):
        return f"https://github.com/{source['repo']}"
    return source.get("url", "")


def maintainer_cell(plugin: dict) -> str:
    """Render the maintainer column.

    The owner of the source repository is the maintainer. Its display name is
    stored as `maintainer.name` by refresh_repo_facts.py; the login is derived
    from the source so the link cannot drift from the repo it points at.
    """
    maintainer = plugin.get("maintainer", {})
    login = maintainer.get("login", "")
    if not login:
        source = plugin.get("source", {})
        login = source.get("repo", "/").split("/")[0]
    name = maintainer.get("name") or login
    return f"[{escape_cell(name)}](https://github.com/{login})"


def render_row(plugin: dict) -> str:
    """Render one table row for a plugin."""
    name = escape_cell(plugin["name"])
    url = repo_url(plugin)
    plugin_cell = f"[{name}]({url})" if url else name
    skills = plugin.get("skills")
    skills_cell = str(skills) if isinstance(skills, int) else "?"
    description = escape_cell(summarize(plugin.get("description", "")))
    return (
        f"| {plugin_cell} | {skills_cell} | {description} | {maintainer_cell(plugin)} |"
    )


def render_table(data: dict) -> str:
    """Render the full plugin table, including the surrounding markers."""
    rows = "\n".join(render_row(p) for p in data.get("plugins", []))
    return f"{BEGIN_MARKER}\n\n{HEADER}{rows}\n\n{END_MARKER}"


def replace_table(readme: str, table: str) -> str:
    """Replace the marked table section in the README text."""
    start = readme.find(BEGIN_MARKER)
    end = readme.find(END_MARKER)
    if start == -1 or end == -1:
        raise ValueError(
            f"Markers {BEGIN_MARKER} / {END_MARKER} niet gevonden in README.md"
        )
    if end < start:
        raise ValueError(f"{END_MARKER} staat voor {BEGIN_MARKER} in README.md")
    return readme[:start] + table + readme[end + len(END_MARKER) :]


def main() -> None:
    if not SOURCE_PATH.exists():
        print(f"FOUT: {SOURCE_PATH} niet gevonden")
        sys.exit(1)

    with open(SOURCE_PATH) as f:
        data = json.load(f)

    readme = README_PATH.read_text()

    try:
        updated = replace_table(readme, render_table(data))
    except ValueError as exc:
        print(f"FOUT: {exc}")
        sys.exit(1)

    if "--check" in sys.argv:
        if updated == readme:
            print("OK: de plugin-tabel in README.md is actueel")
            sys.exit(0)
        print(
            "FOUT: de plugin-tabel in README.md is niet actueel. "
            "Draai: python .github/scripts/generate_readme_table.py"
        )
        sys.exit(1)

    README_PATH.write_text(updated)
    print(f"Plugin-tabel bijgewerkt: {len(data.get('plugins', []))} plugins")


if __name__ == "__main__":
    main()
