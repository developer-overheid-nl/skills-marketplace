# Plugins voor AI-assisted coding bij de overheid

[![EUPL-1.2](https://img.shields.io/badge/licentie-EUPL--1.2-blue.svg)](LICENSE)
[![plugins](https://img.shields.io/badge/plugins-9-green.svg)](#beschikbare-plugins)
[![CI](https://github.com/developer-overheid-nl/skills-marketplace/actions/workflows/validate.yml/badge.svg)](https://github.com/developer-overheid-nl/skills-marketplace/actions/workflows/validate.yml)

Centrale catalogus van plugins voor AI-assisted coding door developers bij de Nederlandse overheid. Ondersteunt meerdere platformen: [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://developers.openai.com/codex) en [Cursor](https://www.cursor.com/). Via deze marketplace kunnen overheidsteams hun plugins publiceren en ontdekken.

> **CONCEPT** — Deze marketplace is in ontwikkeling. De plugins zijn informatieve samenvattingen — niet de officiële standaarden zelf. Zie onze [verantwoording](docs/verantwoording.md) en [disclaimer](DISCLAIMER.md) voor meer informatie.

## Snel starten

### Claude Code

```bash
# 1. Voeg de marketplace toe
claude plugin marketplace add developer-overheid-nl/skills-marketplace

# 2. Installeer een plugin
claude plugin install standaarden@overheid-plugins
```

**Zet auto-update aan.** Een geïnstalleerde plugin blijft anders staan op de
versie waarmee je hem installeerde, en niets wijst je erop dat er een nieuwe is.
Met auto-update ververst Claude Code de marketplace en werkt het de plugins op
schijf bij:

- **In Claude Code:** `/plugin` → **Marketplaces** → `overheid-plugins` → **Enable auto-update**
- **Of in `~/.claude/settings.json`:**

```json
{
  "extraKnownMarketplaces": {
    "overheid-plugins": {
      "source": { "source": "github", "repo": "developer-overheid-nl/skills-marketplace" },
      "autoUpdate": true
    }
  }
}
```

De waarde in `settings.json` gaat vóór op de toggle in `/plugin`: staat daar
`false`, dan doet de toggle niets. De nieuwe versie laadt bij de volgende start,
of direct met `/reload-plugins`.

Heb je een nieuwe versie meteen nodig, dan werkt dit los van auto-update, dat tot
tien minuten na je eerste bericht wacht en buiten een interactieve sessie niet
draait:

```bash
claude plugin update <plugin>@overheid-plugins
```

### Codex

```bash
# 1. Voeg de marketplace toe
codex plugin marketplace add developer-overheid-nl/skills-marketplace

# 2. Installeer een plugin
codex plugin add standaarden@overheid-plugins
```

Installeren kan ook met `/plugins` in een sessie, of via de Plugins-tab in de
app. Start daarna een nieuwe sessie: Codex laadt de skills bij het opstarten.

Acht van de negen plugins werken nu in Codex. `developer-overheid` volgt zodra
de fix in zijn eigen repository is gemerged: de `name` in het manifest wijkt af
van de naam in deze marketplace, en Codex weigert de installatie dan.

Codex werkt plugins niet zelf bij. Haal eerst de nieuwe versies van de
marketplace op en installeer daarna de plugin opnieuw:

```bash
codex plugin marketplace upgrade overheid-plugins
codex plugin add <plugin>@overheid-plugins
```

Dat tweede commando installeert de nieuwe versie over de oude heen.

### Cursor

Importeer de marketplace via **Plugins & MCPs → Team Marketplaces → Add
Marketplace → Import from Repo** in het Cursor-dashboard, met de repository
`developer-overheid-nl/skills-marketplace`.

Dit werkt alleen op een Teams- of Enterprise-plan, en op Enterprise kan alleen
een admin een marketplace toevoegen.

Zet **Enable Auto Refresh** aan. Cursor ververst de marketplace dan na een push,
hooguit eens per tien minuten; zonder die instelling gebeurt het alleen als je
zelf op **Refresh** klikt. Zie de [Cursor plugin
documentatie](https://cursor.com/docs/plugins) voor meer informatie.

## Demo

![Demo: plugin installeren en browsen](docs/demo.gif)

## Beschikbare plugins

Deze tabel wordt gegenereerd uit `marketplace.json`; bewerk hem niet met de
hand. Zie [Tabel bijwerken](#tabel-bijwerken).

<!-- BEGIN PLUGIN TABLE -->

| Plugin | Skills | Beschrijving | Maintainer |
|--------|--------|-------------|------------|
| [standaarden](https://github.com/developer-overheid-nl/skills-standaarden) | 10 | Skills voor Nederlandse overheidsstandaarden (beheerd door Logius): API Design Rules, Digikoppeling, OAuth NL, FSC, Logboek Dataverwerkingen, CloudEvents, BOMOS, E-Government en Publicatie-tooling | [developer.overheid.nl](https://github.com/developer-overheid-nl) |
| [zad-actions](https://github.com/RijksICTGilde/zad-actions) | 5 | Skills voor ZAD deployment: linting, releases, action validatie, workflow generatie en deployment debugging voor Zelfservice voor Applicatie Deployment | [Rijks ICT Gilde](https://github.com/RijksICTGilde) |
| [developer-overheid](https://github.com/developer-overheid-nl/skills-developer-overheid-nl) | 9 | Dutch Government Developer Knowledge Base (developer.overheid.nl/kennisbank) - guidelines and standards for government software development | [developer.overheid.nl](https://github.com/developer-overheid-nl) |
| [nerds](https://github.com/NederlandseDigitaleDienst/NeRDS) | 14 | Plugin voor de Nederlandse Richtlijn Digitale Systemen (NeRDS) | [Nederlandse Digitale Dienst](https://github.com/NederlandseDigitaleDienst) |
| [internet](https://github.com/developer-overheid-nl/skills-internet) | 5 | Skills voor moderne internetstandaarden (getest via internet.nl): webstandaarden (HTTPS, TLS, DNSSEC, IPv6, RPKI), mailstandaarden (DMARC, DKIM, SPF, STARTTLS, DANE), batch API en implementatiegidsen uit de toolbox-wiki | [developer.overheid.nl](https://github.com/developer-overheid-nl) |
| [geo](https://github.com/developer-overheid-nl/skills-geo) | 6 | Skills voor Nederlandse geo-standaarden (beheerd door Geonovum): OGC API services (WMS, WFS, WMTS, OGC API Features), metadata (ISO 19115, NGR), informatiemodellen (NEN 3610, MIM), INSPIRE implementatie en 3D standaarden (CityGML, 3D Tiles) | [developer.overheid.nl](https://github.com/developer-overheid-nl) |
| [developer-overheid-open-source-repo](https://github.com/developer-overheid-nl/repo-docs-generator) | 1 | Maak een repository klaar voor open source: vul input.json en genereer README, LICENSE, SECURITY, CODE_OF_CONDUCT, CONTRIBUTING, CHANGELOG en publiccode.yml met de repo-docs-generator CLI | [developer.overheid.nl](https://github.com/developer-overheid-nl) |
| [nldd-design-system](https://github.com/NederlandseDigitaleDienst/design-system) | 6 | Bouw applicaties met het NLDD Designsysteem (@nldd/design-system) | [Nederlandse Digitale Dienst](https://github.com/NederlandseDigitaleDienst) |
| [nldd-archi](https://github.com/NederlandseDigitaleDienst/ai-assisted-architecting) | 3 | Werk aan native ArchiMate-modellen (.archimate) met de archi-CLI | [Nederlandse Digitale Dienst](https://github.com/NederlandseDigitaleDienst) |

<!-- END PLUGIN TABLE -->

## Plugin toevoegen

Heb je een plugin die relevant is voor de Nederlandse overheid? Voeg hem toe aan deze marketplace:

1. **Plugin bouwen** - Zie [docs/plugin-maken.md](docs/plugin-maken.md) voor een stap-voor-stap handleiding
2. **Plugin aanmelden** - Zie [docs/plugin-toevoegen.md](docs/plugin-toevoegen.md) of open een [issue](../../issues/new?template=plugin-aanmelding.yml)

### Kwaliteitseisen

- Open-source licentie (EUPL-1.2, Apache-2.0, MIT, of vergelijkbaar)
- Publieke GitHub repository
- Geldige `.plugin/plugin.json`, met een `name` die gelijk is aan de naam in de
  marketplace (Codex weigert de plugin als die twee verschillen)
- Minimaal 1 werkende skill, command of agent, in `skills/<naam>/SKILL.md` (een
  `SKILL.md` in de root wordt niet gevonden)
- Nederlandse of tweetalige documentatie

Zie [CONTRIBUTING.md](CONTRIBUTING.md) voor het volledige review-proces.

## Structuur

```
marketplace.json              # Neutraal formaat (single source of truth)
.claude-plugin/
  marketplace.json            # Gegenereerd voor Claude Code
.cursor-plugin/
  marketplace.json            # Gegenereerd voor Cursor
.agents/plugins/
  marketplace.json            # Gegenereerd voor Codex
.github/scripts/
  generate_marketplace.py     # Genereert platform-bestanden
  generate_readme_table.py    # Genereert de plugin-tabel in deze README
  refresh_repo_facts.py       # Haalt skills, maintainer en repo-pad op uit GitHub
docs/
  plugin-maken.md             # Handleiding: plugin bouwen
  plugin-toevoegen.md         # Handleiding: plugin registreren
```

### Cross-platform architectuur

Het neutrale `marketplace.json` in de root is de single source of truth. Platform-specifieke bestanden worden gegenereerd door `generate_marketplace.py`. CI controleert of de gegenereerde bestanden in sync zijn.

```bash
# Genereer platform-bestanden
uv run python .github/scripts/generate_marketplace.py

# Controleer of alles in sync is
uv run python .github/scripts/generate_marketplace.py --check
```

Codex krijgt een eigen bestand in plaats van het Claude Code-bestand te hergebruiken. Codex leest `.agents/plugins/marketplace.json` namelijk eerst, en kent het source-type `github` niet: een plugin die zo'n source gebruikt wordt zonder melding overgeslagen. In het Codex-bestand staan daarom clone-URL's, plus de velden `policy` en `category` die Codex verwacht. CI controleert dat er geen source-type in staat dat Codex stil negeert.

Een nieuw platform toevoegen (bijv. Windsurf, Copilot) vereist alleen een nieuwe `generate_<platform>()` functie in het script.

### Tabel bijwerken

De plugin-tabel onder [Beschikbare plugins](#beschikbare-plugins) wordt gegenereerd
uit `marketplace.json`, net als de platform-bestanden. CI controleert of de tabel
actueel is, dus een handmatige bewerking faalt in de PR.

Drie velden komen niet uit de aanmelding maar uit de bron-repository zelf: het
aantal skills, de maintainer, en het canonieke repo-pad. Die lopen stil uit de
pas. Wordt een repository overgedragen aan een andere organisatie, dan blijft
GitHub doorverwijzen en werkt de oude verwijzing gewoon, terwijl de tabel de
verkeerde eigenaar vermeldt. `refresh_repo_facts.py` haalt ze op en zet ze in
`marketplace.json`.

```bash
# Haal skills, maintainer en repo-pad op uit GitHub
uv run python .github/scripts/refresh_repo_facts.py

# Genereer de tabel opnieuw
uv run python .github/scripts/generate_readme_table.py

# Controleer of de tabel actueel is (draait ook in CI)
uv run python .github/scripts/generate_readme_table.py --check
```

De dagelijkse `check-versions` workflow draait de refresh mee en neemt de
wijzigingen op in dezelfde bump-PR, dus normaal gebeurt dit vanzelf.

## Disclaimer

Dit is een experimenteel project om te leren hoe generatieve AI gestuurd kan worden om te werken volgens de kaders, richtlijnen en standaarden van de overheid. De plugins in deze marketplace bevatten informatieve samenvattingen — **niet** de officiële standaarden zelf. De definities op [Forum Standaardisatie](https://www.forumstandaardisatie.nl/open-standaarden) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Overheidsbreed standpunt voor de inzet van generatieve AI](https://open.overheid.nl/documenten/bc03ce31-0cf1-4946-9c94-e934a62ebe73/file). Zie [DISCLAIMER.md](DISCLAIMER.md) voor de volledige disclaimer en [verantwoording](docs/verantwoording.md) voor de achtergrond van dit experiment.

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
