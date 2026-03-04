# Een Claude Code plugin maken

Deze handleiding beschrijft hoe je een Claude Code plugin bouwt die via de marketplace gedistribueerd kan worden.

## Wat is een plugin?

Een Claude Code plugin is een verzameling skills, commands, agents, hooks en/of MCP servers die Claude Code uitbreiden met domeinkennis of tooling. Plugins worden gedistribueerd via een marketplace en zijn beschikbaar in elke Claude Code sessie.

## Stap 1: Directory-structuur

Maak de volgende structuur aan in je repository:

```
mijn-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest (verplicht)
├── skills/
│   └── mijn-skill/
│       └── SKILL.md         # Skill definitie
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## Stap 2: Plugin manifest

Maak `.claude-plugin/plugin.json`:

```json
{
  "name": "mijn-plugin",
  "description": "Korte beschrijving van wat de plugin doet",
  "version": "1.0.0"
}
```

De `name` wordt de **namespace-prefix** voor je skills. Gebruikers roepen skills aan als `/mijn-plugin:skill-naam`. Kies een unieke, beschrijvende naam in kebab-case.

## Stap 3: Skills schrijven

Maak een `SKILL.md` in `skills/<skill-naam>/`:

```markdown
---
name: mijn-skill
description: >-
  Beschrijving die bepaalt wanneer de skill wordt geactiveerd.
  Gebruik triggerwoorden in zowel Nederlands als Engels.
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - WebFetch(*)
---

## Instructie voor de agent

Beschrijf wanneer en hoe de agent deze skill moet gebruiken.

## Referentie-informatie

Voeg tabellen, beslisbomen, codevoorbeelden toe die de agent nodig heeft.
```

### Tips voor goede skills

- **Description is cruciaal** - dit bepaalt wanneer Claude de skill activeert. Gebruik relevante triggerwoorden.
- **Agent-instructies, geen encyclopedie** - schrijf instructies die een agent kan volgen, geen achtergrondverhaal.
- **Implementatievoorbeelden** - voeg werkende codevoorbeelden toe in relevante talen.
- **Maximaal 500 regels** - grotere content hoort in een apart `reference.md` bestand.
- **Allowed-tools beperken** - geef alleen de tools die de skill nodig heeft.

## Stap 4: Lokaal testen

Test je plugin lokaal voordat je hem publiceert:

```bash
claude --plugin-dir ./mijn-plugin
```

Stel vragen die je skill zouden moeten activeren en controleer of de juiste skill wordt gekozen.

## Stap 5: Valideren

Valideer de plugin-structuur:

```bash
claude plugin validate ./mijn-plugin
```

## Stap 6: Publiceren

1. Push je repository naar GitHub (publiek)
2. Meld je plugin aan bij de marketplace - zie [plugin-toevoegen.md](plugin-toevoegen.md)

## Bestaande skills migreren

Heb je al `.claude/skills/` in je project? Je kunt ze **in-place** omzetten naar plugin-formaat zonder ze te verplaatsen:

1. Maak `.claude-plugin/plugin.json` aan met een `skills` veld dat naar `.claude/skills/` verwijst:
   ```json
   {
     "name": "mijn-plugin",
     "description": "Beschrijving",
     "version": "1.0.0",
     "skills": "./.claude/skills/"
   }
   ```
2. Zet elke `skill-naam.md` om naar een directory `skill-naam/SKILL.md`
3. Voeg YAML frontmatter toe aan elke SKILL.md (name, description, model, allowed-tools)
4. Test lokaal met `--plugin-dir`

Zo heb je **één locatie** voor skills die zowel lokaal in het project als via de marketplace werkt. Zie [zad-actions](https://github.com/RijksICTGilde/zad-actions) voor een werkend voorbeeld.

## Cursor compatibiliteit

`SKILL.md` bestanden met YAML frontmatter zijn cross-platform en werken in zowel Claude Code als Cursor. Om je plugin ook via Cursor beschikbaar te maken:

1. Voeg `.cursor-plugin/plugin.json` toe aan je repository (vergelijkbaar met `.claude-plugin/plugin.json`)
2. De marketplace genereert automatisch een Cursor-variant met `displayName`, `keywords` en `repository` velden

## Meer informatie

- [Claude Code plugin documentatie](https://code.claude.com/docs/en/plugins)
- [Plugin marketplace documentatie](https://code.claude.com/docs/en/plugin-marketplaces)
- [Plugin referentie](https://code.claude.com/docs/en/plugins-reference)
