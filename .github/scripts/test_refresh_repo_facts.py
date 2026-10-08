"""Tests for refresh_repo_facts.py."""

from refresh_repo_facts import apply_facts


def make_plugin(**overrides):
    plugin = {
        "name": "geo",
        "source": {"source": "github", "repo": "org/skills-geo"},
    }
    plugin.update(overrides)
    return plugin


FACTS = {
    "full_name": "org/skills-geo",
    "maintainer": {"login": "org", "name": "Org Naam"},
    "skills": 6,
}


class TestApplyFacts:
    def test_fills_empty_plugin(self):
        plugin = make_plugin()
        changes = apply_facts(plugin, FACTS)
        assert plugin["skills"] == 6
        assert plugin["maintainer"] == {"login": "org", "name": "Org Naam"}
        assert len(changes) == 2

    def test_no_changes_when_current(self):
        plugin = make_plugin(skills=6, maintainer={"login": "org", "name": "Org Naam"})
        assert apply_facts(plugin, FACTS) == []

    def test_detects_transferred_repo(self):
        plugin = make_plugin(skills=6, maintainer={"login": "org", "name": "Org Naam"})
        facts = dict(FACTS, full_name="NieuweOrg/skills-geo")
        changes = apply_facts(plugin, facts)
        assert plugin["source"]["repo"] == "NieuweOrg/skills-geo"
        assert any("source.repo" in c for c in changes)

    def test_updates_skill_count(self):
        plugin = make_plugin(skills=5, maintainer={"login": "org", "name": "Org Naam"})
        changes = apply_facts(plugin, FACTS)
        assert plugin["skills"] == 6
        assert changes == ["skills: 5 -> 6"]

    def test_leaves_non_github_source_alone(self):
        plugin = {
            "name": "x",
            "source": {"source": "url", "url": "https://example.org/x.git"},
            "skills": 6,
            "maintainer": {"login": "org", "name": "Org Naam"},
        }
        assert apply_facts(plugin, FACTS) == []

    def test_missing_skill_count_is_not_written(self):
        plugin = make_plugin(maintainer={"login": "org", "name": "Org Naam"})
        facts = {k: v for k, v in FACTS.items() if k != "skills"}
        apply_facts(plugin, facts)
        assert "skills" not in plugin
