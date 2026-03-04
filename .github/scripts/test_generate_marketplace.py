"""Tests for generate_marketplace.py."""

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from generate_marketplace import (
    CLAUDE_SCHEMA,
    _display_name,
    _transform_plugin_for_cursor,
    check_sync,
    generate_all,
    generate_claude,
    generate_cursor,
    load_source,
    write_json,
)

SAMPLE_DATA = {
    "name": "test-plugins",
    "metadata": {"description": "Test plugins"},
    "owner": {"name": "test-org"},
    "plugins": [
        {
            "name": "my-plugin",
            "description": "A test plugin",
            "version": "1.0.0",
            "author": {"name": "Test Author"},
            "source": {"source": "github", "repo": "org/my-plugin"},
            "category": "productivity",
            "tags": ["test", "demo"],
        }
    ],
}

SAMPLE_PLUGIN = SAMPLE_DATA["plugins"][0]


class TestDisplayName:
    def test_single_word(self):
        assert _display_name("standaarden") == "Standaarden"

    def test_hyphenated(self):
        assert _display_name("zad-actions") == "Zad Actions"

    def test_multi_hyphen(self):
        assert _display_name("bio-security-baseline") == "Bio Security Baseline"

    def test_already_capitalized(self):
        assert _display_name("MyPlugin") == "Myplugin"


class TestGenerateClaude:
    def test_adds_schema(self):
        result = generate_claude(SAMPLE_DATA)
        assert result["$schema"] == CLAUDE_SCHEMA

    def test_preserves_all_fields(self):
        result = generate_claude(SAMPLE_DATA)
        assert result["name"] == "test-plugins"
        assert result["owner"] == {"name": "test-org"}
        assert len(result["plugins"]) == 1
        assert result["plugins"][0]["name"] == "my-plugin"

    def test_schema_is_first_key(self):
        result = generate_claude(SAMPLE_DATA)
        keys = list(result.keys())
        assert keys[0] == "$schema"

    def test_deep_copy(self):
        result = generate_claude(SAMPLE_DATA)
        result["plugins"][0]["name"] = "modified"
        assert SAMPLE_DATA["plugins"][0]["name"] == "my-plugin"


class TestTransformPluginForCursor:
    def test_display_name(self):
        result = _transform_plugin_for_cursor(SAMPLE_PLUGIN)
        assert result["displayName"] == "My Plugin"

    def test_keywords_from_category_and_tags(self):
        result = _transform_plugin_for_cursor(SAMPLE_PLUGIN)
        assert result["keywords"] == ["productivity", "test", "demo"]

    def test_repository_url(self):
        result = _transform_plugin_for_cursor(SAMPLE_PLUGIN)
        assert result["repository"] == "https://github.com/org/my-plugin"

    def test_preserves_basic_fields(self):
        result = _transform_plugin_for_cursor(SAMPLE_PLUGIN)
        assert result["name"] == "my-plugin"
        assert result["description"] == "A test plugin"
        assert result["version"] == "1.0.0"
        assert result["author"] == {"name": "Test Author"}

    def test_no_category_no_tags(self):
        plugin = {"name": "bare", "source": {"source": "github", "repo": "o/r"}}
        result = _transform_plugin_for_cursor(plugin)
        assert "keywords" not in result

    def test_only_category(self):
        plugin = {
            "name": "cat-only",
            "category": "security",
            "source": {"source": "github", "repo": "o/r"},
        }
        result = _transform_plugin_for_cursor(plugin)
        assert result["keywords"] == ["security"]

    def test_only_tags(self):
        plugin = {
            "name": "tags-only",
            "tags": ["a", "b"],
            "source": {"source": "github", "repo": "o/r"},
        }
        result = _transform_plugin_for_cursor(plugin)
        assert result["keywords"] == ["a", "b"]

    def test_non_github_source(self):
        plugin = {
            "name": "other",
            "source": {"source": "url", "url": "https://example.com"},
        }
        result = _transform_plugin_for_cursor(plugin)
        assert "repository" not in result

    def test_deep_copy_author(self):
        result = _transform_plugin_for_cursor(SAMPLE_PLUGIN)
        result["author"]["name"] = "modified"
        assert SAMPLE_PLUGIN["author"]["name"] == "Test Author"


