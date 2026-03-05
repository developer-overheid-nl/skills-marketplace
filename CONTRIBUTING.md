# Bijdragen aan de Overheid AI-Assistant Plugins Marketplace

Bedankt voor je interesse om een plugin toe te voegen aan de marketplace!

## Kwaliteitseisen

Elke plugin moet voldoen aan:

### Verplicht

- **Open-source licentie** - EUPL-1.2, Apache-2.0, MIT, of vergelijkbaar
- **Publieke GitHub repository** - de plugin-code moet openbaar toegankelijk zijn
- **Geldig manifest** - `.plugin/plugin.json` met minimaal `name`, `description`, `version`
- **Minimaal 1 component** - een werkende skill, command, agent, hook of MCP server
- **Documentatie** - README met installatie-instructies en beschrijving

### Aanbevolen

- Nederlandse of tweetalige documentatie
- CHANGELOG.md
- CI/CD pipeline die de plugin valideert
- Voorbeelden van gebruik

## Plugin aanmelden

Er zijn twee manieren om een plugin aan te melden:

### 1. Via een issue (aanbevolen)

Open een [Plugin aanmelding](../../issues/new?template=plugin-aanmelding.yml) issue. Vul het formulier in en wij reviewen je plugin.

### 2. Via een pull request

1. Fork deze repository
2. Voeg je plugin toe aan `marketplace.json` (in de root)
3. Draai `python .github/scripts/generate_marketplace.py` om platform-bestanden te genereren
4. Open een pull request met een beschrijving van je plugin

Zie [docs/plugin-toevoegen.md](docs/plugin-toevoegen.md) voor gedetailleerde instructies.

## Review-proces

1. **Automatische checks** - CI valideert de JSON-structuur en controleert of de plugin-repo bereikbaar is
2. **Handmatige review** - een maintainer bekijkt de plugin op kwaliteit en relevantie
3. **Feedback** - eventuele opmerkingen worden in de PR of het issue geplaatst
4. **Merge** - na goedkeuring wordt de plugin toegevoegd aan de marketplace

## Plugin-naam als namespace

De `name` in je `plugin.json` wordt de namespace-prefix voor je skills. Gebruikers roepen skills aan als `/plugin-naam:skill-naam`, bijvoorbeeld:

- `/logius-standaarden:ls-api`
- `/zad-actions:lint`

Zorg ervoor dat:
- De plugin-naam uniek en beschrijvend is (kebab-case)
- Skill-namen binnen je plugin uniek zijn
- Namen niet lijken op officiële platform-plugins (Anthropic, Cursor, etc.)

## Vragen?

Open een [issue](../../issues) of neem contact op via standaarden@logius.nl.
