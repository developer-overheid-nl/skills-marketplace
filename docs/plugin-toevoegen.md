# Een plugin toevoegen aan de marketplace

Deze handleiding beschrijft hoe je een bestaande Claude Code plugin registreert in de overheid-plugins marketplace.

## Voorwaarden

Je plugin moet voldoen aan de [kwaliteitseisen](../CONTRIBUTING.md):

- Open-source licentie
- Publieke GitHub repository
- Geldige `.claude-plugin/plugin.json`
- Minimaal 1 werkende skill, command of agent
- README met documentatie

## Optie 1: Via een issue (aanbevolen)

1. Ga naar [Plugin aanmelding](../../issues/new?template=plugin-aanmelding.yml)
2. Vul het formulier in met je plugin-gegevens
3. Een maintainer reviewt je plugin en voegt deze toe

## Optie 2: Via een pull request

### Stap 1: Fork en clone

```bash
gh repo fork developer-overheid-nl/overheid-claude-plugins --clone
cd overheid-claude-plugins
```

### Stap 2: Voeg je plugin toe aan marketplace.json

Open `.claude-plugin/marketplace.json` en voeg je plugin toe aan de `plugins` array:

```json
{
  "name": "jouw-plugin",
  "description": "Korte beschrijving van je plugin",
  "version": "1.0.0",
  "author": {
    "name": "Jouw Organisatie",
    "email": "contact@organisatie.nl"
  },
  "source": {
    "source": "github",
    "repo": "organisatie/jouw-plugin"
  },
  "category": "productivity",
  "tags": ["relevante", "zoektermen"]
}
```

### Velden

| Veld | Verplicht | Beschrijving |
|------|-----------|-------------|
| `name` | Ja | Plugin-naam (moet overeenkomen met `name` in je `plugin.json`) |
| `source` | Ja | Waar de plugin te vinden is (GitHub repo) |
| `description` | Aanbevolen | Korte beschrijving |
| `version` | Aanbevolen | Huidige versie (semver) |
| `author` | Aanbevolen | Naam en email van de maintainer |
| `category` | Optioneel | Categorie (productivity, security, testing, etc.) |
| `tags` | Optioneel | Zoektermen voor discovery |

### Stap 3: Open een pull request

```bash
git checkout -b add-jouw-plugin
git add .claude-plugin/marketplace.json
git commit -m "Voeg jouw-plugin toe aan marketplace"
git push origin add-jouw-plugin
gh pr create --title "Voeg jouw-plugin toe" --body "Beschrijving van de plugin en wat deze doet."
```

### Stap 4: Review

- De CI controleert automatisch of de JSON geldig is en de plugin-repo bereikbaar is
- Een maintainer reviewt de plugin op kwaliteit en relevantie
- Na goedkeuring wordt de PR gemerged

## Na toevoeging

Zodra je plugin is toegevoegd kunnen gebruikers deze installeren:

```bash
claude plugin marketplace add developer-overheid-nl/overheid-claude-plugins
claude plugin install jouw-plugin@overheid-plugins
```

## Plugin updaten

Als je een nieuwe versie van je plugin uitbrengt:

1. Update de `version` in je eigen `plugin.json`
2. Open een PR om de `version` in `marketplace.json` bij te werken
3. Gebruikers krijgen de update via `claude plugin marketplace update`
