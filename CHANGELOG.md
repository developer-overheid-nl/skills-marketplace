# Changelog

Alle noemenswaardige wijzigingen aan deze marketplace worden hier gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.1.0/)
en dit project volgt [Semantic Versioning](https://semver.org/lang/nl/).

## [Unreleased]

### Toegevoegd

- CI workflow voor automatische plugin versie-checks (dagelijks, maakt PR bij versie-drift)
- Versie-vergelijking met normalisatie (v-prefix, trailing .0)
- Tests voor check-versions script

## [1.1.0] - 2026-02-23

### Toegevoegd

- Plugin: bio-security-baseline v0.2.0 (1 skill voor BIO2 informatiebeveiliging)
  - Source verplaatst van djimit/bio-security-baseline naar MinBZK/bio-security-baseline-plugin

## [1.0.0] - 2026-02-16

### Toegevoegd

- Marketplace opgezet als centrale catalogus voor overheids AI-assistant plugins
- Plugin: logius-standaarden v1.0.0 (10 skills voor 88 Logius standaarden repositories)
- Plugin: zad-actions v1.0.0 (3 skills voor ZAD deployment)
- Documentatie: plugin-maken.md handleiding
- Documentatie: plugin-toevoegen.md handleiding
- CI workflow voor validatie van marketplace.json
- Issue template voor plugin-aanmeldingen
- PR template

[Unreleased]: https://github.com/developer-overheid-nl/skills-marketplace/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/developer-overheid-nl/skills-marketplace/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/developer-overheid-nl/skills-marketplace/releases/tag/v1.0.0
