---
name: bio-security-baseline
description: >-
  Gebruik deze skill wanneer de gebruiker vraagt over 'BIO', 'BIO2',
  'Baseline Informatiebeveiliging Overheid', 'informatiebeveiliging overheid',
  'overheidsbeveiliging', 'government security baseline', 'information security',
  'cybersecurity overheid', 'NIS2', 'ISO 27001 overheid', 'ISO 27002 overheid',
  'beveiligingsmaatregelen overheid', 'ISMS overheid', 'security controls',
  'overheidsmaatregelen beveiliging', 'BIO-compliance', 'BIO toetsing',
  'security audit overheid', 'penetratietest overheid', 'logging overheid',
  'toegangsbeheer overheid', 'cryptografie overheid', 'kwetsbaarhedenbeheer overheid',
  'patch management overheid', 'security by design overheid', 'MFA overheid',
  of wanneer de gebruiker een systeem wil laten voldoen aan de BIO2-normen.
model: sonnet
allowed-tools:
  - WebFetch(*)
  - Bash(gh api *)
  - Bash(gh search *)
---

# Baseline Informatiebeveiliging Overheid 2 (BIO2)

**Agent-instructie:** Deze skill helpt bij het implementeren van informatiebeveiliging conform de BIO2. Gebruik deze skill om code, architectuur en processen te toetsen aan de verplichte overheidsmaatregelen. De BIO2 is de verplichte beveiligingsbaseline voor alle Nederlandse overheidsorganisaties.

De BIO2 (versie 1.2, september 2025) is opgebouwd uit drie delen:

- **Deel 1 — BIO2-Kader**: context, toepassingsgebied, risicomanagement
- **Deel 2 — Overheidsmaatregelen**: verplichte maatregelen bovenop ISO/IEC 27001/27002
- **Deel 3 — Handreiking**: praktische implementatieondersteuning

Alle overheidsorganisaties moeten een werkend Information Security Management System (ISMS) conform NEN-EN-ISO/IEC 27001 inrichten en de BIO2-overheidsmaatregelen implementeren.

