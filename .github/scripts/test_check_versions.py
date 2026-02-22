"""Tests for check_versions.py."""

import json
from unittest.mock import MagicMock, patch

import pytest

from check_versions import (
    apply_updates,
    build_branch_and_title,
    build_pr_body,
    detect_updates,
    normalize_version,
    resolve_repo,
    sanitize_branch,
    versions_equal,
)


class TestNormalizeVersion:
    def test_simple(self):
        assert normalize_version("1.2.3") == "1.2.3"

    def test_strip_v_prefix(self):
        assert normalize_version("v1.2.3") == "1.2.3"

    def test_strip_V_prefix(self):
        assert normalize_version("V1.2.3") == "1.2.3"

    def test_trailing_zero(self):
        assert normalize_version("1.2.0") == "1.2"

    def test_trailing_zeros(self):
        assert normalize_version("1.0.0") == "1"

    def test_whitespace(self):
        assert normalize_version("  1.2.3  ") == "1.2.3"

    def test_single_digit(self):
        assert normalize_version("1") == "1"

    def test_empty(self):
        assert normalize_version("") == ""


class TestVersionsEqual:
    def test_identical(self):
        assert versions_equal("1.2.3", "1.2.3")

    def test_v_prefix(self):
        assert versions_equal("v1.2.3", "1.2.3")

    def test_trailing_zero(self):
        assert versions_equal("1.2", "1.2.0")

    def test_trailing_zeros(self):
        assert versions_equal("1", "1.0.0")

    def test_different(self):
        assert not versions_equal("1.2.3", "1.3.0")

    def test_v_prefix_different(self):
        assert not versions_equal("v1.2.0", "1.3.0")


class TestSanitizeBranch:
    def test_simple(self):
        assert sanitize_branch("hello-world") == "hello-world"

    def test_dots_removed(self):
        assert "." not in sanitize_branch("v1.2.3")

    def test_spaces(self):
        assert sanitize_branch("hello world") == "hello-world"

    def test_special_chars(self):
        assert sanitize_branch("a@b#c$d") == "a-b-c-d"

    def test_path_traversal_dots(self):
        result = sanitize_branch("../../etc/passwd")
        assert ".." not in result
        assert "/" not in result

    def test_consecutive_dashes_collapsed(self):
        assert "--" not in sanitize_branch("a--b---c")

    def test_leading_trailing_dashes_stripped(self):
        result = sanitize_branch("---hello---")
        assert not result.startswith("-")
        assert not result.endswith("-")

    def test_empty_returns_unknown(self):
        assert sanitize_branch("...") == "unknown"

    def test_underscores_preserved(self):
        assert sanitize_branch("hello_world") == "hello_world"


class TestResolveRepo:
    def test_github_source(self):
        plugin = {
            "source": {"source": "github", "repo": "MinBZK/logius-standaarden-plugin"}
        }
        assert resolve_repo(plugin) == "MinBZK/logius-standaarden-plugin"

    def test_github_source_missing_repo(self):
        plugin = {"source": {"source": "github"}}
        assert resolve_repo(plugin) is None

    def test_url_source_github(self):
        plugin = {
            "source": {
                "source": "url",
                "url": "https://github.com/MinBZK/test-repo.git",
            }
        }
        assert resolve_repo(plugin) == "MinBZK/test-repo"

    def test_url_source_non_github(self):
        plugin = {
            "source": {"source": "url", "url": "https://gitlab.com/org/repo"}
        }
        assert resolve_repo(plugin) is None

    def test_unknown_source_type(self):
        plugin = {"source": {"source": "npm", "package": "test"}}
        assert resolve_repo(plugin) is None

    def test_no_source(self):
        plugin = {"name": "test"}
        assert resolve_repo(plugin) is None

    def test_source_not_dict(self):
        plugin = {"source": "some-string"}
        assert resolve_repo(plugin) is None


class TestApplyUpdates:
    def test_version_update(self):
        data = {"plugins": [{"name": "test", "version": "1.0.0", "description": "old"}]}
        updates = [
            {
                "name": "test",
                "version_changed": True,
                "description_changed": False,
                "new_version": "2.0.0",
                "new_description": "old",
            }
        ]
        apply_updates(data, updates)
        assert data["plugins"][0]["version"] == "2.0.0"
        assert data["plugins"][0]["description"] == "old"

    def test_description_update(self):
        data = {"plugins": [{"name": "test", "version": "1.0.0", "description": "old"}]}
        updates = [
            {
                "name": "test",
                "version_changed": False,
                "description_changed": True,
                "new_version": "1.0.0",
                "new_description": "new desc",
            }
        ]
        apply_updates(data, updates)
        assert data["plugins"][0]["version"] == "1.0.0"
        assert data["plugins"][0]["description"] == "new desc"

    def test_both_updated(self):
        data = {"plugins": [{"name": "test", "version": "1.0.0", "description": "old"}]}
        updates = [
            {
                "name": "test",
                "version_changed": True,
                "description_changed": True,
                "new_version": "2.0.0",
                "new_description": "new desc",
            }
        ]
        apply_updates(data, updates)
        assert data["plugins"][0]["version"] == "2.0.0"
        assert data["plugins"][0]["description"] == "new desc"

    def test_no_match(self):
        data = {"plugins": [{"name": "other", "version": "1.0.0", "description": "old"}]}
        updates = [
            {
                "name": "test",
                "version_changed": True,
                "description_changed": False,
                "new_version": "2.0.0",
                "new_description": "old",
            }
        ]
        apply_updates(data, updates)
        assert data["plugins"][0]["version"] == "1.0.0"


