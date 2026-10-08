# Een plugin toevoegen aan de marketplace

Deze handleiding beschrijft hoe je een bestaande plugin registreert in de overheid-plugins marketplace.

## Voorwaarden

Je plugin moet voldoen aan de [kwaliteitseisen](../CONTRIBUTING.md):

- Open-source licentie
- Publieke GitHub repository
- Geldige `.plugin/plugin.json` (en gegenereerde platform-bestanden)
- Minimaal 1 werkende skill, command of agent
- README met documentatie

## Optie 1: Via een issue (aanbevolen)

1. Ga naar [Plugin aanmelding](../../issues/new?template=plugin-aanmelding.yml)
2. Vul het formulier in met je plugin-gegevens
3. Een maintainer reviewt je plugin en voegt deze toe

## Optie 2: Via een pull request

### Stap 1: Fork en clone

```bash
gh repo fork developer-overheid-nl/skills-marketplace --clone
cd skills-marketplace
```

### Stap 2: Voeg je plugin toe aan marketplace.json

Open `marketplace.json` (in de root van het project) en voeg je plugin toe aan de `plugins` array.

De `name` moet exact gelijk zijn aan de `name` in de `.plugin/plugin.json` van je eigen repository. Codex vergelijkt die twee en weigert de plugin te installeren als ze verschillen.

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
| `skills` | Gegenereerd | Aantal skills, opgehaald uit de bron-repo |
| `maintainer` | Gegenereerd | Eigenaar van de bron-repo, opgehaald van GitHub |

De velden `skills` en `maintainer` vul je niet zelf in. `refresh_repo_facts.py`
haalt ze op uit de bron-repository, en de plugin-tabel in de README wordt eruit
gegenereerd. Hetzelfde script corrigeert `source.repo` wanneer een repository is
hernoemd of overgedragen.

### Stap 3: Open een pull request

```bash
git checkout -b add-jouw-plugin
# Haal het aantal skills en de maintainer op uit je repo
python .github/scripts/refresh_repo_facts.py
# Genereer de platform-bestanden en de plugin-tabel in de README
python .github/scripts/generate_marketplace.py
python .github/scripts/generate_readme_table.py
git add marketplace.json .claude-plugin/marketplace.json .cursor-plugin/marketplace.json .agents/plugins/marketplace.json README.md
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

**Claude Code:**
```bash
claude plugin marketplace add developer-overheid-nl/skills-marketplace
claude plugin install jouw-plugin@overheid-plugins
```

**Codex:**
```bash
codex plugin marketplace add developer-overheid-nl/skills-marketplace
codex plugin add jouw-plugin@overheid-plugins
```

**Cursor:** Importeer de marketplace via **Plugins & MCPs → Team Marketplaces → Add Marketplace → Import from Repo** in het dashboard. Dit vereist een Teams- of Enterprise-plan.

## Plugin updaten

Als je een nieuwe versie van je plugin uitbrengt:

1. Update de `version` in je eigen `.plugin/plugin.json`
2. Draai `python scripts/generate_plugin.py` in je plugin-repo om platform-bestanden bij te werken
3. De marketplace detecteert automatisch versie-wijzigingen en maakt een PR aan
4. Gebruikers halen de nieuwe versie op met `claude plugin update <plugin>@overheid-plugins`,
   of automatisch als ze auto-update aan hebben staan voor de marketplace. Let op:
   `claude plugin marketplace update` ververst alleen de index met beschikbare versies,
   het werkt de geïnstalleerde plugin zelf niet bij
5. In Codex werkt bijwerken niet automatisch. Gebruikers draaien
   `codex plugin marketplace upgrade overheid-plugins` en daarna
   `codex plugin add <plugin>@overheid-plugins`, wat de nieuwe versie over de oude
   heen installeert
6. In Cursor ververst de marketplace zichzelf alleen met **Enable Auto Refresh**
   aan, en dan hooguit eens per tien minuten na een push; anders moeten gebruikers
   zelf op **Refresh** klikken
