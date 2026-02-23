# Overheid Claude Plugins

[![EUPL-1.2](https://img.shields.io/badge/licentie-EUPL--1.2-blue.svg)](LICENSE)
[![plugins](https://img.shields.io/badge/plugins-7-green.svg)](#beschikbare-plugins)
[![CI](https://github.com/MinBZK/overheid-claude-plugins/actions/workflows/validate.yml/badge.svg)](https://github.com/MinBZK/overheid-claude-plugins/actions/workflows/validate.yml)

Centrale catalogus van [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugins voor de Nederlandse overheid. Via deze marketplace kunnen overheidsteams hun Claude Code plugins publiceren en ontdekken.

## Snel starten

```bash
# 1. Voeg de marketplace toe
claude plugin marketplace add MinBZK/overheid-claude-plugins

# 2. Installeer een plugin
claude plugin install logius-standaarden@overheid-plugins
```

![Demo: plugin installeren en browsen](docs/demo.gif)

## Beschikbare plugins

| Plugin | Skills | Beschrijving | Maintainer |
|--------|--------|-------------|------------|
| [logius-standaarden](https://github.com/MinBZK/logius-standaarden-plugin) | 10 | Skills voor 77 Logius standaarden repositories: API Design Rules, Digikoppeling, OAuth NL, FSC, CloudEvents, BOMOS, en meer | [MinBZK](https://github.com/MinBZK) |
| [zad-actions](https://github.com/RijksICTGilde/zad-actions) | 5 | Skills voor ZAD deployment: linting, releases, action validatie, workflow generatie en debugging | [Rijks ICT Gilde](https://github.com/RijksICTGilde) |
| [developer-overheid](https://github.com/dstotijn/developer-overheid-nl-agent-skills) | 9 | Kennisbank van developer.overheid.nl: richtlijnen en standaarden voor overheidssoftwareontwikkeling (API's, data, frontend, infra, security, open source) | [David Stotijn](https://github.com/dstotijn) |
| [nerds](https://github.com/MinBZK/NeRDS) | 14 | Skills voor de Nederlandse Richtlijn Digitale Systemen (NeRDS): 13 richtlijnen voor ontwerpen, ontwikkelen en inkopen van digitale systemen (toegankelijkheid, open source, cloud, veiligheid, privacy, en meer) | [MinBZK](https://github.com/MinBZK) |
| [internet-nl](https://github.com/MinBZK/internet-nl-plugin) | 5 | Skills voor internet.nl: test compliance met moderne internetstandaarden voor websites en mailservers (IPv6, DNSSEC, HTTPS, TLS, DMARC, DKIM, SPF, DANE) | [MinBZK](https://github.com/MinBZK) |
| [geonovum](https://github.com/MinBZK/geonovum-plugin) | 6 | Skills voor Geonovum geo-standaarden: OGC API, WMS, WFS, metadata (ISO 19115), informatiemodellen (NEN 3610, MIM), INSPIRE en 3D | [MinBZK](https://github.com/MinBZK) |
| [bio-security-baseline](https://github.com/MinBZK/bio-security-baseline-plugin) | 1 | BIO2 security baseline: verplichte beveiligingsmaatregelen, Forum Standaardisatie-standaarden, NCSC-richtlijnen, NIS2/Cyberbeveiligingswet, EU CRA, AI Act en compliance-informatie | [MinBZK](https://github.com/MinBZK) |

## Plugin toevoegen

Heb je een Claude Code plugin die relevant is voor de Nederlandse overheid? Voeg hem toe aan deze marketplace:

1. **Plugin bouwen** - Zie [docs/plugin-maken.md](docs/plugin-maken.md) voor een stap-voor-stap handleiding
2. **Plugin aanmelden** - Zie [docs/plugin-toevoegen.md](docs/plugin-toevoegen.md) of open een [issue](../../issues/new?template=plugin-aanmelding.yml)

### Kwaliteitseisen

- Open-source licentie (EUPL-1.2, Apache-2.0, MIT, of vergelijkbaar)
- Publieke GitHub repository
- Geldige `.claude-plugin/plugin.json`
- Minimaal 1 werkende skill, command of agent
- Nederlandse of tweetalige documentatie

Zie [CONTRIBUTING.md](CONTRIBUTING.md) voor het volledige review-proces.

## Structuur

```
.claude-plugin/
  marketplace.json      # Catalogus met alle plugins
docs/
  plugin-maken.md       # Handleiding: plugin bouwen
  plugin-toevoegen.md   # Handleiding: plugin registreren
```

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
