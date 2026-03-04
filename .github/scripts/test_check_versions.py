"""Tests for check_versions.py."""

import base64
import json
import os
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from check_versions import (
    apply_updates,
    build_branch_and_title,
    build_pr_body,
    check_existing_bump_pr,
    create_pr,
    detect_updates,
    fetch_upstream_plugin,
    main,
    normalize_version,
    regenerate_platform_files,
    resolve_repo,
    sanitize_branch,
    validate_repo,
    versions_equal,
    write_job_summary,
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


class TestValidateRepo:
    def test_valid(self):
        assert validate_repo("MinBZK/logius-standaarden-plugin")

    def test_valid_with_dots(self):
        assert validate_repo("org/repo.name")

    def test_valid_with_underscores(self):
        assert validate_repo("org_name/repo_name")

    def test_invalid_slash_count(self):
        assert not validate_repo("org/repo/extra")

    def test_injection_attempt(self):
        assert not validate_repo("../../etc/passwd")

    def test_semicolon(self):
        assert not validate_repo("org/repo; rm -rf /")

    def test_spaces(self):
        assert not validate_repo("org/repo name")

    def test_empty(self):
        assert not validate_repo("")

    def test_no_slash(self):
        assert not validate_repo("just-a-name")


class TestResolveRepo:
    def test_github_source(self):
        plugin = {
            "source": {"source": "github", "repo": "MinBZK/logius-standaarden-plugin"}
        }
        assert resolve_repo(plugin) == "MinBZK/logius-standaarden-plugin"

    def test_github_source_missing_repo(self):
        plugin = {"source": {"source": "github"}}
        assert resolve_repo(plugin) is None

    def test_github_source_invalid_repo(self):
        plugin = {"source": {"source": "github", "repo": "../../etc/passwd"}}
        assert resolve_repo(plugin) is None

    def test_github_source_injection_attempt(self):
        plugin = {"source": {"source": "github", "repo": "org/repo; rm -rf /"}}
        assert resolve_repo(plugin) is None

    def test_url_source_github(self):
        plugin = {
            "source": {
                "source": "url",
                "url": "https://github.com/MinBZK/test-repo.git",
            }
        }
        assert resolve_repo(plugin) == "MinBZK/test-repo"

    def test_url_source_github_with_trailing_path(self):
        plugin = {
            "source": {
                "source": "url",
                "url": "https://github.com/MinBZK/test-repo/tree/main/something",
            }
        }
        assert resolve_repo(plugin) == "MinBZK/test-repo"

    def test_url_source_non_github(self):
        plugin = {"source": {"source": "url", "url": "https://gitlab.com/org/repo"}}
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

    def test_url_source_single_segment(self):
        plugin = {"source": {"source": "url", "url": "https://github.com/onlyone"}}
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
        data = {
            "plugins": [{"name": "other", "version": "1.0.0", "description": "old"}]
        }
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
        updates, summary, failures = detect_updates(plugins)
        assert len(updates) == 0
        assert failures == 0
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
        updates, summary, failures = detect_updates(plugins)
        assert len(updates) == 1
        assert updates[0]["new_version"] == "2.0.0"
        assert failures == 0

    @patch("check_versions.fetch_upstream_plugin")
    def test_description_only_change(self, mock_fetch):
        mock_fetch.return_value = {"version": "1.0.0", "description": "new desc"}
        plugins = [
            {
                "name": "test",
                "version": "1.0.0",
                "description": "old desc",
                "source": {"source": "github", "repo": "org/test"},
            }
        ]
        updates, summary, failures = detect_updates(plugins)
        assert len(updates) == 1
        assert updates[0]["description_changed"] is True
        assert updates[0]["version_changed"] is False
        assert updates[0]["new_description"] == "new desc"
        assert failures == 0

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
        updates, _, failures = detect_updates(plugins)
        assert len(updates) == 0
        assert failures == 0

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
        updates, _, failures = detect_updates(plugins)
        assert len(updates) == 0
        assert failures == 0

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
        updates, summary, failures = detect_updates(plugins)
        assert len(updates) == 0
        assert failures == 1
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
        updates, summary, failures = detect_updates(plugins)
        assert len(updates) == 0
        assert failures == 0
        assert any("SKIP" in s for s in summary)

    @patch("check_versions.fetch_upstream_plugin")
    def test_description_whitespace_not_false_positive(self, mock_fetch):
        mock_fetch.return_value = {"version": "1.0.0", "description": "desc  "}
        plugins = [
            {
                "name": "test",
                "version": "1.0.0",
                "description": "desc",
                "source": {"source": "github", "repo": "org/test"},
            }
        ]
        updates, _, failures = detect_updates(plugins)
        assert len(updates) == 0
        assert failures == 0

    @patch("check_versions.fetch_upstream_plugin")
    def test_multiple_failures_counted(self, mock_fetch):
        mock_fetch.return_value = None
        plugins = [
            {
                "name": "a",
                "version": "1.0.0",
                "description": "d",
                "source": {"source": "github", "repo": "org/a"},
            },
            {
                "name": "b",
                "version": "1.0.0",
                "description": "d",
                "source": {"source": "github", "repo": "org/b"},
            },
        ]
        _, _, failures = detect_updates(plugins)
        assert failures == 2


class TestFetchUpstreamPlugin:
    @patch("check_versions.subprocess.run")
    def test_success(self, mock_run):
        plugin_data = {"name": "test", "version": "1.0.0"}
        encoded = base64.b64encode(json.dumps(plugin_data).encode()).decode()
        mock_run.return_value = MagicMock(returncode=0, stdout=encoded)

        result = fetch_upstream_plugin("org/repo")
        assert result == plugin_data

    @patch("check_versions.subprocess.run")
    def test_api_failure(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1, stdout="")
        assert fetch_upstream_plugin("org/repo") is None

    @patch("check_versions.subprocess.run")
    def test_invalid_base64(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="not-valid-base64!!!")
        assert fetch_upstream_plugin("org/repo") is None

    @patch("check_versions.subprocess.run")
    def test_invalid_json(self, mock_run):
        encoded = base64.b64encode(b"not json").decode()
        mock_run.return_value = MagicMock(returncode=0, stdout=encoded)
        assert fetch_upstream_plugin("org/repo") is None

    @patch("check_versions.subprocess.run")
    def test_timeout_passed(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="e30=")  # {}
        fetch_upstream_plugin("org/repo")
        _, kwargs = mock_run.call_args
        assert kwargs.get("timeout") == 60

    @patch("check_versions.subprocess.run")
    def test_timeout_returns_none(self, mock_run):
        mock_run.side_effect = subprocess.TimeoutExpired(cmd="gh", timeout=60)
        assert fetch_upstream_plugin("org/repo") is None


class TestCheckExistingBumpPr:
    @patch("check_versions.subprocess.run")
    def test_found(self, mock_run):
        prs = [{"number": 5, "title": "Bump plugin", "headRefName": "automated/bump-x"}]
        mock_run.return_value = MagicMock(returncode=0, stdout=json.dumps(prs))
        result = check_existing_bump_pr()
        assert result is not None
        assert result["number"] == 5

    @patch("check_versions.subprocess.run")
    def test_no_prs(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="[]")
        assert check_existing_bump_pr() is None

    @patch("check_versions.subprocess.run")
    def test_command_failure(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1, stdout="")
        assert check_existing_bump_pr() is None

    @patch("check_versions.subprocess.run")
    def test_invalid_json(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="not json")
        assert check_existing_bump_pr() is None

    @patch("check_versions.subprocess.run")
    def test_label_match_without_branch_prefix(self, mock_run):
        """Any PR with automated-bump label counts, regardless of branch name."""
        prs = [
            {"number": 7, "title": "Manual bump", "headRefName": "manual/some-branch"}
        ]
        mock_run.return_value = MagicMock(returncode=0, stdout=json.dumps(prs))
        result = check_existing_bump_pr()
        assert result is not None
        assert result["number"] == 7


class TestWriteJobSummary:
    def test_writes_to_file(self, tmp_path):
        summary_file = tmp_path / "summary.md"
        with patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary_file)}):
            write_job_summary(["OK: test v1.0.0"], "Extra info")

        content = summary_file.read_text()
        assert "Plugin versie-check resultaten" in content
        assert "OK: test v1.0.0" in content
        assert "Extra info" in content

    def test_no_env_var_does_nothing(self):
        with patch.dict(os.environ, {}, clear=True):
            # Should not raise
            write_job_summary(["OK: test v1.0.0"])

    def test_emoji_for_ok(self, tmp_path):
        summary_file = tmp_path / "summary.md"
        with patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary_file)}):
            write_job_summary(["OK: test"])
        assert "\u2705" in summary_file.read_text()

    def test_emoji_for_update(self, tmp_path):
        summary_file = tmp_path / "summary.md"
        with patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary_file)}):
            write_job_summary(["UPDATE: test"])
        assert "\U0001f504" in summary_file.read_text()

    def test_emoji_for_warning(self, tmp_path):
        summary_file = tmp_path / "summary.md"
        with patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary_file)}):
            write_job_summary(["WAARSCHUWING: test"])
        assert "\u26a0\ufe0f" in summary_file.read_text()


