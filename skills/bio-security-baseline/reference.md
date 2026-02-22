# BIO2 Overheidsmaatregelen — Volledig overzicht

Dit document bevat alle BIO2-overheidsmaatregelen (Deel 2) gegroepeerd per domein.
Maatregelen zonder nadere specificatie verwijzen naar Deel 1 (BIO2-Kader) en ISO/IEC 27002.

Bron: [BIO2 op GitHub](https://github.com/MinBZK/Baseline-Informatiebeveiliging-Overheid)

---

## 5.01 Beleid voor informatiebeveiliging

| ID | Maatregel |
|----|-----------|
| 5.01.01 | De organisatie stelt verantwoordelijkheden vast voor informatiebeveiliging, bescherming van operationele technologie (OT) en bedrijfscontinuiteitsbeheer (BCM). Het informatiebeveiligingsbeleid adresseert strategie, organisatiestructuur, verantwoordelijkheidstoewijzingen, betrouwbaarheidsnormen, reviewfrequentie en bevordering van beveiligingsbewustzijn. |
| 5.01.02 | Beleidsreview minimaal jaarlijks, afgestemd op management- en P&C-cyclus. |

## 5.02 Rollen en verantwoordelijkheden

| ID | Maatregel |
|----|-----------|
| 5.02.01 | Leiding definieert rollen en verantwoordelijkheden inclusief incidentafhandeling; lijnmanagers zijn eigenaar van risicomanagement voor hun assets. |
| 5.02.02 | Een Chief Information Security Officer (CISO) wordt aangesteld met onafhankelijke adviesbevoegdheid aan het bestuur. |

## 5.04 Bewustwording en training

| ID | Maatregel |
|----|-----------|
| 5.04.01 | Medewerkers en leiding krijgen regelmatige cybersecuritytraining over risicoherkenning en incidentresponsprocedures. |
| 5.04.02 | Gedragsregels voor apparatuurgebruik zijn gedocumenteerd voor extern personeel. |
| 5.04.03 | Alle medewerkers erkennen de gedragsregels. |

## 5.05 Contact met autoriteiten

| ID | Maatregel |
|----|-----------|
| 5.05.01 | Actueel register van functionarissen die formele beveiligingscontacten onderhouden met autoriteiten en toezichthouders. |

## 5.08 Risicobeoordeling

| ID | Maatregel |
|----|-----------|
| 5.08.01 | Nieuwe systemen of significante wijzigingen vereisen expliciete risicobeoordelingen met vastgestelde methodieken om risico's te identificeren en te beheersen. |

## 5.09 Assetbeheer

| ID | Maatregel |
|----|-----------|
| 5.09.01 | Assetinventarisatie omvat alle eigenschappen nodig voor beheer en onderhoud, inclusief remote devices, cloudomgevingen en aangesloten apparatuur buiten organisatorische controle. Volledigheid en actualiteit vereisen periodieke verificatie. |

## 5.12 Classificatie van informatie

| ID | Maatregel |
|----|-----------|
| 5.12.01 | Informatie wordt geclassificeerd via expliciete risicobeoordeling met vastgestelde impactclassificatiemethodieken. |

## 5.14 Internetgerichte systemen en standaarden

| ID | Maatregel |
|----|-----------|
| 5.14.01 | Internetgerichte systemen en e-mail voldoen aan verplichte standaarden van Forum Standaardisatie, geoptimaliseerd voor beveiliging zonder functionaliteit te compromitteren. |
| 5.14.02 | Publiek toegankelijke gevoelige data vereist Organization Validated (OV) certificaten; interne gevoelige data vereist minimaal OV of private PKIo-certificaten. |
| 5.14.03 | Elektronische handtekeningen voldoen aan AdES Baseline Profiles conform Forum Standaardisatie-richtlijnen. |
| 5.14.04 | Actueel register van alle internetgerichte systemen, webapplicaties, IP-adressen en API's. |
| 5.14.05 | Publieke websites geregistreerd in Register Internetdomeinen Overheid; minimaal halfjaarlijks bijwerken. |

## 5.15 Toegang tot vertrouwde zones

| ID | Maatregel |
|----|-----------|
| 5.15.01 | Toegang tot vertrouwde zones alleen toegestaan vanaf geauthenticeerde apparatuur of beveiligde shell-software. |

## 5.16 Gebruikersregistratie

| ID | Maatregel |
|----|-----------|
| 5.16.01 | Formele procedures voor gebruikersregistratie en -deregistratie. |
| 5.16.02 | Groepsaccounts verboden tenzij proceseigenaar goedkeurt en CISO instemt. |

## 5.17 Authenticatie

| ID | Maatregel |
|----|-----------|
| 5.17.01 | Multi-factor authenticatie (MFA) verplicht voor: primaire digitale werkplek-login, internettoegankelijke systemen en geprivilegieerde accounts. Twee vormen vereist: wachtwoordloze toegang (PIN + hardware token/passkey) of wachtwoord + tweede factor. Authenticatiegegevens volgen formele procedures met misbruikmonitoring. |
| 5.17.02 | Wachtwoordmanagers beschikbaar voor alle medewerkers. |
| 5.17.03 | Wachtwoordeisen automatisch afgedwongen. |

## 5.18 Geprivilegieerd toegangsbeheer

| ID | Maatregel |
|----|-----------|
| 5.18.01 | Aanmaak/wijziging van geprivilegieerde accounts wordt gemonitord; ongeautoriseerde wijzigingen zijn beveiligingsincidenten. |
| 5.18.02 | Alle toegangsrechten minimaal jaarlijks gereviewd; risicobeoordeling kan frequentere checks vereisen. |

## 5.19 Inkoop en aanbesteding

| ID | Maatregel |
|----|-----------|
| 5.19.01 | Informatiebeveiligingseisen (beschikbaarheid, integriteit, vertrouwelijkheid) op basis van expliciete risicobeoordeling in alle aanbestedingen die informatiesystemen betreffen. |

## 5.20 Leverancierscontracten

| ID | Maatregel |
|----|-----------|
| 5.20.01 | Beveiligingseisen expliciet opgenomen in contracten voor informatieverwerking. |
| 5.20.02 | Algemene voorwaarden van leveranciers waar mogelijk uitsluiten; onvermijdelijke voorwaarden vereisen risicobeoordeling met expliciete consequentiedocumentatie. |
| 5.20.03 | Contracten vereisen dat leveranciers compliance aantonen via onafhankelijke third-party onderzoeken; jaarlijkse hertoetsing verplicht. |
| 5.20.04 | Organisaties voeren onafhankelijke audits uit inclusief externe auditbepalingen; restrisico's worden beheerd via vastgestelde risicomethodieken. |
| 5.20.05 | Contracten vereisen transparantie van leveranciers over kwetsbaarheden en beveiligingsincidenten inclusief datalekken. |
| 5.20.06 | Contracten adresseren leveranciersafhankelijkheid via risicobeoordeling en expliciete exitstrategieen. |

## 5.21 Ketenbeheer

| ID | Maatregel |
|----|-----------|
| 5.21.01 | Leverancierscontracten vereisen compliance-borging door de gehele toeleveringsketen. |
| 5.21.02 | Voorafgaand aan contract: zichtbaarheid in toeleveringsketen met risicobeoordeling; beveiligingseisen vloeien door de keten tenzij aantoonbaar irrelevant. |
| 5.21.03 | Leveranciers melden ketenwijzigingen en gerelateerde risico's inclusief kwetsbaarheden en incidenten. |
| 5.21.04 | Compliance-eisen doorlopend geborgd in de keten. |

## 5.22 Leveranciersbeoordeling

| ID | Maatregel |
|----|-----------|
| 5.22.01 | Proceseigenaren beoordelen jaarlijks leverancierscompliance op basis van leveranciersbewijsvoering, identificeren risico's, implementeren mitigaties en accepteren restrisico's. |
| 5.22.02 | Actueel register van leveranciers en contracten. |

## 5.23 Cloudserviceproviders

| ID | Maatregel |
|----|-----------|
| 5.23.01 | CSP-beleid adresseert selectie, beoordeling, beheer en beeindiging van diensten. Beleid minimaal driejaarlijks reviewen; contracten specificeren beeindigingsgronden en risicobeoordeling bij grote wijzigingen. |

## 5.24 Incidentmanagement

| ID | Maatregel |
|----|-----------|
| 5.24.01 | Toegankelijk incidentmeldingssysteem voor alle interne en externe medewerkers. |
| 5.24.02 | Incidentprocedures documenteren meldtaken en verantwoordelijkheden. |
| 5.24.03 | Proceseigenaren verantwoordelijk voor incidentoplossing. |
| 5.24.04 | Proceseigenaren rapporteren maandelijks over incidentopvolging aan operationele leiding. |
| 5.24.05 | Incidentprocedures zijn gekoppeld aan crisismanagement. |
| 5.24.06 | Ketenbeveiliging opgenomen in organisatorische risicoanalyse met aandacht voor specifieke leverancierskwetsbaarheden, productkwaliteit en hun cyberbeveiligingspraktijken. |
| 5.24.07 | Procedures voor melding aan nationaal CSIRT binnen wettelijke termijnen, verwerking van CSIRT-meldingen en informeren van getroffen partijen binnen vereiste perioden. |

## 5.25 Incidentrapportage

| ID | Maatregel |
|----|-----------|
| 5.25.01 | Incidenten afgehandeld via incidentprocessen met toezichtrapportage per toepasselijke wetgeving (Cyberbeveiligingswet, Archiefwet, AVG). |

## 5.27 Leren van incidenten

| ID | Maatregel |
|----|-----------|
| 5.27.01 | Incidenten vereisen root-cause-analyse en verbeteridentificatie. |
| 5.27.02 | Bevindingen breed gedeeld met partners om herhaling te voorkomen. |

## 5.28 Bewaartermijn incidentregistratie

| ID | Maatregel |
|----|-----------|
| 5.28.01 | Incidentregistratie inclusief analyse- en oplossingsinformatie minimaal drie jaar bewaard. |

## 5.30 Continuiteit

| ID | Maatregel |
|----|-----------|
| 5.30.01 | Proceseigenaren testen jaarlijks continuiteitsplannen op functionaliteit, volledigheid en actualiteit. |
| 5.30.02 | Kritieke systemen geidentificeerd in assetinventarisatie op basis van risicobeoordeling; review minimaal driejaarlijks. |

## 5.33 Bewaartermijnen

| ID | Maatregel |
|----|-----------|
| 5.33.01 | Bewaartermijnen voor alle informatiesystemen gedocumenteerd per bedrijfsdoelstellingen en toepasselijke wet (Archiefwet, privacywetgeving); termijnen praktisch geimplementeerd met periodieke tests. |

## 5.35 Managementsystemen

| ID | Maatregel |
|----|-----------|
| 5.35.01 | Werkend Information Security Management System (ISMS) conform NEN-EN-ISO/IEC 27001. |
| 5.35.02 | Jaarlijks auditplan dat bepaalt welke systemen welke beveiligingsaudittypes ontvangen. |

## 5.36 Rapportage

| ID | Maatregel |
|----|-----------|
| 5.36.01 | P&C- en PDCA-cycli bevatten jaarlijkse beveiligingsrapportage gecoordineerd door CISO, resulterend in jaarlijkse In Control Verklaring (ICV) over organisatorische beveiliging. |

## 6.01 Screening

| ID | Maatregel |
|----|-----------|
| 6.01.01 | Screeningbeleid vastgesteld; Verklaring Omtrent het Gedrag (VOG) kan vereist zijn op basis van risicobeoordeling bij aanname en functiewijzigingen. |

## 6.02 Arbeidsvoorwaarden

| ID | Maatregel |
|----|-----------|
| 6.02.01 | Alle medewerkers worden bij aanname of functiewijziging geinformeerd over beveiligingsverantwoordelijkheden; toepasselijke regels en instructies zijn gemakkelijk toegankelijk. |

## 6.03 Bewustwording

| ID | Maatregel |
|----|-----------|
| 6.03.01 | Alle medewerkers en leiding delen verantwoordelijkheid voor bescherming van bedrijfsinformatie en kennen toepasselijke beveiligingsregels. |
| 6.03.02 | Alle medewerkers en contractanten voltooien verplichte informatiebeveiligings-bewustwordingstraining binnen drie maanden na indiensttreding. |
| 6.03.03 | Management benadrukt belang van beveiligingstraining en moedigt regelmatige deelname actief aan. |

## 6.08 Incidentmelding personeel

| ID | Maatregel |
|----|-----------|
| 6.08.01 | Alle interne en externe medewerkers erkennen incidentmeldingsprocedures. |

## 7.01 Fysieke beveiliging

| ID | Maatregel |
|----|-----------|
| 7.01.01 | Beveiligde zones gebruiken standaarden voor implementatie. |
| 7.01.02 | Kritieke informatie/systemen zijn nooit toegankelijk via een enkele beveiligde zone. |

## 7.02 Beveiligingswaarschuwingen

| ID | Maatregel |
|----|-----------|
| 7.02.01 | Beveiligingswaarschuwingen over concrete risico's verspreid aan relevante domeinmedewerkers conform onderlinge afspraken. |

## 7.07 Toegangstokens

| ID | Maatregel |
|----|-----------|
| 7.07.01 | Chipkaarttokens activeren automatisch toegangsblokkering bij verwijdering. |

## 7.10 Media en dataverwijdering

| ID | Maatregel |
|----|-----------|
| 7.10.01 | Herbruikbare verwijderbare media die de organisatie verlaten: bedrijfsgevoelige inhoud onomkeerbaar verwijderd conform verwijderingsinstructies. |
| 7.10.02 | Dataverwijdering is onomkeerbaar of ontoegankelijk met verificatie en documentatie. Producten met positieve NBV-toelating hebben voorkeur. |
| 7.10.03 | Koeriers die gerubriceerde informatie transporteren voldoen aan vastgestelde betrouwbaarheidsnormen. |

## 8.01 Mobiele apparaten

| ID | Maatregel |
|----|-----------|
| 8.01.01 | Mobiele apparaten implementeren zero footprint (of near-zero) voor bedrijfsinformatie. Bij onhaalbaarheid: minimaal toegangsbescherming via encryptie. Remote wipe verplicht. |
| 8.01.02 | Mobiel gebruik omvat bewustwordingstraining, patch management en hardening, MDM/MAM-oplossingen, en ondertekende gebruikersovereenkomsten. Periodieke compliance-test verplicht. |

## 8.02 Geprivilegieerde rechten

| ID | Maatregel |
|----|-----------|
| 8.02.01 | Speciale privileges minimaal driemaandelijks gereviewd in opzet, bestaan en werking. |

## 8.03 Informatie-isolatie

| ID | Maatregel |
|----|-----------|
| 8.03.01 | Maatregelen waarborgen fysieke/logische isolatie van bijzonder gevoelige informatie. |
| 8.03.02 | Gebruikers hebben alleen toegang tot informatie die noodzakelijk is voor hun taken. |

## 8.05 Leverancierstoegang

| ID | Maatregel |
|----|-----------|
| 8.05.01 | Externe leveranciersnetwerktoegang vereist voorafgaande risicobeoordeling die voorwaarden en duur bepaalt; documentatie van toegangsrechten verplicht. |

## 8.07 Malwarebescherming

| ID | Maatregel |
|----|-----------|
| 8.07.01 | Bestandsdownloads worden beheerst en beperkt op basis van risico en gebruiksbehoefte; antimalware beoordeelt alle downloads. |
| 8.07.02 | Gebruikers geinformeerd over surfrisico's en gevaren van onbekende links. |
| 8.07.03 | Antimalwaresoftware actueel gehouden met periodieke updates. |
| 8.07.04 | Malwarescanning dekt alle omgevingen, alle gedownloade content voor uitvoering/opslag, en alle via netwerk/media ontvangen bestanden voor gebruik/opslag. |

## 8.08 Kwetsbaarhedenbeheer en patching

| ID | Maatregel |
|----|-----------|
| 8.08.01 | Bij hoge misbruikwaarschijnlijkheid en hoge verwachte schade: mitigerende maatregelen onmiddellijk binnen maximaal een week implementeren. |
| 8.08.02 | Risicogebaseerde bepaling van mitigatiebenadering. |
| 8.08.03 | Interim mitigerende maatregelen wanneer installatie binnen een week onmogelijk. |
| 8.08.04 | Systemen bij voorkeur jaarlijkse technische controle via geautomatiseerde kwetsbaarheidsanalyse, penetratietest of red-team-test; internetgerichte systemen bij voorkeur continu getest. |
| 8.08.05 | Internetgerichte systemen vereisen verplichte penetratietest bij elke release/major update; high-risk bevindingen blokkeren productiedeployment; minimaal jaarlijks uitgebreide test. |
| 8.08.06 | Coordinated Vulnerability Disclosure (CVD) procedure conform NCSC-richtlijnen of NEN-EN-ISO/IEC 29147:2020; CVD-informatie geintegreerd in incidentrapportage. |

## 8.13 Backup en herstel

| ID | Maatregel |
|----|-----------|
| 8.13.01 | Backupbeleid definieert bewaar- en beschermingseisen met specifieke ransomwarebescherming en integriteitsmaatregelen. |
| 8.13.02 | Expliciete risicobeoordeling bepaalt maximaal acceptabel dataverlies en hersteltijd. |
| 8.13.03 | Backupopslag op aparte locatie zodat incidenten op een locatie de andere niet kunnen beschadigen. |
| 8.13.04 | Herstelprocedures minimaal jaarlijks of na grote wijzigingen getest. |

## 8.15 Logging

| ID | Maatregel |
|----|-----------|
| 8.15.01 | Logregels bevatten minimaal: actie, object, resultaat, herkomst, actor-identificatie en tijdstempel. |
| 8.15.02 | Logregels bevatten nooit beveiligingscompromitterende gegevens. |
| 8.15.03 | Overzicht van gegenereerde logbestanden verplicht. |
| 8.15.04 | Logretentie risicogebaseerd rekening houdend met langdurige aanwezigheidsscenario's van aanvallers. |
| 8.15.05 | Ongeautoriseerde logwijziging/-verwijdering/-pogingen worden onmiddellijk gemeld als beveiligingsincident. |
| 8.15.06 | Risicogebaseerde periodieke verificatie van logintegriteit door onafhankelijk personeel. |

## 8.16 Monitoring

| ID | Maatregel |
|----|-----------|
| 8.16.01 | Nieuwe dreigingen/aanvallen ontdekt via monitoring worden gedeeld met aangewezen CERT binnen wettelijke kaders. |
| 8.16.02 | SIEM/SOC-monitoringprocessen hebben duidelijke incidentmeldingsregels. |
| 8.16.03 | Gemonitorde informatieomgeving met detectie-/responscapaciteiten voor aanvalsdetectie en tijdige afwijkingsbehandeling. |
| 8.16.04 | Actieve netwerkcomponenten bevatten logging en monitoring voor anomaliedetectie en -respons. |

## 8.18 Systeemhulpmiddelen

| ID | Maatregel |
|----|-----------|
| 8.18.01 | Alleen geautoriseerd personeel heeft toegang tot systeemhulpmiddelen wanneer strikt noodzakelijk. |
| 8.18.02 | Gebruik van systeemhulpmiddelen gelogd met zes maanden onderzoekbeschikbaarheid. |

## 8.19 Software-installatie

| ID | Maatregel |
|----|-----------|
| 8.19.01 | Risico van ongeautoriseerde software-installatie door gebruikers wordt beheerst. |

## 8.20 Netwerkcomponenten

| ID | Maatregel |
|----|-----------|
| 8.20.01 | Netwerkcomponenten voldoen aan minimaal vertrouwensniveau van hun netwerk. |
| 8.20.02 | Beheertoegang tot netwerkcomponenten gescheiden (waar mogelijk en risicopassend) van gebruikersnetwerken. |

## 8.21 Netwerkbeveiliging

| ID | Maatregel |
|----|-----------|
| 8.21.01 | Aansluitpunten met externe/onvertrouwde zones bevatten maatregelen voor detectie/mitigatie van aanvallen die informatiebeschikbaarheid beinvloeden (DDoS). |
| 8.21.02 | Dataverkeer van/naar vertrouwde omgevingen gemonitord/geanalyseerd op verdachte activiteit via detectiecapaciteiten. |
| 8.21.03 | Nieuw ontdekte dreigingen gedeeld binnen de overheid conform wettelijke kaders. |
| 8.21.04 | Draadloos en extern datatransport versleuteld exclusief noodzakelijke transportmetadata. Versleutelingsbenadering risicogebaseerd rekening houdend met vereiste beschermingsduur/-niveau; voorkeur voor AIVD-goedgekeurde versleuteling of door CISO goedgekeurde alternatieven. |

## 8.22 Netwerksegmentatie

| ID | Maatregel |
|----|-----------|
| 8.22.01 | Alle gesegmenteerde groepen hebben gedefinieerde beveiligingsniveaus. |

## 8.24 Cryptografie

| ID | Maatregel |
|----|-----------|
| 8.24.01 | Cryptografiebeleid adresseert inzetcriteria, verantwoordelijkheidstoewijzingen, sleutelbeheer, gebruiksregistratie, Forum Standaardisatie-standaarden, beschermingsniveaubepaling en interorganisatorische coordinatie. |
| 8.24.02 | Cryptografische toepassingen opgenomen in assetinventarisatie met inzet-, verantwoordelijkheids- en onderhoudsinformatie. |
| 8.24.03 | Cryptografische toepassingen voldoen aan Forum Standaardisatie-standaarden. |
| 8.24.04 | Cryptografische sterkte gebaseerd op actuele NCSC- en AIVD Unit Weerbaarheid-richtlijnen. |
| 8.24.05 | Contractuele afspraken voor backup-certificaten van alternatieve leveranciers wanneer risicobeoordeling dit aangeeft voor bedrijfscontinuiteitsparaatheid. |

## 8.27 Architectuurprincipes

| ID | Maatregel |
|----|-----------|
| 8.27.01 | Architectuurprincipes inclusief "security by design" en "security by default" vastgesteld, gedocumenteerd, onderhouden en toegepast op alle ontwikkelactiviteiten. |

## 8.29 Systeemacceptatie

| ID | Maatregel |
|----|-----------|
| 8.29.01 | Systeemacceptatietests gebruiken gestructureerde methodieken, bij voorkeur geautomatiseerd, met gedocumenteerde resultaten. |

## 8.30 Uitbestede ontwikkeling

| ID | Maatregel |
|----|-----------|
| 8.30.01 | Interne ontwikkelbeveiligingsmaatregelen gelden volledig voor uitbestede ontwikkeling plus aanvullende outsourcing-specifieke maatregelen. |

## 8.31 Testen

| ID | Maatregel |
|----|-----------|
| 8.31.01 | Testen op productieomgeving verboden tenzij met goedkeuring van proceseigenaar. |
| 8.31.02 | Significante productiewijzigingen vereisen voorafgaande test tenzij met goedkeuring van proceseigenaar. |

## 8.32 Wijzigingsbeheer

| ID | Maatregel |
|----|-----------|
| 8.32.01 | Wijzigingsbeheer omvat wijzigingsadministratie met testresultaten, risicobeoordeling met rollback-plannen en goedkeuringsprocedures. |
| 8.32.02 | Wijzigingsbeheer volgt algemeen geaccepteerde beheerframeworks. |

---

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

### security.txt conform BIO2 (voorbeeld)

```text
# https://www.example.overheid.nl/.well-known/security.txt
# Conform BIO2 8.08.06 (CVD) en internet.nl-vereisten

Contact: mailto:security@example.overheid.nl
Expires: 2027-01-01T00:00:00.000Z
Encryption: https://www.example.overheid.nl/pgp-key.txt
Preferred-Languages: nl, en
Canonical: https://www.example.overheid.nl/.well-known/security.txt
Policy: https://www.example.overheid.nl/responsible-disclosure
```

---

## Relatie met andere standaarden

| Standaard | Relatie met BIO2 |
|-----------|-----------------|
| NEN-EN-ISO/IEC 27001:2023 | BIO2 vereist werkend ISMS conform 27001 (5.35.01); Deel 1 volgt 27001-structuur |
| NEN-EN-ISO/IEC 27002:2022 | BIO2-overheidsmaatregelen (Deel 2) zijn aanvullend op 27002-controls |
| Cyberbeveiligingswet (Cbw) | BIO2 is het sectorspecifieke implementatiekader (zorgplichtinvulling) voor de Cbw/NIS2 bij de overheid |
| Forum Standaardisatie | Verplichte standaarden voor internetgerichte systemen (5.14.01); ~40+ standaarden op "pas toe of leg uit"-lijst |
| NCSC TLS-richtlijnen 2025-05 | Referentie voor TLS-configuratie; TLS 1.3=Goed, 1.2=Voldoende, 1.0/1.1=Onvoldoende |
| NCSC Webapplicatie-richtlijnen | Wettelijk verplicht voor alle internettoegankelijke overheidswebsites |
| AVG / GDPR | Incidentmelding (meldplicht datalekken), bewaartermijnen en privacy by design sluiten aan bij AVG-vereisten |
| Wet digitale overheid (Wdo) | Wettelijke basis voor verplicht HTTPS/HSTS (sinds 1 juli 2023) en DigiToegankelijk |
| DigiToegankelijk (WCAG 2.1) | Wettelijk verplicht voor alle overheidswebsites en -apps; apart van BIO2 maar onderdeel van dezelfde compliance-vereisten |
| NLGov REST API Design Rules | Verplicht bij aanbieden van REST-API's; Transport Security-module referereert aan NCSC TLS-richtlijnen |
| OAuth 2.0 NL GOV | Verplicht voor API-autorisatie; complementair aan BIO2 toegangsbeheer (5.15–5.18) |
| OpenID.NLGov + SAML | Verplichte authenticatiestandaarden; aanvullend op BIO2 MFA-vereiste (5.17.01) |
| ENSIA | Jaarlijks auditframework voor aantonen BIO-compliance en andere beveiligingsvereisten |
| NORA | Referentiearchitectuur met beveiligingsprincipes die aansluiten bij BIO2 security by design (8.27.01) |
| Cyber Resilience Act (CRA) | EU-verordening voor producten met digitale elementen; vereist SBOM, kwetsbaarhedenbeheer en security-by-design. Complementair aan BIO2 voor software die de overheid inkoopt of ontwikkelt |
| AI Act | EU-verordening voor AI-systemen; risicogebaseerde eisen inclusief conformiteitsbeoordeling en menselijk toezicht voor hoog-risico AI bij de overheid |
| eIDAS 2.0 | European Digital Identity Wallet; overheden moeten EUDI Wallet accepteren. Aanvullend op BIO2 authenticatievereisten (5.17) |

---

## Uitgebreide bronnenlijst

### BIO2 en beveiliging
- [BIO2 op GitHub](https://github.com/MinBZK/Baseline-Informatiebeveiliging-Overheid)
- [BIO2 v1.2 PDF](https://www.bio-overheid.nl/media/cs5ctudu/20250924-baseline-informatiebeveiliging-overheid-2-bio2-v12-deff.pdf)
- [bio-overheid.nl](https://www.bio-overheid.nl/category/producten/bio)
- [CIP — Centrum Informatiebeveiliging en Privacybescherming](https://www.cip-overheid.nl)
- [Digitale Overheid — BIO en ENSIA](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/)

### Wet- en regelgeving
- [Digitale Overheid — Cyberbeveiligingswet](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cyberbeveiligingswet/)
- [NCTV — Cyberbeveiligingswet](https://www.nctv.nl/onderwerpen/c/cyberbeveiligingswet)
- [DigiToegankelijk.nl — Wat is verplicht](https://www.digitoegankelijk.nl/wetgeving/wat-is-verplicht)
- [EU Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

### Forum Standaardisatie
- [Verplichte standaarden](https://www.forumstandaardisatie.nl/open-standaarden/verplicht)
- [Alle open standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
- [Streefbeeldafspraken](https://www.forumstandaardisatie.nl/onderwerpen/veilig-internet/streefbeeldafspraken)
- [Monitor Open Standaarden 2025](https://www.forumstandaardisatie.nl/monitor-open-standaarden-2025-hoofdlijnen-en-conclusies)

### NCSC-richtlijnen
- [NCSC — TLS-richtlijnen 2025-05](https://www.ncsc.nl/documenten/publicaties/2025/juni/01/ict-beveiligingsrichtlijnen-voor-transport-layer-security-2025-05)
- [NCSC — Webapplicatie-richtlijnen](https://www.ncsc.nl/onderwerpen/ict-beveiligingsrichtlijnen-voor-webapplicaties)
- [NCSC — Basisprincipes](https://www.ncsc.nl/basisprincipes)
- [NCSC — Cybersecuritybeeld 2025](https://www.ncsc.nl/nieuws/cybersecuritybeeld-2025-dreigingen-divers-en-onvoorspelbaar-digitale-basishygiene-op-orde-blijft)

### API- en authenticatiestandaarden
- [NLGov REST API Design Rules](https://logius-standaarden.github.io/API-Design-Rules/)
- [NL GOV OAuth 2.0](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20)
- [Authenticatie-standaarden (OpenID.NLGov + SAML)](https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden)
- [NL GOV Profile for CloudEvents](https://logius-standaarden.github.io/NL-GOV-profile-for-CloudEvents/)
- [Digikoppeling Architectuur](https://logius-standaarden.github.io/Digikoppeling-Architectuur/)
- [Developer.overheid.nl](https://developer.overheid.nl)

### Audit en compliance
- [ENSIA — Digitale Overheid](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/ensia/)
- [VNG — ENSIA](https://vng.nl/projecten/ensia)
- [DigiD Normenkader 3.0](https://www.logius.nl/onze-dienstverlening/toegang/digid/ict-beveiligingsassessments-digid/documentatie/norm-ict-beveiligingsassessments-digid)
- [Internet.nl — Compliancetest](https://internet.nl)

### Architectuur
- [NORA Online](https://www.noraonline.nl)
- [Digitale Overheid — NORA](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/nora/)
- [Digitale Overheid — NORA Familie](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/nora/nora-familie/)