class TestGenerateCursor:
    def test_structure(self):
        result = generate_cursor(SAMPLE_DATA)
        assert result["name"] == "test-plugins"
        assert result["metadata"]["pluginRoot"] == ".cursor-plugin"
        assert result["owner"] == {"name": "test-org"}
        assert len(result["plugins"]) == 1

    def test_no_schema(self):
        result = generate_cursor(SAMPLE_DATA)
        assert "$schema" not in result

    def test_plugin_transformed(self):
        result = generate_cursor(SAMPLE_DATA)
        plugin = result["plugins"][0]
        assert "displayName" in plugin
        assert "keywords" in plugin


class TestWriteJson:
    def test_writes_valid_json(self, tmp_path):
        path = tmp_path / "sub" / "test.json"
        write_json(path, {"key": "value"})
        with open(path) as f:
            data = json.load(f)
        assert data == {"key": "value"}

    def test_trailing_newline(self, tmp_path):
        path = tmp_path / "test.json"
        write_json(path, {})
        assert path.read_text().endswith("\n")

    def test_creates_parent_dirs(self, tmp_path):
        path = tmp_path / "a" / "b" / "test.json"
        write_json(path, {})
        assert path.exists()

    def test_unicode(self, tmp_path):
        path = tmp_path / "test.json"
        write_json(path, {"text": "Digikoppeling — standaard"})
        content = path.read_text()
        assert "Digikoppeling — standaard" in content


class TestCheckSync:
    def test_in_sync(self, tmp_path):
        source = SAMPLE_DATA

        with patch("generate_marketplace.PLATFORMS") as mock_platforms, \
             patch("generate_marketplace.ROOT_DIR", tmp_path):
            claude_path = tmp_path / ".claude-plugin" / "marketplace.json"
            generated = generate_claude(source)
            write_json(claude_path, generated)
            mock_platforms.items.return_value = [
                ("claude", (claude_path, generate_claude))
            ]

            assert check_sync(source) is True

    def test_out_of_sync(self, tmp_path):
        source = SAMPLE_DATA

        with patch("generate_marketplace.PLATFORMS") as mock_platforms, \
             patch("generate_marketplace.ROOT_DIR", tmp_path):
            claude_path = tmp_path / ".claude-plugin" / "marketplace.json"
            write_json(claude_path, {"different": "data"})
            mock_platforms.items.return_value = [
                ("claude", (claude_path, generate_claude))
            ]

            assert check_sync(source) is False

    def test_missing_file(self, tmp_path):
        source = SAMPLE_DATA

        with patch("generate_marketplace.PLATFORMS") as mock_platforms, \
             patch("generate_marketplace.ROOT_DIR", tmp_path):
            missing_path = tmp_path / "nonexistent" / "marketplace.json"
            mock_platforms.items.return_value = [
                ("claude", (missing_path, generate_claude))
            ]

            assert check_sync(source) is False


class TestGenerateAll:
    def test_generates_both_files(self, tmp_path):
        source = SAMPLE_DATA
        claude_path = tmp_path / ".claude-plugin" / "marketplace.json"
        cursor_path = tmp_path / ".cursor-plugin" / "marketplace.json"

        with patch("generate_marketplace.PLATFORMS", {
            "claude": (claude_path, generate_claude),
            "cursor": (cursor_path, generate_cursor),
        }), patch("generate_marketplace.ROOT_DIR", tmp_path):
            results = generate_all(source)

        assert claude_path.exists()
        assert cursor_path.exists()
        assert "claude" in results
        assert "cursor" in results

        with open(claude_path) as f:
            claude_data = json.load(f)
        assert claude_data["$schema"] == CLAUDE_SCHEMA

        with open(cursor_path) as f:
            cursor_data = json.load(f)
        assert cursor_data["metadata"]["pluginRoot"] == ".cursor-plugin"


class TestEndToEnd:
    """Test with the real marketplace.json in the repo."""

    def test_real_marketplace(self):
        """Verify the generation script works with the actual marketplace.json."""
        source_path = Path(__file__).resolve().parent.parent.parent / "marketplace.json"
        if not source_path.exists():
            pytest.skip("marketplace.json not found in repo root")

        with open(source_path) as f:
            source = json.load(f)

        # Generate Claude
        claude = generate_claude(source)
        assert "$schema" in claude
        assert len(claude["plugins"]) == len(source["plugins"])

        # Generate Cursor
        cursor = generate_cursor(source)
        assert cursor["metadata"]["pluginRoot"] == ".cursor-plugin"
        assert len(cursor["plugins"]) == len(source["plugins"])

        # Every Cursor plugin should have displayName and source
        for plugin in cursor["plugins"]:
            assert "displayName" in plugin
            assert "source" in plugin
