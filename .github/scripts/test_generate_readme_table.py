"""Tests for generate_readme_table.py."""

import pytest

from generate_readme_table import (
    BEGIN_MARKER,
    END_MARKER,
    escape_cell,
    maintainer_cell,
    render_row,
    render_table,
    replace_table,
    repo_url,
    summarize,
)


class TestSummarize:
    def test_strips_status_prefix(self):
        assert summarize("CONCEPT — Skills voor geo") == "Skills voor geo"

    def test_strips_status_prefix_case_insensitive(self):
        assert summarize("beta - Skills voor geo") == "Skills voor geo"

    def test_keeps_single_sentence_without_trailing_period(self):
        assert (
            summarize("Skills voor geo-standaarden.") == "Skills voor geo-standaarden"
        )

    def test_cuts_at_first_sentence(self):
        text = "Plugin voor NeRDS. Bevat skills voor 13 richtlijnen."
        assert summarize(text) == "Plugin voor NeRDS"

    def test_keeps_filename_with_dot(self):
        text = "Genereer publiccode.yml en input.json met de CLI."
        assert summarize(text) == "Genereer publiccode.yml en input.json met de CLI"

    def test_keeps_version_number(self):
        assert summarize("Vereist archi-cli v1.2.3.") == "Vereist archi-cli v1.2.3"

    def test_cuts_before_parenthesised_sentence(self):
        text = "Bouw applicaties. (Niet voor onderhouders.)"
        assert summarize(text) == "Bouw applicaties"

    def test_empty_description(self):
        assert summarize("") == ""


class TestEscapeCell:
    def test_escapes_pipe(self):
        assert escape_cell("a | b") == "a \\| b"

    def test_flattens_newlines(self):
        assert escape_cell("a\nb") == "a b"


class TestRepoUrl:
    def test_github_source(self):
        plugin = {"source": {"source": "github", "repo": "org/repo"}}
        assert repo_url(plugin) == "https://github.com/org/repo"

    def test_url_source(self):
        plugin = {"source": {"source": "url", "url": "https://example.org/x.git"}}
        assert repo_url(plugin) == "https://example.org/x.git"

    def test_missing_source(self):
        assert repo_url({}) == ""


class TestMaintainerCell:
    def test_uses_stored_display_name(self):
        plugin = {"maintainer": {"login": "org-slug", "name": "Mooie Naam"}}
        assert maintainer_cell(plugin) == "[Mooie Naam](https://github.com/org-slug)"

    def test_falls_back_to_login_when_name_empty(self):
        plugin = {"maintainer": {"login": "org-slug", "name": ""}}
        assert maintainer_cell(plugin) == "[org-slug](https://github.com/org-slug)"

    def test_derives_login_from_source_when_missing(self):
        plugin = {"source": {"source": "github", "repo": "SomeOrg/repo"}}
        assert maintainer_cell(plugin) == "[SomeOrg](https://github.com/SomeOrg)"


class TestRenderRow:
    def test_full_row(self):
        plugin = {
            "name": "geo",
            "description": "CONCEPT — Skills voor geo. Meer tekst.",
            "skills": 6,
            "source": {"source": "github", "repo": "org/skills-geo"},
            "maintainer": {"login": "org", "name": "Org Naam"},
        }
        assert render_row(plugin) == (
            "| [geo](https://github.com/org/skills-geo) | 6 | Skills voor geo "
            "| [Org Naam](https://github.com/org) |"
        )

    def test_missing_skill_count_renders_question_mark(self):
        plugin = {
            "name": "geo",
            "description": "Skills.",
            "source": {"source": "github", "repo": "org/g"},
            "maintainer": {"login": "org", "name": "Org"},
        }
        assert "| ? |" in render_row(plugin)


class TestRenderTable:
    def test_includes_markers_and_header(self):
        data = {
            "plugins": [
                {
                    "name": "geo",
                    "description": "Skills.",
                    "skills": 1,
                    "source": {"source": "github", "repo": "org/g"},
                    "maintainer": {"login": "org", "name": "Org"},
                }
            ]
        }
        table = render_table(data)
        assert table.startswith(BEGIN_MARKER)
        assert table.endswith(END_MARKER)
        assert "| Plugin | Skills | Beschrijving | Maintainer |" in table

    def test_empty_plugin_list(self):
        table = render_table({"plugins": []})
        assert BEGIN_MARKER in table and END_MARKER in table


class TestReplaceTable:
    def test_replaces_between_markers(self):
        readme = f"voor\n{BEGIN_MARKER}\noud\n{END_MARKER}\nna"
        result = replace_table(readme, f"{BEGIN_MARKER}\nnieuw\n{END_MARKER}")
        assert result == f"voor\n{BEGIN_MARKER}\nnieuw\n{END_MARKER}\nna"

    def test_missing_markers_raises(self):
        with pytest.raises(ValueError, match="niet gevonden"):
            replace_table("geen markers", "tabel")

    def test_swapped_markers_raise(self):
        readme = f"{END_MARKER}\n{BEGIN_MARKER}"
        with pytest.raises(ValueError, match="staat voor"):
            replace_table(readme, "tabel")
