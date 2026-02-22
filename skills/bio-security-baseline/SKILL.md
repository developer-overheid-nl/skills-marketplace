---
name: bio-security-baseline
description: >-
  Gebruik deze skill wanneer de gebruiker vraagt over 'BIO', 'BIO2',
  'Baseline Informatiebeveiliging Overheid', 'informatiebeveiliging overheid',
  'overheidsbeveiliging', 'government security baseline', 'information security',
  'cybersecurity overheid', 'NIS2', 'Cyberbeveiligingswet', 'ISO 27001 overheid',
  'ISO 27002 overheid', 'beveiligingsmaatregelen overheid', 'ISMS overheid',
  'security controls', 'overheidsmaatregelen beveiliging', 'BIO-compliance',
  'BIO toetsing', 'security audit overheid', 'penetratietest overheid',
  'logging overheid', 'toegangsbeheer overheid', 'cryptografie overheid',
  'kwetsbaarhedenbeheer overheid', 'patch management overheid',
  'security by design overheid', 'MFA overheid', 'HTTPS overheid', 'TLS overheid',
  'DNSSEC', 'DMARC', 'DKIM', 'SPF', 'DANE', 'RPKI', 'internet.nl',
  'Forum Standaardisatie standaarden', 'verplichte standaarden overheid',
  'NCSC richtlijnen', 'NCSC TLS', 'NCSC webapplicaties',
  'DigiToegankelijk', 'WCAG overheid', 'toegankelijkheid overheid',
  'digitale toegankelijkheid', 'EN 301 549', 'ENSIA', 'DigiD normenkader',
  'OAuth overheid', 'OpenID NLGov', 'SAML overheid', 'API Design Rules',
  'Wet digitale overheid', 'NORA', 'pas toe of leg uit',
  'Cyber Resilience Act', 'CRA overheid', 'AI Act overheid', 'eIDAS',
  'EUDI Wallet', 'SBOM overheid', 'security.txt',
  of wanneer de gebruiker een systeem wil laten voldoen aan de BIO2-normen
  of andere verplichte overheidsstandaarden.
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

