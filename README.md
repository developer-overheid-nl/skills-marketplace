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

| Plugin | Skills | Beschrijving | Maintainer |
|--------|--------|-------------|------------|
| [standaarden](https://github.com/developer-overheid-nl/skills-standaarden) | 10 | Skills voor Nederlandse overheidsstandaarden (beheerd door Logius): API Design Rules, Digikoppeling, OAuth NL, FSC, CloudEvents, BOMOS, en meer | [developer-overheid-nl](https://github.com/developer-overheid-nl) |
| [zad-actions](https://github.com/RijksICTGilde/zad-actions) | 5 | Skills voor ZAD deployment: linting, releases, action validatie, workflow generatie en debugging | [Rijks ICT Gilde](https://github.com/RijksICTGilde) |
| [developer-overheid](https://github.com/developer-overheid-nl/skills-developer-overheid-nl) | 9 | Kennisbank van developer.overheid.nl: richtlijnen en standaarden voor overheidssoftwareontwikkeling (API's, data, frontend, infra, security, open source) | [developer-overheid-nl](https://github.com/developer-overheid-nl) |
| [nerds](https://github.com/MinBZK/NeRDS) | 14 | Skills voor de Nederlandse Richtlijn Digitale Systemen (NeRDS): 13 richtlijnen voor ontwerpen, ontwikkelen en inkopen van digitale systemen (toegankelijkheid, open source, cloud, veiligheid, privacy, en meer) | [MinBZK](https://github.com/MinBZK) |
| [internet](https://github.com/developer-overheid-nl/skills-internet) | 5 | Skills voor moderne internetstandaarden (getest via internet.nl): compliance voor websites en mailservers (IPv6, DNSSEC, HTTPS, TLS, DMARC, DKIM, SPF, DANE) | [developer-overheid-nl](https://github.com/developer-overheid-nl) |
| [geo](https://github.com/developer-overheid-nl/skills-geo) | 6 | Skills voor Nederlandse geo-standaarden (beheerd door Geonovum): OGC API, WMS, WFS, metadata (ISO 19115), informatiemodellen (NEN 3610, MIM), INSPIRE en 3D | [developer-overheid-nl](https://github.com/developer-overheid-nl) |
| [developer-overheid-open-source-repo](https://github.com/developer-overheid-nl/skills-open-source-repo) | 1 | Maakt de bestanden aan die een open source project nodig heeft (LICENSE, CODE_OF_CONDUCT, SECURITY, publiccode.yml), of controleert of ze er al zijn | [developer-overheid-nl](https://github.com/developer-overheid-nl) |
| [nldd-design-system](https://github.com/NederlandseDigitaleDienst/design-system) | 6 | Bouw applicaties met het NLDD Designsysteem (@nldd/design-system): componenten opzoeken, een applicatie bouwen, een bestaande frontend migreren, een versie verhogen en wijzigingen voorstellen | [Nederlandse Digitale Dienst](https://github.com/NederlandseDigitaleDienst) |
| [nldd-archi](https://github.com/NederlandseDigitaleDienst/ai-assisted-architecting) | 3 | Werk aan native ArchiMate-modellen (.archimate) met de archi-CLI: het model wijzigen, views genereren en presentaties maken | [Nederlandse Digitale Dienst](https://github.com/NederlandseDigitaleDienst) |

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

## Disclaimer

Dit is een experimenteel project om te leren hoe generatieve AI gestuurd kan worden om te werken volgens de kaders, richtlijnen en standaarden van de overheid. De plugins in deze marketplace bevatten informatieve samenvattingen — **niet** de officiële standaarden zelf. De definities op [Forum Standaardisatie](https://www.forumstandaardisatie.nl/open-standaarden) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Overheidsbreed standpunt voor de inzet van generatieve AI](https://open.overheid.nl/documenten/bc03ce31-0cf1-4946-9c94-e934a62ebe73/file). Zie [DISCLAIMER.md](DISCLAIMER.md) voor de volledige disclaimer en [verantwoording](docs/verantwoording.md) voor de achtergrond van dit experiment.

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