Bron: [GitHub — MinBZK/Baseline-Informatiebeveiliging-Overheid](https://github.com/MinBZK/Baseline-Informatiebeveiliging-Overheid)

## Wanneer deze skill gebruiken

- Bij het ontwerpen of reviewen van systemen voor de Nederlandse overheid
- Bij het toetsen van code of architectuur aan BIO2-eisen
- Bij het opstellen van beveiligingsbeleid of risicobeoordeling
- Bij vragen over specifieke BIO2-maatregelen en hun implementatie
- Bij het voorbereiden van audits of compliance-checks

## Kerndomeinen en maatregelen

Zie [reference.md](reference.md) voor de volledige lijst van alle BIO2-overheidsmaatregelen.

### 1. Governance & beleid (5.01–5.05)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 5.01.01 | Informatiebeveiligingsbeleid met strategie, organisatie, verantwoordelijkheden, betrouwbaarheidsniveaus, reviewfrequentie en bewustwordingsbevordering |
| 5.01.02 | Jaarlijkse beleidsreview afgestemd op P&C-cyclus |
| 5.02.01 | Rollen en verantwoordelijkheden inclusief incidentafhandeling; lijnmanagers eigenaar van risicomanagement |
| 5.02.02 | CISO aanstellen met onafhankelijke adviesbevoegdheid aan het bestuur |
| 5.04.01 | Regelmatige cybersecuritytraining voor alle medewerkers en leiding |
| 5.05.01 | Actueel register van functionarissen die contacten onderhouden met autoriteiten |

### 2. Risicomanagement & systeemontwerp (5.08–5.12)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 5.08.01 | Expliciete risicobeoordeling bij nieuwe systemen of significante wijzigingen |
| 5.09.01 | Assetinventarisatie inclusief remote devices, cloudomgevingen en OT-apparatuur |
| 5.12.01 | Informatieclassificatie op basis van risicobeoordeling met vastgestelde impactmethodiek |

### 3. Internetgerichte systemen & standaarden (5.14)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 5.14.01 | Internetgerichte systemen en e-mail voldoen aan verplichte standaarden Forum Standaardisatie |
| 5.14.02 | OV-certificaten voor publiek toegankelijke gevoelige data; OV of privaat PKIo intern |
| 5.14.03 | Elektronische handtekeningen conform AdES Baseline Profiles |
| 5.14.04 | Actueel register van alle internetgerichte systemen, webapplicaties, IP-adressen en API's |
| 5.14.05 | Publieke websites geregistreerd in Register Internetdomeinen Overheid (halfjaarlijks bijwerken) |

### 4. Toegangsbeheer (5.15–5.18)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 5.15.01 | Toegang tot vertrouwde zones alleen vanaf geauthenticeerde apparatuur of beveiligde shell-software |
| 5.16.01 | Formele gebruikersregistratie en -deregistratie |
| 5.16.02 | Groepsaccounts verboden tenzij proceseigenaar goedkeurt en CISO instemt |
| 5.17.01 | **MFA verplicht** voor primaire digitale werkplek, internettoegankelijke systemen en geprivilegieerde accounts |
| 5.17.02 | Wachtwoordmanager beschikbaar voor alle medewerkers |
| 5.17.03 | Wachtwoordeisen automatisch afgedwongen |
| 5.18.01 | Aanmaak/wijziging geprivilegieerde accounts monitoren; ongeautoriseerde wijzigingen zijn beveiligingsincidenten |
| 5.18.02 | Jaarlijkse review van alle toegangsrechten |

### 5. Inkoop & leveranciersbeheer (5.19–5.23)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 5.19.01 | Beveiligingseisen (BIV) op basis van risicobeoordeling in alle aanbestedingen |
| 5.20.01 | Beveiligingseisen expliciet opgenomen in contracten |
| 5.20.03 | Leveranciers tonen compliance via onafhankelijke third-party audits; jaarlijkse hertoetsing |
| 5.20.05 | Leveranciers transparant over kwetsbaarheden en beveiligingsincidenten |
| 5.20.06 | Risicobeoordeling leveranciersafhankelijkheid met expliciete exitstrategie |
| 5.21.01 | Compliance-borging door gehele toeleveringsketen |
| 5.23.01 | Cloud Service Provider-beleid voor selectie, beoordeling, beheer en beeindiging |

### 6. Incidentmanagement (5.24–5.28)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 5.24.01 | Laagdrempelig incidentmeldingssysteem voor alle medewerkers |
| 5.24.05 | Incidentprocedures gekoppeld aan crisismanagement |
| 5.24.07 | Melding aan nationaal CSIRT binnen wettelijke termijnen |
| 5.25.01 | Incidenten afgehandeld via incidentproces met rapportage conform wet (Cyberbeveiligingswet, Archiefwet, AVG) |
| 5.27.01 | Root-cause-analyse en verbeteridentificatie bij incidenten |
| 5.28.01 | Incidentregistratie inclusief analyse minimaal 3 jaar bewaren |

### 7. Continuiteit & veerkracht (5.30, 5.33)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 5.30.01 | Jaarlijkse test van continuiteitsplannen |
| 5.30.02 | Kritieke systemen geidentificeerd in assetinventarisatie; driejaarlijkse review |
| 5.33.01 | Bewaartermijnen gedocumenteerd per wet (Archiefwet, AVG); periodiek getest |

### 8. Ontwikkeling & testen (8.27–8.32)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 8.27.01 | **Security by design** en **security by default** als architectuurprincipes bij alle ontwikkelactiviteiten |
| 8.29.01 | Gestructureerde systeemacceptatietests, bij voorkeur geautomatiseerd, met gedocumenteerde resultaten |
| 8.30.01 | Uitbestede ontwikkeling: interne beveiligingsmaatregelen plus aanvullende outsourcing-specifieke maatregelen |
| 8.31.01 | Testen op productieomgeving verboden tenzij proceseigenaar goedkeurt |
| 8.31.02 | Significante productiewijzigingen vereisen voorafgaande test |
| 8.32.01 | Wijzigingsbeheer met testresultaten, risicobeoordeling, rollback-plannen en goedkeuringsprocedures |

### 9. Kwetsbaarhedenbeheer & patching (8.08)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 8.08.01 | Bij hoge misbruikkans en hoge schade: mitigatie **binnen een week** |
| 8.08.02 | Risicogebaseerde bepaling van mitigatiebenadering |
| 8.08.04 | Jaarlijkse technische controle via geautomatiseerde kwetsbaarheidsanalyse, pentest of red-team-test |
| 8.08.05 | **Verplichte pentest** bij elke release van internetgerichte systemen; high-risk bevindingen blokkeren productie |
| 8.08.06 | Coordinated Vulnerability Disclosure (CVD) procedure conform NCSC-richtlijnen |

### 10. Logging & monitoring (8.15–8.16)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 8.15.01 | Logregels bevatten minimaal: actie, object, resultaat, herkomst, actor-identificatie, tijdstempel |
| 8.15.02 | Logregels bevatten **nooit** beveiligingsgevoelige gegevens |
| 8.15.04 | Risicogebaseerde logretentie rekening houdend met langdurige aanwezigheid van aanvallers |
| 8.15.05 | Ongeautoriseerde logwijziging/verwijdering direct melden als beveiligingsincident |
| 8.16.01 | Nieuwe dreigingen delen met aangewezen CERT |
| 8.16.03 | Gemonitorde informatieomgeving met detectie- en responscapaciteiten |

### 11. Cryptografie (8.24)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 8.24.01 | Cryptografiebeleid: inzetcriteria, verantwoordelijkheden, sleutelbeheer, Forum Standaardisatie-standaarden |
| 8.24.03 | Cryptografische toepassingen conform Forum Standaardisatie-standaarden |
| 8.24.04 | Cryptografische sterkte op basis van actuele NCSC- en AIVD-richtlijnen |

### 12. Netwerkbeveiliging (8.20–8.22)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 8.20.01 | Netwerkcomponenten voldoen aan minimaal vertrouwensniveau van hun netwerk |
| 8.21.01 | DDoS-mitigatie op koppelingen met externe/onvertrouwde zones |
| 8.21.02 | Dataverkeer van/naar vertrouwde omgevingen gemonitord op verdachte activiteit |
| 8.21.04 | Draadloos en extern datatransport versleuteld; voorkeur AIVD-goedgekeurde encryptie |
| 8.22.01 | Alle gesegmenteerde groepen hebben gedefinieerde beveiligingsniveaus |

### 13. Backup & herstel (8.13)

| Maatregel | Kernvereiste |
|-----------|-------------|
| 8.13.01 | Backupbeleid met ransomwarebescherming en integriteitsmaatregelen |
| 8.13.02 | Maximaal acceptabel dataverlies en hersteltijd bepaald via risicobeoordeling |
| 8.13.03 | Backupopslag op aparte locatie |
| 8.13.04 | Herstelprocedures jaarlijks getest |

## Implementatie-checklist voor ontwikkelaars

Bij het bouwen van systemen voor de overheid, controleer minimaal:

- [ ] **Authenticatie**: MFA geimplementeerd voor alle internettoegankelijke systemen (5.17.01)
- [ ] **Wachtwoorden**: automatisch afgedwongen wachtwoordeisen (5.17.03)
- [ ] **Geprivilegieerde accounts**: aanmaak/wijziging gemonitord en gelogd (5.18.01)
- [ ] **TLS/certificaten**: OV-certificaten voor publieke gevoelige data (5.14.02)
- [ ] **Forum Standaardisatie**: internetgerichte systemen voldoen aan verplichte standaarden (5.14.01)
- [ ] **Security by design**: beveiligingsprincipes toegepast vanaf ontwerp (8.27.01)
- [ ] **Logging**: minimaal actie, object, resultaat, herkomst, actor, tijdstempel (8.15.01)
- [ ] **Geen gevoelige data in logs**: wachtwoorden, tokens, BSN nooit loggen (8.15.02)
- [ ] **Kwetsbaarheden**: patches binnen een week bij hoog risico (8.08.01)
- [ ] **Pentesting**: verplicht bij elke release van internetgerichte systemen (8.08.05)
- [ ] **CVD**: Coordinated Vulnerability Disclosure procedure ingericht (8.08.06)
- [ ] **Encryptie**: conform NCSC/AIVD-richtlijnen en Forum Standaardisatie (8.24.03–04)
- [ ] **Backup**: ransomware-bestendige backups op aparte locatie (8.13.01–03)
- [ ] **Wijzigingsbeheer**: testresultaten, risicobeoordeling, rollback-plan (8.32.01)
- [ ] **Acceptatietests**: gestructureerd en bij voorkeur geautomatiseerd (8.29.01)
- [ ] **Netwerksegmentatie**: beveiligingsniveaus per segment gedefinieerd (8.22.01)
- [ ] **DDoS-mitigatie**: bescherming op externe koppelingen (8.21.01)
- [ ] **Incidentmelding**: meldprocedure en koppeling met nationaal CSIRT (5.24.07)

## Codevoorbeelden

### Logging conform BIO2 (Python)

```python
import logging
import json
from datetime import datetime, timezone

class BIO2AuditLogger:
    """Logger die voldoet aan BIO2 maatregel 8.15.01 (minimale logvelden)
    en 8.15.02 (geen beveiligingsgevoelige data)."""

    SENSITIVE_FIELDS = {"password", "wachtwoord", "token", "secret",
                        "bsn", "api_key", "authorization", "cookie",
                        "session_id", "credit_card"}

    def __init__(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)

    def _sanitize(self, data: dict) -> dict:
        """Verwijder beveiligingsgevoelige velden (8.15.02)."""
        return {k: "***REDACTED***" if k.lower() in self.SENSITIVE_FIELDS
                else v for k, v in data.items()}

    def audit_log(self, action: str, obj: str, result: str,
                  origin: str, actor: str, details: dict | None = None):
        """Schrijf auditlogregel conform BIO2 8.15.01.

        Verplichte velden: actie, object, resultaat, herkomst,
        actor-identificatie, tijdstempel.
        """
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "object": obj,
            "result": result,
            "origin": origin,
            "actor": actor,
        }
        if details:
            entry["details"] = self._sanitize(details)
        self.logger.info(json.dumps(entry))

# Gebruik:
audit = BIO2AuditLogger("myapp.audit")
audit.audit_log(
    action="login",
    obj="user_session",
    result="success",
    origin="192.168.1.100",
    actor="user@example.nl",
)
```

### Security headers conform BIO2 (Python/FastAPI)

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def bio2_security_headers(request: Request, call_next):
    """Voeg beveiligingsheaders toe conform BIO2 5.14.01
    en Forum Standaardisatie-eisen."""
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    response.headers["Cache-Control"] = "no-store"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    return response
```

## Relatie met andere standaarden

| Standaard | Relatie met BIO2 |
|-----------|-----------------|
| NEN-EN-ISO/IEC 27001 | BIO2 vereist werkend ISMS conform 27001 (5.35.01) |
| NEN-EN-ISO/IEC 27002 | BIO2-maatregelen zijn aanvullend op 27002-controls |
| NIS2 / Cyberbeveiligingswet | BIO2 is het implementatiekader voor NIS2-verplichtingen bij de overheid |
| Forum Standaardisatie | Verplichte standaarden voor internetgerichte systemen (5.14.01) |
| NCSC-richtlijnen | Referentie voor cryptografische sterkte en kwetsbaarhedenbeheer |
| AVG / GDPR | Incidentmelding en bewaartermijnen sluiten aan bij AVG-vereisten |

## Meer informatie

- [BIO2 op GitHub](https://github.com/MinBZK/Baseline-Informatiebeveiliging-Overheid)
- [CIP — Centrum Informatiebeveiliging en Privacybescherming](https://www.cip-overheid.nl)
- [Forum Standaardisatie — Verplichte standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
- [NCSC — Beveiligingsrichtlijnen](https://www.ncsc.nl)