MOCK_PLATFORM_FILES = [".claude-plugin/marketplace.json", ".cursor-plugin/marketplace.json"]


class TestCreatePr:
    @pytest.fixture(autouse=True)
    def _mock_regenerate(self, monkeypatch):
        monkeypatch.setattr(
            "check_versions.regenerate_platform_files",
            lambda: MOCK_PLATFORM_FILES,
        )

    @patch("check_versions.subprocess.run")
    def test_success(self, mock_run, tmp_path):
        marketplace = tmp_path / "marketplace.json"
        marketplace.write_text('{"plugins": []}')

        # Mock all subprocess calls to succeed
        mock_run.return_value = MagicMock(
            returncode=0, stdout="https://github.com/org/repo/pull/1\n", stderr=""
        )

        data = {"plugins": [{"name": "test", "version": "2.0.0"}]}
        updates = [{"name": "test", "new_version": "2.0.0"}]

        url = create_pr(
            str(marketplace),
            data,
            updates,
            "automated/bump-test",
            "Update test",
            "body",
        )
        assert url == "https://github.com/org/repo/pull/1"

        # Verify marketplace.json was written correctly
        written = json.loads(marketplace.read_text())
        assert written["plugins"][0]["version"] == "2.0.0"

    @patch("check_versions.subprocess.run")
    def test_push_failure_exits(self, mock_run, tmp_path):
        marketplace = tmp_path / "marketplace.json"
        marketplace.write_text('{"plugins": []}')

        def side_effect(cmd, **kwargs):
            if cmd[:2] == ["git", "push"]:
                return MagicMock(returncode=1, stderr="push failed", stdout="")
            return MagicMock(returncode=0, stdout="", stderr="")

        mock_run.side_effect = side_effect

        data = {"plugins": []}
        with pytest.raises(SystemExit) as exc:
            create_pr(
                str(marketplace), data, [{"name": "x"}], "branch", "title", "body"
            )
        assert exc.value.code == 1

    @patch("check_versions.subprocess.run")
    def test_pr_create_failure_exits(self, mock_run, tmp_path):
        marketplace = tmp_path / "marketplace.json"
        marketplace.write_text('{"plugins": []}')

        def side_effect(cmd, **kwargs):
            if cmd[:3] == ["gh", "pr", "create"]:
                return MagicMock(returncode=1, stderr="pr create failed", stdout="")
            return MagicMock(returncode=0, stdout="url", stderr="")

        mock_run.side_effect = side_effect

        data = {"plugins": []}
        with pytest.raises(SystemExit) as exc:
            create_pr(
                str(marketplace), data, [{"name": "x"}], "branch", "title", "body"
            )
        assert exc.value.code == 1

    @patch("check_versions.subprocess.run")
    def test_git_config_failure_exits(self, mock_run, tmp_path):
        marketplace = tmp_path / "marketplace.json"
        marketplace.write_text('{"plugins": []}')

        def side_effect(cmd, **kwargs):
            if cmd[:2] == ["git", "config"]:
                return MagicMock(returncode=1, stderr="config failed", stdout="")
            return MagicMock(returncode=0, stdout="", stderr="")

        mock_run.side_effect = side_effect

        data = {"plugins": []}
        with pytest.raises(SystemExit) as exc:
            create_pr(
                str(marketplace), data, [{"name": "x"}], "branch", "title", "body"
            )
        assert exc.value.code == 1

    @patch("check_versions.subprocess.run")
    def test_timeout_on_subprocess_calls(self, mock_run, tmp_path):
        marketplace = tmp_path / "marketplace.json"
        marketplace.write_text('{"plugins": []}')

        mock_run.return_value = MagicMock(returncode=0, stdout="url\n", stderr="")

        data = {"plugins": []}
        create_pr(str(marketplace), data, [{"name": "x"}], "branch", "title", "body")

        # Verify every subprocess.run call got a timeout
        for call in mock_run.call_args_list:
            _, kwargs = call
            assert "timeout" in kwargs, f"Missing timeout in call: {call}"

    @patch("check_versions.subprocess.run")
    def test_triggers_validate_workflow(self, mock_run, tmp_path):
        marketplace = tmp_path / "marketplace.json"
        marketplace.write_text('{"plugins": []}')

        mock_run.return_value = MagicMock(returncode=0, stdout="url\n", stderr="")

        data = {"plugins": []}
        create_pr(str(marketplace), data, [{"name": "x"}], "my-branch", "title", "body")

        # Find the workflow dispatch call
        workflow_calls = [
            call
            for call in mock_run.call_args_list
            if call[0][0][:3] == ["gh", "workflow", "run"]
        ]
        assert len(workflow_calls) == 1
        cmd = workflow_calls[0][0][0]
        assert "validate.yml" in cmd
        assert "--ref" in cmd
        assert "my-branch" in cmd

    @patch("check_versions.subprocess.run")
    def test_multi_update_commit_message(self, mock_run, tmp_path):
        marketplace = tmp_path / "marketplace.json"
        marketplace.write_text('{"plugins": []}')

        mock_run.return_value = MagicMock(returncode=0, stdout="url\n", stderr="")

        data = {"plugins": []}
        updates = [
            {"name": "a", "new_version": "1.0"},
            {"name": "b", "new_version": "2.0"},
        ]
        create_pr(str(marketplace), data, updates, "branch", "Update 2 plugins", "body")

        # Find the commit call and check message
        for call in mock_run.call_args_list:
            args = call[0][0]
            if args[:2] == ["git", "commit"]:
                assert "a, b" in args[3]


