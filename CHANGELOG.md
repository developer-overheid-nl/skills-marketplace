# Changelog

Alle noemenswaardige wijzigingen aan deze marketplace worden hier gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.1.0/)
en dit project volgt [Semantic Versioning](https://semver.org/lang/nl/).

## [Unreleased]

### Toegevoegd

- CI workflow voor automatische plugin versie-checks (dagelijks, maakt PR bij versie-drift)
- Versie-vergelijking met normalisatie (v-prefix, trailing .0)
- Tests voor check-versions script

## [1.1.0] - 2026-02-22

### Toegevoegd

- Plugin: bio-security-baseline v0.2.0 (1 skill voor BIO2 informatiebeveiliging)
  - BIO2-overheidsmaatregelen over 13 domeinen (governance, toegangsbeheer, logging, cryptografie, etc.)
  - Implementatie-checklist voor ontwikkelaars
  - Forum Standaardisatie verplichte standaarden (HTTPS/HSTS, TLS, DNSSEC, DMARC, DKIM, SPF, etc.)
  - NCSC-richtlijnen (TLS 2025-05, webapplicaties, basisprincipes)
  - Cyberbeveiligingswet (NIS2-implementatie)
  - EU-regelgeving: Cyber Resilience Act, AI Act, Data Act, eIDAS 2.0
  - DigiToegankelijk (WCAG), authenticatie- en API-standaarden
  - Audit en compliance (ENSIA, DigiD Normenkader, internet.nl)
  - Codevoorbeelden (logging, security headers, security.txt)

## [1.0.0] - 2026-02-16

### Toegevoegd

- Marketplace opgezet als centrale catalogus voor overheids-Claude Code plugins
- Plugin: logius-standaarden v1.0.0 (10 skills voor 88 Logius standaarden repositories)
- Plugin: zad-actions v1.0.0 (3 skills voor ZAD deployment)
- Documentatie: plugin-maken.md handleiding
- Documentatie: plugin-toevoegen.md handleiding
- CI workflow voor validatie van marketplace.json
- Issue template voor plugin-aanmeldingen
- PR template

[Unreleased]: https://github.com/MinBZK/overheid-claude-plugins/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/MinBZK/overheid-claude-plugins/releases/tag/v1.0.0
