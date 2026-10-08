#!/usr/bin/env python3
"""Generate platform-specific marketplace files from the neutral root format.

The root marketplace.json is the single source of truth. This script generates
platform-specific variants for Claude Code, Cursor and Codex (and future
platforms).

Usage:
    python generate_marketplace.py          # generate all platform files
    python generate_marketplace.py --check  # verify files are in sync
"""

import copy
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SOURCE_PATH = ROOT_DIR / "marketplace.json"
CLAUDE_PATH = ROOT_DIR / ".claude-plugin" / "marketplace.json"
CURSOR_PATH = ROOT_DIR / ".cursor-plugin" / "marketplace.json"
CODEX_PATH = ROOT_DIR / ".agents" / "plugins" / "marketplace.json"

CLAUDE_SCHEMA = "https://anthropic.com/claude-code/marketplace.schema.json"


def load_source() -> dict:
    """Load the neutral marketplace.json from the project root."""
    with open(SOURCE_PATH) as f:
        return json.load(f)


# Fields the README table is rendered from. They describe the upstream repo
# rather than the plugin entry itself, and are not part of any platform schema,
# so they stay in the neutral marketplace.json. `skills` especially: Claude Code
# reads that key as a list of skill paths, not as a count.
README_ONLY_FIELDS = ("skills", "maintainer")


def _strip_readme_fields(plugin: dict) -> dict:
    """Return a copy of a plugin entry without the README-only fields."""
    return {k: v for k, v in plugin.items() if k not in README_ONLY_FIELDS}


def generate_claude(data: dict) -> dict:
    """Generate Claude Code marketplace.json.

    Adds $schema and copies all fields unchanged, apart from the README-only
    fields which have no meaning in the Claude Code schema.
    """
    result = {"$schema": CLAUDE_SCHEMA}
    result.update(copy.deepcopy(data))
    result["plugins"] = [_strip_readme_fields(p) for p in result.get("plugins", [])]
    return result


def _display_name(name: str) -> str:
    """Convert a kebab-case plugin name to a human-readable display name.

    Examples:
        "standaarden" -> "Standaarden"
        "zad-actions" -> "Zad Actions"
        "bio-security-baseline" -> "Bio Security Baseline"
    """
    return name.replace("-", " ").title()


def _transform_plugin_for_cursor(plugin: dict) -> dict:
    """Transform a single plugin entry to Cursor format."""
    cursor_plugin: dict = {
        "name": plugin["name"],
        "displayName": _display_name(plugin["name"]),
    }

    if "description" in plugin:
        cursor_plugin["description"] = plugin["description"]
    if "version" in plugin:
        cursor_plugin["version"] = plugin["version"]
    if "author" in plugin:
        cursor_plugin["author"] = copy.deepcopy(plugin["author"])

    # Source mapping
    source = plugin.get("source", {})
    if isinstance(source, dict):
        cursor_plugin["source"] = copy.deepcopy(source)
        if source.get("source") == "github":
            repo = source.get("repo", "")
            cursor_plugin["repository"] = f"https://github.com/{repo}"

    # Keywords: merge category + tags
    keywords = []
    if "category" in plugin:
        keywords.append(plugin["category"])
    keywords.extend(plugin.get("tags", []))
    if keywords:
        cursor_plugin["keywords"] = keywords

    return cursor_plugin


def generate_cursor(data: dict) -> dict:
    """Generate Cursor marketplace.json.

    Transforms plugin fields to Cursor's expected format.
    """
    result: dict = {
        "name": data.get("name", ""),
        "metadata": {
            "description": data.get("metadata", {}).get("description", ""),
            "pluginRoot": ".cursor-plugin",
        },
        "owner": copy.deepcopy(data.get("owner", {})),
        "plugins": [_transform_plugin_for_cursor(p) for p in data.get("plugins", [])],
    }
    return result


def _codex_source(source: dict) -> dict:
    """Transform a plugin source to a type Codex understands.

    Codex has no "github" source type and silently skips any entry using one,
    so a GitHub repo becomes a plain clone URL. Other source types pass through
    unchanged.
    """
    if not isinstance(source, dict) or source.get("source") != "github":
        return copy.deepcopy(source)

    codex_source = {
        "source": "url",
        "url": f"https://github.com/{source.get('repo', '')}.git",
    }
    for key in ("ref", "sha"):
        if key in source:
            codex_source[key] = source[key]
    return codex_source


def _transform_plugin_for_codex(plugin: dict) -> dict:
    """Transform a single plugin entry to Codex format."""
    codex_plugin: dict = {"name": plugin["name"]}

    if "description" in plugin:
        codex_plugin["description"] = plugin["description"]

    codex_plugin["source"] = _codex_source(plugin.get("source", {}))
    codex_plugin["policy"] = {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    }
    codex_plugin["category"] = plugin.get("category", "productivity").capitalize()

    return codex_plugin


def generate_codex(data: dict) -> dict:
    """Generate the Codex marketplace.json.

    Codex reads .agents/plugins/marketplace.json before the Claude Code file,
    and needs url sources plus a policy and category per plugin.
    """
    name = data.get("name", "")
    return {
        "name": name,
        "interface": {"displayName": _display_name(name)},
        "plugins": [_transform_plugin_for_codex(p) for p in data.get("plugins", [])],
    }


# Registry of platform generators — add new platforms here
PLATFORMS: dict[str, tuple[Path, callable]] = {
    "claude": (CLAUDE_PATH, generate_claude),
    "cursor": (CURSOR_PATH, generate_cursor),
    "codex": (CODEX_PATH, generate_codex),
}


def write_json(path: Path, data: dict) -> None:
    """Write JSON data to a file with consistent formatting."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def generate_all(source_data: dict) -> dict[str, dict]:
    """Generate all platform marketplace files. Returns dict of platform -> data."""
    results = {}
    for name, (path, generator) in PLATFORMS.items():
        generated = generator(source_data)
        write_json(path, generated)
        results[name] = generated
        print(f"Gegenereerd: {path.relative_to(ROOT_DIR)}")
    return results


def check_sync(source_data: dict) -> bool:
    """Check if platform files are in sync with the source. Returns True if synced."""
    all_synced = True

    for _name, (path, generator) in PLATFORMS.items():
        expected = generator(source_data)

        if not path.exists():
            print(f"FOUT: {path.relative_to(ROOT_DIR)} bestaat niet")
            all_synced = False
            continue

        with open(path) as f:
            actual = json.load(f)

        if actual != expected:
            print(
                f"FOUT: {path.relative_to(ROOT_DIR)} is niet in sync met marketplace.json"
            )
            all_synced = False
        else:
            print(f"OK: {path.relative_to(ROOT_DIR)} is in sync")

    return all_synced


def main() -> None:
    if not SOURCE_PATH.exists():
        print(f"FOUT: {SOURCE_PATH} niet gevonden")
        sys.exit(1)

    source_data = load_source()

    if "--check" in sys.argv:
        if check_sync(source_data):
            print("\nAlle platform-bestanden zijn in sync")
            sys.exit(0)
        else:
            print(
                "\nPlatform-bestanden zijn NIET in sync. Draai: python generate_marketplace.py"
            )
            sys.exit(1)
    else:
        generate_all(source_data)
        print("\nAlle platform-bestanden gegenereerd")


if __name__ == "__main__":
    main()