class TestBuildBranchAndTitle:
    def test_single_version_update(self):
        updates = [
            {
                "name": "logius-standaarden",
                "version_changed": True,
                "description_changed": False,
                "new_version": "1.3.0",
            }
        ]
        branch, title = build_branch_and_title(updates)
        assert branch.startswith("automated/bump-")
        assert "logius-standaarden" in branch
        assert "v1-3-0" in branch
        assert "logius-standaarden" in title

    def test_single_description_update(self):
        updates = [
            {
                "name": "test-plugin",
                "version_changed": False,
                "description_changed": True,
                "new_version": "1.0.0",
            }
        ]
        branch, title = build_branch_and_title(updates)
        assert "description" in branch
        assert "description" in title

    def test_multiple_updates(self):
        updates = [
            {
                "name": "plugin-a",
                "version_changed": True,
                "description_changed": False,
                "new_version": "2.0.0",
            },
            {
                "name": "plugin-b",
                "version_changed": True,
                "description_changed": False,
                "new_version": "3.0.0",
            },
        ]
        branch, title = build_branch_and_title(updates)
        assert branch.startswith("automated/bump-plugins-")
        assert "Update 2 plugins" in title

    def test_branch_is_valid_git_ref(self):
        updates = [
            {
                "name": "plugin with spaces & symbols!",
                "version_changed": True,
                "description_changed": False,
                "new_version": "1.0.0",
            }
        ]
        branch, _ = build_branch_and_title(updates)
        # Should not contain spaces or special chars
        assert " " not in branch
        assert "&" not in branch
        assert "!" not in branch


class TestBuildPrBody:
    def test_contains_table(self):
        updates = [
            {
                "name": "test",
                "repo": "org/repo",
                "version_changed": True,
                "description_changed": False,
                "old_version": "1.0.0",
                "new_version": "2.0.0",
                "old_description": "",
                "new_description": "",
            }
        ]
        body = build_pr_body(updates)
        assert "| Plugin |" in body
        assert "| test |" in body
        assert "1.0.0" in body
        assert "2.0.0" in body

    def test_contains_checklist(self):
        updates = [
            {
                "name": "test",
                "repo": "org/repo",
                "version_changed": True,
                "description_changed": False,
                "old_version": "1.0.0",
                "new_version": "2.0.0",
                "old_description": "",
                "new_description": "",
            }
        ]
        body = build_pr_body(updates)
        assert "Review checklist" in body
        assert "- [ ]" in body

    def test_long_description_truncated(self):
        updates = [
            {
                "name": "test",
                "repo": "org/repo",
                "version_changed": False,
                "description_changed": True,
                "old_version": "1.0.0",
                "new_version": "1.0.0",
                "old_description": "a" * 100,
                "new_description": "b" * 100,
            }
        ]
        body = build_pr_body(updates)
        assert "..." in body


class TestDetectUpdates:
    @patch("check_versions.fetch_upstream_plugin")
    def test_no_changes(self, mock_fetch):
        mock_fetch.return_value = {"version": "1.0.0", "description": "desc"}
        plugins = [
            {
                "name": "test",
                "version": "1.0.0",
                "description": "desc",
                "source": {"source": "github", "repo": "org/test"},
            }
        ]
        updates, summary = detect_updates(plugins)
        assert len(updates) == 0
        assert any("OK:" in s for s in summary)

    @patch("check_versions.fetch_upstream_plugin")
    def test_version_change(self, mock_fetch):
        mock_fetch.return_value = {"version": "2.0.0", "description": "desc"}
        plugins = [
            {
                "name": "test",
                "version": "1.0.0",
                "description": "desc",
                "source": {"source": "github", "repo": "org/test"},
            }
        ]
        updates, summary = detect_updates(plugins)
        assert len(updates) == 1
        assert updates[0]["new_version"] == "2.0.0"

    @patch("check_versions.fetch_upstream_plugin")
    def test_v_prefix_not_false_positive(self, mock_fetch):
        mock_fetch.return_value = {"version": "v1.0.0", "description": "desc"}
        plugins = [
            {
                "name": "test",
                "version": "1.0.0",
                "description": "desc",
                "source": {"source": "github", "repo": "org/test"},
            }
        ]
        updates, _ = detect_updates(plugins)
        assert len(updates) == 0

    @patch("check_versions.fetch_upstream_plugin")
    def test_trailing_zero_not_false_positive(self, mock_fetch):
        mock_fetch.return_value = {"version": "1.2", "description": "desc"}
        plugins = [
            {
                "name": "test",
                "version": "1.2.0",
                "description": "desc",
                "source": {"source": "github", "repo": "org/test"},
            }
        ]
        updates, _ = detect_updates(plugins)
        assert len(updates) == 0

    @patch("check_versions.fetch_upstream_plugin")
    def test_upstream_fetch_failure(self, mock_fetch):
        mock_fetch.return_value = None
        plugins = [
            {
                "name": "test",
                "version": "1.0.0",
                "description": "desc",
                "source": {"source": "github", "repo": "org/test"},
            }
        ]
        updates, summary = detect_updates(plugins)
        assert len(updates) == 0
        assert any("WAARSCHUWING" in s for s in summary)

    def test_no_github_repo(self):
        plugins = [
            {
                "name": "test",
                "version": "1.0.0",
                "description": "desc",
                "source": {"source": "npm"},
            }
        ]
        updates, summary = detect_updates(plugins)
        assert len(updates) == 0
        assert any("SKIP" in s for s in summary)