class TestMain:
    @patch("check_versions.create_pr")
    @patch("check_versions.check_existing_bump_pr")
    @patch("check_versions.fetch_upstream_plugin")
    @patch("builtins.open", create=True)
    def test_all_up_to_date(
        self, mock_file_open, mock_fetch, mock_pr_check, mock_create
    ):
        data = {
            "plugins": [
                {
                    "name": "test",
                    "version": "1.0.0",
                    "description": "desc",
                    "source": {"source": "github", "repo": "org/test"},
                }
            ]
        }
        mock_file_open.return_value.__enter__ = lambda s: s
        mock_file_open.return_value.__exit__ = MagicMock(return_value=False)
        mock_file_open.return_value.read = MagicMock(return_value=json.dumps(data))

        mock_fetch.return_value = {"version": "1.0.0", "description": "desc"}

        with patch("json.load", return_value=data):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 0

        mock_create.assert_not_called()

    @patch("check_versions.write_job_summary")
    @patch("check_versions.fetch_upstream_plugin")
    @patch("builtins.open", create=True)
    def test_all_fetches_fail_exits_with_error(
        self, mock_file_open, mock_fetch, mock_summary
    ):
        data = {
            "plugins": [
                {
                    "name": "a",
                    "version": "1.0.0",
                    "description": "d",
                    "source": {"source": "github", "repo": "org/a"},
                },
                {
                    "name": "b",
                    "version": "1.0.0",
                    "description": "d",
                    "source": {"source": "github", "repo": "org/b"},
                },
            ]
        }
        mock_file_open.return_value.__enter__ = lambda s: s
        mock_file_open.return_value.__exit__ = MagicMock(return_value=False)

        mock_fetch.return_value = None

        with patch("json.load", return_value=data):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1

    @patch("check_versions.create_pr", return_value="https://example.com/pr/1")
    @patch("check_versions.check_existing_bump_pr", return_value=None)
    @patch("check_versions.fetch_upstream_plugin")
    @patch("builtins.open", create=True)
    def test_creates_pr_on_drift(
        self, mock_file_open, mock_fetch, mock_pr_check, mock_create
    ):
        data = {
            "plugins": [
                {
                    "name": "test",
                    "version": "1.0.0",
                    "description": "desc",
                    "source": {"source": "github", "repo": "org/test"},
                }
            ]
        }
        mock_file_open.return_value.__enter__ = lambda s: s
        mock_file_open.return_value.__exit__ = MagicMock(return_value=False)

        mock_fetch.return_value = {"version": "2.0.0", "description": "desc"}

        with patch("json.load", return_value=data):
            main()

        mock_create.assert_called_once()

    @patch("check_versions.create_pr")
    @patch("check_versions.check_existing_bump_pr")
    @patch("check_versions.fetch_upstream_plugin")
    @patch("builtins.open", create=True)
    def test_skips_pr_if_existing(
        self, mock_file_open, mock_fetch, mock_pr_check, mock_create
    ):
        data = {
            "plugins": [
                {
                    "name": "test",
                    "version": "1.0.0",
                    "description": "desc",
                    "source": {"source": "github", "repo": "org/test"},
                }
            ]
        }
        mock_file_open.return_value.__enter__ = lambda s: s
        mock_file_open.return_value.__exit__ = MagicMock(return_value=False)

        mock_fetch.return_value = {"version": "2.0.0", "description": "desc"}
        mock_pr_check.return_value = {"number": 5, "title": "Existing PR"}

        with patch("json.load", return_value=data):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 0

        mock_create.assert_not_called()