Bron: [GitHub — MinBZK/Baseline-Informatiebeveiliging-Overheid](https://github.com/MinBZK/Baseline-Informatiebeveiliging-Overheid) | [BIO2 v1.2 PDF](https://www.bio-overheid.nl/media/cs5ctudu/20250924-baseline-informatiebeveiliging-overheid-2-bio2-v12-deff.pdf) | [bio-overheid.nl](https://www.bio-overheid.nl/category/producten/bio)

### Belangrijke wijzigingen t.o.v. BIO 1.04zv

- De drie basisbetrouwbaarheidsniveaus (BBN1/BBN2/BBN3) zijn **afgeschaft** — volledig risicomanagement is nu leidend
- Nieuwe structuur op basis van NEN-EN-ISO/IEC 27002:2022 (vervangt de oude 27002:2013-structuur)
- Publicatie van ISMS-reikwijdte en Verklaring van Toepasselijkheid (VvT) is **verplicht**
- Afgestemd op NIS2-richtlijn (Artikel 21 over cyberbeveiligingsmaatregelen)
- BIO2 vereist geen ISO 27001-certificering, maar wel toepassing van de standaard
- Provincies, waterschappen en Rijksoverheid: BIO2 als verplichtende zelfregulering sinds september 2025
- Gemeenten: BIO 1.04zv blijft van kracht maar BIO2 als leidraad tijdens transitie

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

## Cyberbeveiligingswet (Cbw) — NIS2-implementatie

De Cyberbeveiligingswet is de Nederlandse implementatie van de EU NIS2-richtlijn. BIO2 dient als de sectorspecifieke invulling van de zorgplicht voor de overheidssector.

| Aspect | Detail |
|--------|--------|
| **Status** | Wetsvoorstel ingediend bij Tweede Kamer op 4 juni 2025; verwachte inwerkingtreding Q2 2026 |
| **Vervangt** | Wet beveiliging netwerk- en informatiesystemen (Wbni) |
| **Verantwoordelijk** | NCTV / Ministerie van Justitie en Veiligheid |
| **Reikwijdte** | ~8.000+ organisaties in essentiële en belangrijke sectoren |

**Drie hoofdverplichtingen:**

1. **Zorgplicht**: passende en proportionele technische, operationele en organisatorische maatregelen
2. **Meldplicht**: eerste waarschuwing binnen 24 uur, volledig rapport binnen 72 uur, eindrapport binnen 1 maand
3. **Bestuurlijke verantwoordelijkheid**: bestuur moet risicobeheersmaatregelen goedkeuren en kennis aantonen via opleiding

**Regelgevingsstructuur:** Cyberbeveiligingswet (Cbw) → Cyberbeveiligingsbesluit (Cbb) → sectorale ministeriële regelingen (waaronder BIO2 voor de overheidssector)

- [Digitale Overheid — Cyberbeveiligingswet](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cyberbeveiligingswet/)
- [NCTV — Cyberbeveiligingswet](https://www.nctv.nl/onderwerpen/c/cyberbeveiligingswet)

## Verplichte internetstandaarden (Forum Standaardisatie)

BIO2-maatregel 5.14.01 vereist dat internetgerichte systemen en e-mail voldoen aan verplichte standaarden van Forum Standaardisatie. Dit zijn de specifieke standaarden:

### Webbeveiliging

| Standaard | Status | Toelichting |
|-----------|--------|-------------|
| **HTTPS en HSTS** | **Wettelijk verplicht** (AMvB sinds 1 juli 2023) | Alle publiek toegankelijke overheidswebsites; configuratie conform NCSC TLS-richtlijnen |
| **TLS** | Verplicht (pas toe of leg uit) | TLS 1.3 = Goed; TLS 1.2 = Voldoende; TLS 1.0/1.1 = Onvoldoende (uitfaseren) |
| **DNSSEC** | Verplicht (pas toe of leg uit) | Integriteit en authenticiteit van DNS-responses; voorkomt DNS-spoofing |
| **IPv6** | Verplicht (pas toe of leg uit) | Naast IPv4 ondersteunen; RPKI vereist bij nieuwe IPv6-adressen |
| **RPKI** | Verplicht (pas toe of leg uit) | Route origin validation voor BGP; voorkomt route-hijacking |

### E-mailbeveiliging

| Standaard | Status | Toelichting |
|-----------|--------|-------------|
| **DMARC** | Verplicht (pas toe of leg uit) | E-maildomeinauthenticatie; streefbeeld p=reject |
| **DKIM** | Verplicht (pas toe of leg uit) | Cryptografische ondertekening van e-mailberichten |
| **SPF** | Verplicht (pas toe of leg uit) | Bepaalt welke mailservers namens een domein mogen verzenden; streefbeeld -all |
| **STARTTLS en DANE** | Verplicht (pas toe of leg uit) | Versleuteld e-mailtransport tussen mailservers; DANE pint TLS-certificaten via DNS |

### Overige verplichte standaarden

| Standaard | Status | Toelichting |
|-----------|--------|-------------|
| **STIX en TAXII** | Verplicht (pas toe of leg uit) | Gestandaardiseerd delen van cyber threat intelligence |
| **NEN-ISO/IEC 27001** | Verplicht (pas toe of leg uit) | ISMS-raamwerk; BIO2 Deel 1 volgt deze structuur |
| **NEN-ISO/IEC 27002** | Verplicht (pas toe of leg uit) | Beveiligingsmaatregelen; BIO2 Deel 2 voegt overheidsmaatregelen toe |
| **AdES Baseline Profiles** | Verplicht (pas toe of leg uit) | Geavanceerde elektronische handtekeningen (eIDAS); vereist door BIO2 5.14.03 |
| **ODF** | Verplicht (pas toe of leg uit) | Open Document Format voor uitwisselbare documenten |
| **PDF/A** | Verplicht (pas toe of leg uit) | Documentarchivering en -uitwisseling |

**Compliancetest:** [internet.nl](https://internet.nl) — test HTTPS, TLS, DNSSEC, DMARC, DKIM, SPF, STARTTLS, DANE, RPKI en IPv6 voor overheidsdomein.

## NCSC-richtlijnen

Het Nationaal Cyber Security Centrum (NCSC) publiceert gezaghebbende beveiligingsrichtlijnen. Sinds 1 januari 2026 zijn NCSC en DTC (Digital Trust Center) samengevoegd.

### ICT-beveiligingsrichtlijnen voor TLS (versie 2025-05)

Vier configuratieniveaus:

| Protocol | Niveau | Actie |
|----------|--------|-------|
| TLS 1.3 | **Goed** | Voorkeur |
| TLS 1.2 | **Voldoende** | Acceptabel (afgewaardeerd in 2025) |
| TLS 1.1 | **Onvoldoende** | Uitfaseren |
| TLS 1.0 | **Onvoldoende** | Uitfaseren |

De versie 2025-05 adviseert **hybride (quantum-safe) oplossingen** ter voorbereiding op post-quantum cryptografiedreigingen.

- [NCSC TLS-richtlijnen 2025-05](https://www.ncsc.nl/documenten/publicaties/2025/juni/01/ict-beveiligingsrichtlijnen-voor-transport-layer-security-2025-05)

### ICT-beveiligingsrichtlijnen voor Webapplicaties

Wettelijk verplicht voor alle via internet toegankelijke overheidswebsites. Dekt veilig ontwikkelen, beheren en aanbieden van webapplicaties en REST-API's.

- [NCSC Webapplicatie-richtlijnen](https://www.ncsc.nl/onderwerpen/ict-beveiligingsrichtlijnen-voor-webapplicaties)

### Basisprincipes voor Digitale Weerbaarheid (2025)

Vijf principes (gebaseerd op NIST CSF en NIS2):

1. **Breng de risico's in kaart** — Ken je risico's
2. **Bevorder veilig gedrag** — Bewustwording en training
3. **Bescherm je systemen** — Technische maatregelen
4. **Beheer de toegang** — Identiteit en autorisatie
5. **Bereid je voor op incidenten** — Detectie en respons

- [NCSC Basisprincipes](https://www.ncsc.nl/basisprincipes)

## DigiToegankelijk (WCAG)

**Wettelijk verplicht** voor alle overheidswebsites, mobiele apps, intranets, extranets en cloudapplicaties op basis van het Besluit digitale toegankelijkheid overheid (Wet digitale overheid).

| Aspect | Detail |
|--------|--------|
| **Standaard** | EN 301 549 met WCAG 2.1 level A en AA |
| **WCAG 2.2** | Nog **niet** verplicht (EN 301 549 nog niet bijgewerkt); wel aanbevolen voor nieuwe implementaties |
| **Beheerder** | Logius; beleid door Ministerie van BZK |
| **Toegankelijkheidsverklaring** | Verplicht en jaarlijks bijwerken |
| **Audit** | Elke 36 maanden een nieuwe toegankelijkheidsaudit |

**Complianceniveaus:**

- **Status A**: alle 50 geteste succescriteria voldaan + verklaring gepubliceerd
- **Status B**: gedeeltelijke compliance + verklaring met verbeterplan
- **Status C**: verklaring gepubliceerd + audit gepland binnen 6 maanden

Alle drie de statussen (A, B, C) gelden als wettelijk compliant.

**European Accessibility Act (EAA):** Sinds 28 juni 2025 moeten ook commerciële e-commerce-sites voldoen aan WCAG 2.2 AA.

- [DigiToegankelijk.nl](https://www.digitoegankelijk.nl/)
- [Wat is verplicht?](https://www.digitoegankelijk.nl/wetgeving/wat-is-verplicht)

## Authenticatie- en API-standaarden

### Authenticatie (verplicht — pas toe of leg uit)

| Standaard | Toelichting |
|-----------|-------------|
| **OpenID.NLGov + SAML** | Gecombineerde verplichte standaard sinds september 2023. Identity providers moeten beide ondersteunen. OIDC is de toekomststandaard; SAML blijft relevant voor legacy SSO |
| **NL GOV Assurance Profile for OAuth 2.0** | Verplicht voor REST-API's waar gebruikers toestemming geven aan derden. Versie 1.1 (in procedure) voegt machine-to-machine (M2M) client credentials toe |

### API-standaarden (verplicht — pas toe of leg uit)

| Standaard | Toelichting |
|-----------|-------------|
| **NLGov REST API Design Rules** (v2.0) | Verplicht bij het aanbieden van REST-API's voor overheidsinformatie. Modulair met verplichte modules voor Transport Security. [Logius](https://logius-standaarden.github.io/API-Design-Rules/) |
| **OpenAPI Specification** (v3+) | API-documentatie moet als OAS v3+ definitie worden aangeboden |
| **NL GOV Profile for CloudEvents** | Verplicht sinds november 2025 voor gestandaardiseerde event-notificaties |
| **Digikoppeling** | Verplicht voor gegevensuitwisseling met GDI-componenten (basisregistraties) of cross-sectorale uitwisseling. Vier koppelvlakstandaarden: WUS, ebMS2, REST-API (met FSC), Grote Berichten |

## Audit en compliance

### ENSIA — Eenduidige Normatiek Single Information Audit

Jaarlijks zelfevaluatie- en auditframework voor overheidsorganisaties om BIO-compliance aan te tonen. Principe: Single Information, Single Audit — één set informatie dient zowel horizontale (aan raad/bestuur) als verticale (aan nationale toezichthouders) verantwoording.

**ENSIA dekt:** BIO-compliance, DigiD, BRP, Reisdocumenten, Suwinet, BAG, BGT, BRO.

- [Digitale Overheid — ENSIA](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/ensia/)
- [VNG — ENSIA](https://vng.nl/projecten/ensia)

### DigiD Normenkader 3.0

Verplichte externe beveiligingsassessment voor alle organisaties die aansluiten op DigiD. Bevat 21 normen op basis van NCSC-richtlijnen (inclusief TLS 2025-05). Jaarlijks assessment van 1 januari tot 1 mei.

- [Logius — DigiD Normenkader](https://www.logius.nl/onze-dienstverlening/toegang/digid/ict-beveiligingsassessments-digid/documentatie/norm-ict-beveiligingsassessments-digid)

### Internet.nl — Compliancetesting

Geautomatiseerde test van overheidswebsites en e-maildomeinen op naleving van verplichte internetstandaarden: IPv6, DNSSEC, HTTPS, HSTS, TLS, DMARC, DKIM, SPF, STARTTLS, DANE, RPKI, security.txt.

- [Internet.nl](https://internet.nl)

## Architectuur

### NORA — Nederlandse Overheid Referentie Architectuur

Overkoepelend architectuurraamwerk met 10 basisprincipes en 40 afgeleide principes. Gebaseerd op TOGAF.

**NORA-familie (dochterarchitecturen):**

| Architectuur | Laag |
|-------------|------|
| **GEMMA** | Gemeenten |
| **PETRA** | Provincies |
| **WILMA** | Waterschappen |
| **RORA** | Rijksoverheid (sinds 2024, vervangt EAR) |

- [NORA Online](https://www.noraonline.nl)

## Standaardenhiërarchie

```
EU-niveau
  ├── NIS2-richtlijn → Cyberbeveiligingswet (Cbw, verwacht Q2 2026)
  ├── Cyber Resilience Act (CRA) → SBOM, kwetsbaarhedenbeheer (dec 2027)
  ├── AI Act → risicogebaseerde AI-eisen (aug 2026)
  ├── EN 301 549 → DigiToegankelijk (WCAG 2.1)
  ├── AVG (GDPR)
  ├── European Accessibility Act (EAA)
  ├── Data Act → datatoegang en cloudservices (sep 2025)
  └── eIDAS 2.0 → EUDI Wallet + AdES Baseline Profiles
Nationale wetgeving
  ├── Cyberbeveiligingswet (Cbw)
  ├── Wet digitale overheid (Wdo, sinds 1 juli 2023)
  └── AMvB HTTPS/HSTS (wettelijk verplicht sinds 1 juli 2023)
Overheidsbaseline
  └── BIO2 (gebouwd op ISO 27001:2023 + ISO 27002:2022)
Forum Standaardisatie ("pas toe of leg uit")
  ├── Internet: HTTPS/HSTS, TLS, DNSSEC, DMARC, DKIM, SPF, STARTTLS/DANE, RPKI, IPv6, STIX/TAXII
  ├── API's: NLGov REST API Design Rules, OAuth 2.0 NL GOV, CloudEvents, OpenAPI, Digikoppeling, FSC
  ├── Authenticatie: OpenID.NLGov + SAML
  ├── ISMS: ISO 27001, ISO 27002
  ├── Toegankelijkheid: DigiToegankelijk (EN 301 549/WCAG 2.1)
  └── Documenten: ODF, PDF/A
NCSC-richtlijnen
  ├── TLS-richtlijnen (2025-05)
  ├── Webapplicatie-richtlijnen
  └── Basisprincipes voor Digitale Weerbaarheid
Architectuur
  └── NORA → GEMMA, PETRA, WILMA, RORA
Audit & compliance
  ├── ENSIA (zelfevaluatie + externe audit)
  ├── DigiD Normenkader 3.0
  ├── Internet.nl (geautomatiseerde testing)
  └── Monitor Open Standaarden (halfjaarlijkse meting)
```

## EU-regelgeving met impact op overheidsontwikkeling

Naast de Cyberbeveiligingswet (NIS2) zijn de volgende EU-verordeningen relevant voor softwareontwikkeling bij de overheid:

| Verordening | Impact | Status |
|-------------|--------|--------|
| **Cyber Resilience Act (CRA)** | Verplichte cyberbeveiligingseisen voor producten met digitale elementen; vereist SBOM, kwetsbaarhedenbeheer en security-by-design gedurende hele levenscyclus | Van kracht sinds december 2024; verplichtingen gefaseerd van toepassing (meldplicht september 2026, volledige compliance december 2027) |
| **AI Act** | Risicogebaseerde eisen voor AI-systemen; hoog-risico AI vereist conformiteitsbeoordeling, transparantie en menselijk toezicht | Van kracht sinds augustus 2024; verboden AI-praktijken februari 2025; verplichtingen voor hoog-risico AI-systemen augustus 2026 |
| **Data Act** | Regelt toegang tot en gebruik van data; impact op IoT-producten en cloudservices bij de overheid | Van kracht; volledig van toepassing vanaf september 2025 |
| **eIDAS 2.0** | European Digital Identity Wallet; overheden moeten EUDI Wallet accepteren voor authenticatie en identificatie | Van kracht sinds mei 2024; lidstaten moeten wallets aanbieden uiterlijk 2026 |

**CRA-impact voor ontwikkelaars:** Software die commercieel op de markt wordt gebracht moet een Software Bill of Materials (SBOM) bevatten, kwetsbaarheden actief melden aan ENISA, en security updates leveren gedurende de ondersteuningsperiode. Open-source software die niet commercieel wordt aangeboden valt buiten de CRA-scope, maar "open-source software stewards" hebben beperkte verplichtingen.

Zie [reference.md](reference.md) voor codevoorbeelden, de volledige relatie-met-andere-standaarden-tabel en uitgebreide bronnenlijst.

## Meer informatie

- [BIO2 op GitHub](https://github.com/MinBZK/Baseline-Informatiebeveiliging-Overheid) | [BIO2 v1.2 PDF](https://www.bio-overheid.nl/media/cs5ctudu/20250924-baseline-informatiebeveiliging-overheid-2-bio2-v12-deff.pdf) | [bio-overheid.nl](https://www.bio-overheid.nl/category/producten/bio)
- [Cyberbeveiligingswet](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cyberbeveiligingswet/) | [NCTV](https://www.nctv.nl/onderwerpen/c/cyberbeveiligingswet)
- [Forum Standaardisatie — Verplichte standaarden](https://www.forumstandaardisatie.nl/open-standaarden/verplicht) | [Alle open standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
- [NCSC — TLS-richtlijnen](https://www.ncsc.nl/documenten/publicaties/2025/juni/01/ict-beveiligingsrichtlijnen-voor-transport-layer-security-2025-05) | [Webapplicatie-richtlijnen](https://www.ncsc.nl/onderwerpen/ict-beveiligingsrichtlijnen-voor-webapplicaties) | [Basisprincipes](https://www.ncsc.nl/basisprincipes)
- [Internet.nl — Compliancetest](https://internet.nl) | [ENSIA](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/ensia/) | [DigiD Normenkader](https://www.logius.nl/onze-dienstverlening/toegang/digid/ict-beveiligingsassessments-digid/documentatie/norm-ict-beveiligingsassessments-digid)
- [NLGov REST API Design Rules](https://logius-standaarden.github.io/API-Design-Rules/) | [DigiToegankelijk.nl](https://www.digitoegankelijk.nl/) | [NORA Online](https://www.noraonline.nl)
