# Verkenning inzet van skills als sturingsmechanisme voor AI-assistants voor softwareontwikkeling

**Toetsing en verantwoording i.h.k.v. Overheidsbreed Standpunt Generatieve AI**

## Beschrijving van het experiment

In dit experiment worden skill files gemaakt op basis van open standaarden, standaarden die voorkomen op de ['Pas toe of leg uit'-lijst](https://www.forumstandaardisatie.nl/node/22) van Forum Standaardisatie en kaders, richtlijnen en afspraken van de Nederlandse overheid. Een skill file is een bestand met specifieke instructies voor een AI-assistant over hoe bijv. een taak uitgevoerd kan worden. Het stuurt dus het gedrag van een AI-assistant aan en/of voegt functionaliteit toe.

In ons geval willen we skills maken die beschrijven hoe een AI-assistant software moet genereren die voldoet aan standaarden en eisen die de Nederlandse overheid stelt. We hopen hiermee een hulpmiddel te kunnen gaan bieden aan partijen die AI-assistant inzetten voor het bouwen van software.

Het experiment kent een iteratief karakter en doorloopt de volgende stappen:

1. Skill aanmaken: Op basis van brondocumentatie (bijv. via Forum Standaardisatie of andere relevante kaders en richtlijnen) maken we een skill aan. Dit doen we met een AI-assistant en/of handmatig. Als een AI-assistant wordt ingezet, dan documenteren we dat. We geven de skills een neutrale naam.

2. Menselijke expertreview: De gegeneerde skills worden gereviewed door experts op het gebied van die standaarden.

3. AI genereert wegwerp-testcode/software met behulp van de skill: Om de werking van de skill te toetsen laten we een AI-assistant een klein stuk wegwerp-software genereren dat basisfunctionaliteit demonstreert die nodig is om de standaard te kunnen testen. Deze testcode gaat nooit in productie en bevat geen persoonsgegevens of vertrouwelijke informatie.

4. Validators + handmatige toetsing: De gegenereerde testcode wordt getoetst, zowel handmatig door een expert als met validatiesoftware.

5. Skills verbeteren: op basis van de uitkomsten verbeteren we de skills.

> Stappen 1 tot en met 5 worden herhaald totdat de skill files aantoonbaar voldoen aan de eisen van de standaard. Gedurende het gehele proces wordt geborgd dat de skills werken met meerdere AI-assistants, zodat vendor lock-in wordt voorkomen.

6. Goedkeuring door eigenaar/beheerder standaard: De eigenaren en/of beheerders van de betreffende standaarden keuren het resultaat goed en geven evt. nader toelichting over bijv. inzet van de skills in praktijk en evt. beperkingen ervan, de omstandigheden en randvoorwaarden voor het gebruik, de te verwachten resultaat, etc.

7. Officieel herkenbare naam: Als de eigenaar of beheerder de skill goedkeurt, krijgt deze een officieel herkenbare naam.

8. Skills beschikbaar: Goedgekeurde skills worden aangeboden voor hergebruik, zowel los als gebundeld via een marktplaats, voor meerdere AI-assistants. Organisaties die de skills gebruiken doen dit op eigen verantwoordelijkheid en moeten voldoen aan het beleid van hun eigen organisatie. Zie daarnaast ook de toelichting over risico op "schijnzekerheid" hieronder.

Het experiment ontwikkelt zelf geen AI-systeem. De software die met AI wordt gegenereerd is de tijdelijke wegwerp-testcode uit stap 3; alle overige software wordt handmatig ontwikkeld. Deze software gaat nooit in productie. De licenties voor de gebruikte AI-tools worden aangeschaft door de betrokken organisatie en er wordt expliciet gekozen voor de opt-out voor modeltraining.

Daarnaast worden skills ook door AI-assistants gegenereerd. Skills zijn geen software als zodanig maar kunnen wel, middels instructies, gedrag van andere software beïnvloeden. Hierdoor moeten ze in bepaalde context als software worden behandeld. Zie bijvoorbeeld paragraaf over security en BIO eisen hieronder.

Validatiesoftware waarmee getoetst wordt of een systeem aan een standaard voldoet, wordt handmatig ontwikkeld, zonder inzet van AI. Deze validators zijn mogelijk ook buiten de context van het experiment nuttig en zullen in dat geval worden aangeboden aan developers, bijvoorbeeld via developer.overheid.nl. Hiermee kunnen ontwikkelaars zelfstandig testen of hun code voldoet aan een overheidsstandaard, ook buiten de context van AI.

Tot slot zullen, in het kader van gebruikersgemak, de skills ook gebundeld worden aangeboden, in de vorm van een marktplaats. We zullen er hierbij op letten dat de oplossing/aanpak in potentie werkt met AI-assistants van verschillende leveranciers.

## Verantwoording van het experiment

We doorlopen hieronder het globale stappenplan zoals weergegeven in hoofdstuk 4 van de [Overheidsbrede handreiking Verantwoord inzet van generatieve AI](https://open.overheid.nl/documenten/9c273b71-cebb-4e11-b06f-fa20f7b4b90e/file)

### 1) Doel en toepassingsgebied

*Doel van het experiment:* Onderzoeken of het mogelijk is om middels skill files, de adviezen die een AI-assistant geeft aan ontwikkelaars van overheidssoftware, aantoonbaar in lijn te brengen met standaarden, kaders en richtlijnen van de Nederlandse overheid.

*Toepassingsgebied:* Alle organisaties die met behulp van AI-assistants, software ontwikkelen voor de overheid.

### 2) Zorg voor de juiste mensen en vaardigheden

Bij het experiment betrekken we softwareontwikkelaars, beleidsmakers en standaard-experts, waaronder beheerders van de betrokken standaarden. Waar nodig investeren we in kennisopbouw en -deling via presentaties, expertsessies en blogposts op developer.overheid.nl.

### 3) Creëer een (generatieve) AI-governance structuur

Het experiment gebeurt in opdracht van Ministerie van Binnenlandse Zaken. We houden hierbij het [Overheidsbreede standpunt voor de inzet van generatieve AI](https://open.overheid.nl/documenten/bc03ce31-0cf1-4946-9c94-e934a62ebe73/file) en de bijbehorende [handreiking](https://open.overheid.nl/documenten/9c273b71-cebb-4e11-b06f-fa20f7b4b90e/file) aan als beleidsmatige leidraad.

Alle tussenresultaten --- skills, gegenereerde wegwerp-testcode --- worden beoordeeld door menselijke experts die deel uitmaken van het projectteam. De definitieve goedkeuring van een skill en de toekenning van een officiële naam geschiedt door de eigenaren en/of beheerders van de standaard waarop de skill is gebaseerd. Dit goedkeuringsproces is aanvankelijk onderdeel van het project zelf. Bij een succesvol experiment wordt het belegd in staande organisaties, zodat skills ook in de toekomst synchroon lopen met de ontwikkeling van de standaarden. Per goedgekeurde skill wordt o.a. gepubliceerd: de gehanteerde procedure, de acceptatiecriteria, de te verwachten resultaat en de bijbehorende gebruiksomstandigheden en de goedkeurende partij.

Het experiment ontwikkelt zelf geen AI-systeem en verwerkt geen persoonsgegevens of vertrouwelijke gegevens. Het eindproduct, als het experiment succesvol blijkt, bestaat uit een set (al dan niet gebundeld aangeboden) skill files die andere organisaties kunnen gebruiken bij het genereren van software met AI. Gebruik hiervan geschiedt op eigen verantwoordelijkheid van die organisaties en in lijn met hun eigen AI-beleid.

Voor maximale transparantie worden tussenresultaten en ervaringen openbaar gedeeld via GitHub en developer.overheid.nl, inclusief de mogelijkheid om erop te reageren met verbetervoorstellen (bijv. middels zogenaamde "issues").

Elke skill wordt voorzien van de volgende metadata: (1) of de skill is gegenereerd met generatieve AI, (2) naam en versie van de skill, (3) gebruikte AI-assistant en model, (4) datum, (5) goedkeuringsstatus (concept of goedgekeurd, met vermelding van de goedkeurende partij).

### 4) Risicoanalyse(s) uitvoeren

De [gangbare assessment instrumenten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/hulpmiddelen/#overzicht-hulpmiddelen) gaan er doorgaans van uit dat de organisatie een AI-systeem bouwt of structureel inzet. Dat is hier niet het geval. We gebruiken een AI-assistant als gereedschap en bouwen zelf geen AI-systeem. Ook nemen we geen AI-software in productie en verwerken we geen persoonsgegevens of vertrouwelijke gegevens. Bovendien betreft het een tijdelijk experiment waarbij de met AI gegenereerde software na gebruik wordt weggegooid. Dit beperkt de risico's die doorgaans gepaard gaan met AI-ontwikkeling, zoals bias en ethische risico's.

Echter, bepaalde risico's en aandachtspunten blijven bestaan, zoals:

#### a. Voldoen aan de EU AI verordening

Omdat wij geen AI systemen maken maar alleen die van anderen als gereedschap gebruiken, vallen de verplichtingen primair op de makers ervan zoals bijv. Anthropic in geval van Claude Code. Anthropic is een van de ondertekenaars van de [General Purpose AI code of practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) van EU wat door [EU wordt gezien als voldoende bewijs dat aan EU AI act is voldaan](https://digital-strategy.ec.europa.eu/en/library/commission-opinion-assessment-general-purpose-ai-code-practice).

We zullen bijhouden welke AI-assistant modellen we gebruiken en alle output van deze assistants markeren als door AI gegenereerd.

#### b. AVG en DPIA verplichtingen

Het experiment verwerkt geen persoonsgegevens. Mocht het voor testdoeleinden nodig zijn om met persoonsgegevens te werken, dan zullen we uitsluitend fictieve gegevens gebruiken.

Organisaties die de skill files in de toekomst gebruiken om systemen te bouwen, dienen op dat moment zelf te beoordelen welke AVG-verplichtingen op hen van toepassing zijn, waaronder een eventuele DPIA. Dit geldt ook voor een eventuele marktplaats voor skills; ook daar worden naar verwachting geen persoonsgegevens verwerkt

#### c. BIO en security eisen

Voor wegwerp-testcode/software gelden geen BIO-verplichtingen. Mocht het experiment validatiesoftware opleveren die ook buiten de experimentcontext wordt aangeboden, bijv. via developer.overheid.nl, dan dient die software mogelijk wél te voldoen aan de geldende beveiligingseisen. Hetzelfde geldt voor een eventuele marktplaats.

Skill files kunnen het gedrag van AI-assitants beïnvloeden. Ook kunnen skill files worden gebruikt om andere software aan te roepen of om data te verkrijgen. Dit betekent dat we, bij het aanmaken van de skills, de skill door experts zullen laten reviewen en auditen op security gevaren (bijv. gebruik van scripts, tools en resources door een skill), Ook gaan we ervoor zorgen dat de toekomstige gebruikers van officiële skills, er zeker van kunnen zijn dat ze de skill kunnen vertrouwen. Bijvoorbeeld door de informatie over de identiteit van de maker en de authenticiteit van de skill te waarborgen.

#### d. Datadeling met AI aanbieder

De risico op datadeling wordt beperkt door in het experiment geen vertrouwelijke data of persoonsgegevens te gebruiken en door in de instellingen van de AI-assistant aan te geven dat de data niet wordt gebruikt voor trainingsdoeleinden (opt-out).

Ook zullen we tijdens het experiment gebruik maken van licenties die gekocht zijn door een overheidsorganisatie.

#### e. Risico op "schijnzekerheid"

Het inzetten van skills bij ontwikkelen van software moet niet gezien worden als een compliance garantie. Officiële brondocumenten (zoals beschrijvingen van standaarden) zijn altijd leidend. Organisatie die skills inzet voor bouw van software blijft zelf verantwoordelijk voor het voldoen aan standaarden en richtlijnen. Skills zijn slechts een hulpmiddel.

#### f. Kwaliteitsrisico: onjuiste standaard-interpretatie in skill files

De kwaliteit wordt op meerdere niveaus geborgd: door menselijke expertreview, door inzet van geautomatiseerde validators en door goedkeuring van de eigenaar of beheerder van de standaard. Een skill krijgt pas een officiële status en naam na deze goedkeuring. De gehanteerde acceptatiecriteria zullen worden gepubliceerd. Tevens wordt een proces ingericht om skills actueel te houden bij wijzigingen van de standaard.

#### g. Auteursrecht op standaard documenten als input voor skills

Er zal per standaard worden gecontroleerd of het mag worden gebruikt als input voor een AI-assistant. Brondocumentatie wordt vermeld, samen met de bijbehorende licentie informatie, waar nodig.

#### h. Uitlegbaarheid van skills / gevaar op "black box"

Er zijn meerdere review processen waarbij een menselijke expert is betrokken: zowel bij totstandkoming als bij goedkeuring. Tevens worden de skills bestanden openbaar en in een voor mens leesbare vorm gepubliceerd.

#### i. AI-geletterdheid van betrokken medewerkers

Er worden kennissessie georganiseerd voor de teamleden. Kennis wordt ook vastgelegd en gedeeld via developer.overheid.nl.

### 5) Generatieve AI inkopen of bouwen

#### a. Vendor lock-in bij specifieke AI-aanbieder

Skills worden zo ontwikkeld dat ze met meerdere AI-assistants te gebruiken zijn. Om dit te waarborgen voeren we alle tests uit met minimaal twee AI-assistants, waarvan minimaal één open-source of Europese AI-assistant. Tevens testen we met lokaal uitvoerbare AI-assistants. Een gebundeld aanbod van skills via een marktplaats, wordt ook dusdanig gerealiseerd dat het in potentie kan werken met AI-assistants van verschillende leveranciers.

#### b. Keuze voor AI-assitants

Het experiment is erop gericht dat iedereen --- binnen en buiten de overheid --- de skill files kan gebruiken om software te genereren die voldoet aan de standaarden, kaders en richtlijnen van de Nederlandse overheid. Dit betekent dat in principe alle AI-assistants die binnen Nederland zijn toegestaan, met de skills in potentie gebruikt moeten kunnen worden in het kader van het experiment. Wij hanteren echter een subset daarvan. We richten ons primair op de grote marktspelers die tevens de [EU General Purpose Code of Practice hebben ondertekend](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) en de EU en open source modellen.
