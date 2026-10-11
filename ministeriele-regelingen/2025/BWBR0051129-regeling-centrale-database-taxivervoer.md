---
title: "Regeling centrale database taxivervoer"
identifier: "BWBR0051129"
type: regulation
bwb_type: "ministeriele-regeling"
jurisdiction: nl
language: nl
date: 2025-06-03
last_amended: 2025-07-01
status: in_force
source: "https://wetten.overheid.nl/BWBR0051129/2025-07-01"
source_xml: "https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0051129/2025-07-01_0/xml/BWBR0051129_2025-07-01_0.xml"
authority: "Infrastructuur en Waterstaat"
rechtsgebied: ["Vervoersrecht"]
retrieved: 2026-10-11
---

# Regeling centrale database taxivervoer

*Regeling van de Staatssecretaris van Infrastructuur en Waterstaat, van 3 juni 2025, nr. IENW/BSK-2025/130201, houdende regels met betrekking tot de centrale database taxivervoer (Regeling centrale database taxivervoer) \[KetenID WGK026754\]*

De Staatssecretaris van Infrastructuur en Waterstaat,

Gelet op artikel 83b, derde lid, van het Besluit personenvervoer 2000;

BESLUIT:

## § 1 — Begripsbepalingen

### Artikel 1

In deze regeling wordt verstaan onder:

- *Besluit:* Besluit personenvervoer 2000;
- *centrale applicatie:* applicatie die taxivervoergegevens ontvangt van een of meerdere registratiemiddelen en deze aanlevert aan de CDT via de CDT meldingen API;
- *CDT:* centrale database taxivervoer;
- *CDT Meldingen API:* voorziening voor het uitwisselen van taxivervoergegevens tussen een centrale applicatie en de CDT;
- *gebeurtenis:* voorval dat plaatsvindt binnen het registratiemiddel, zijnde een melding, fout of storing;
- *ICT-oplossing:* het geheel aan digitale technieken en processen voor het registreren van taxivervoergegevens en het aanleveren van deze gegevens aan de CDT;
- *pauze:* een periode van tenminste 15 achtereenvolgende minuten waarin de bestuurder geen werkzaamheden verricht en vrijelijk over zijn tijd kan beschikken;
- *taxivervoergegevens:* gegevens als bedoeld in artikel 83b, tweede lid, van het Besluit;
- *twee factor authenticatie:* methode waarbij de identiteit van een persoon wordt vastgesteld op basis van twee verschillende factoren.

## § 2 — Registratie en aanlevering van taxivervoergegevens

### Artikel 2 — (Registreren en aanleveren van taxivervoergegevens)

1\. De centrale applicatie waarvan de vervoerder gebruik maakt, wordt aangesloten op de CDT als het registratiemiddel en de centrale applicatie voldoen aan de in deze regeling opgenomen voorwaarden.

2\. Via de CDT Meldingen API meldt de vervoerder van welke ICT-oplossing gebruik wordt gemaakt.

3\. De bestuurder maakt gebruik van het registratiemiddel, dat ter beschikking is gesteld door de vervoerder, om taxivervoergegevens te registreren.

4\. De taxivervoergegevens worden door het registratiemiddel geregistreerd en via de centrale applicatie realtime aangeleverd aan de CDT Meldingen API, tenzij sprake is van omstandigheden ten gevolge waarvan deze gegevens niet realtime kunnen worden geregistreerd of aangeleverd.

5\. De omstandigheden waaronder taxivervoergegevens niet realtime kunnen worden aangeleverd, bedoeld in het vijfde lid, zijn beperkt tot:

- a. het niet beschikbaar zijn van de CDT Meldingen API als gevolg van technische problemen of onderhoud;
- b. een verstoring van de gegevensoverdracht tussen centrale applicatie en CDT Meldingen API.

6\. De niet tijdig aangeleverde taxivervoergegevens, bedoeld in het vierde lid, worden onverwijld aangeleverd aan de CDT Meldingen API zodra de omstandigheden, bedoeld in het vijfde lid, zich niet meer voordoen.

7\. Het registreren en aanleveren van taxivervoergegevens vindt plaats aan de hand van de beschrijving, bedoeld in de bijlage.

### Artikel 3 — (Zorgplichten vervoerder)

1\. De vervoerder stelt aan de bestuurder een deugdelijk registratiemiddel ter beschikking.

2\. De vervoerder draagt er zorg voor dat de bestuurder een registratie bijhoudt van de gegevens als genoemd in artikel 83b, tweede lid, van het Besluit.

3\. Indien het registratiemiddel ondeugdelijk, defect of verloren gegaan is, zorgt de vervoerder binnen drie werkdagen voor herstel of een vervangend registratiemiddel.

4\. De vervoerder draagt er zorg voor dat de gegevens, als bedoeld in artikel 7, zesde lid, onverwijld en waarheidsgetrouw worden aangeleverd aan de CDT Meldingen API.

5\. De vervoerder draagt er zorg voor dat de aanlevering aan de CDT Meldingen API zonder foutmeldingen en waarschuwingsberichten verloopt.

6\. Als foutmeldingen of waarschuwingsberichten worden ontvangen, verhelpt de vervoerder onverwijld de oorzaken ervan.

### Artikel 4 — (Validatie van de bestuurder)

1\. De vervoerder valideert de gegevens van de bestuurder bij de CDT Meldingen API voordat de bestuurder voor de eerste keer met het registratiemiddel taxivervoer verricht voor de vervoerder.

2\. Validatie vindt plaats door het aanleveren van het chauffeursnummer en de rijbewijsgegevens van de bestuurder zoals omschreven in de bijlage.

3\. De bestuurder is gevalideerd als:

- a. de rijbewijsgegevens van een geldig rijbewijs zijn;
- b. het chauffeursnummer van een geldige bevoegdheid taxivervoer is; en
- c. het chauffeursnummer en het rijbewijs van dezelfde persoon zijn.

4\. Een niet-gevalideerde bestuurder mag geen taxivervoer voor een vervoerder verrichten, tenzij de CDT Meldingen API niet beschikbaar is ten tijde van de validatiepoging.

5\. Als sprake is van een situatie als bedoeld in het vierde lid, valideert de vervoerder de gegevens als bedoeld in het tweede lid, onverwijld, zodra de CDT Meldingen API weer beschikbaar is.

6\. Als de bestuurder niet in het bezit is van een Nederlands rijbewijs, maar van een niet-Nederlands rijbewijs, valideert de vervoerder het chauffeursnummer van de bestuurder.

7\. De bestuurder met een niet-Nederlands rijbewijs is gevalideerd als het chauffeursnummer van een geldige bevoegdheid taxivervoer is.

### Artikel 5 — (Validatie van de auto waarmee taxivervoer wordt verricht)

1\. De vervoerder valideert een auto waarmee taxivervoer wordt verricht voordat deze voor de eerste keer voor de vervoerder met het registratiesysteem van de CDT wordt gebruikt en legt dit vast.

2\. Validatie vindt plaats door het elektronisch valideren van het kentekenbewijs.

3\. In een niet door de vervoerder gevalideerde auto waarmee taxivervoer wordt verricht, wordt door een bestuurder geen taxivervoer verricht.

### Artikel 6 — (Aanmelden van de bestuurder)

1\. Bij aanvang van de werkzaamheden aan boord van een auto waarmee taxivervoer wordt verricht meldt de bestuurder zich aan op het registratiemiddel.

2\. De bestuurder die in het bezit is van een Nederlands rijbewijs meldt zich aan door zijn Nederlands rijbewijs elektronisch te authentiseren op het registratiemiddel.

3\. Als het Nederlands rijbewijs defect is, meldt de bestuurder zich gedurende een periode van maximaal tien aaneengesloten dagen aan door middel van twee factor authenticatie.

4\. De bestuurder die niet in het bezit is van een Nederlands rijbewijs en wel in het bezit is van een niet-Nederlands rijbewijs meldt zich aan door middel van twee factor authenticatie.

5\. Zonder aanmelden is het een bestuurder niet toegestaan om taxivervoer te verrichten.

### Artikel 7 — (Gebruik van het registratiemiddel door de bestuurder)

1\. Indien de bestuurder, voorafgaand aan de melding, bedoeld in artikel 6, eerste lid, andere werkzaamheden heeft verricht na zijn laatste afmelding als bedoeld in het zevende lid van dit artikel, registreert hij de begin- en eindtijden van de andere werkzaamheden bij de melding als bedoeld in artikel 6, eerste lid.

2\. De bestuurder meldt een rit aan op het registratiemiddel op het moment dat het vervoeren van personen aanvangt.

3\. De bestuurder meldt een rit af op het registratiemiddel op het moment dat het vervoeren van personen is beëindigd.

4\. Ingeval het registratiemiddel niet gekoppeld is aan de taxameter, bedoeld in artikel 78 van het Besluit personenvervoer 2000, voert de bestuurder handmatig de door de taxameter aangegeven totaalprijs in. Als voor het vervoer geen taxameter verplicht is en de volledige ritprijs direct na de rit wordt voldaan voert de bestuurder de door de reiziger verschuldigde vergoeding in.

5\. Gedurende de periode dat er geen registratiemiddel beschikbaar is, als genoemd in artikel 3, derde lid, registreert de bestuurder zijn taxivervoersgegevens op een andere inzichtelijke en controleerbare wijze.

6\. De bestuurder levert de registratie, genoemd in het vijfde lid, uiterlijk de derde werkdag als bedoeld in artikel 3, derde lid, aan bij de vervoerder.

7\. Bij beëindiging van de werkzaamheden aan boord van een auto waarmee taxivervoer wordt verricht meldt de bestuurder zich af op het registratiemiddel.

8\. De bestuurder meldt op het moment dat deze plaats vinden op het registratiemiddel het begin en einde van pauzes die hij tijdens zijn werkzaamheden aan boord van een auto waarmee taxivervoer wordt verricht geniet.

## § 3 — Techniek

### Artikel 8 — (Registratiemiddel)

1\. Het registratiemiddel bevat of heeft de volgende eigenschappen:

- a. een bewegingsdetectie van het registratiemiddel;
- b. een locatiebepaling met een nauwkeurigheid van ten minste 25 meter;
- c. de functionaliteit om de laatst bekende locatie vast te houden;
- d. de functionaliteit om op basis van de locatiebepaling een afgelegde afstand te bepalen met een maximale afwijking van 15%;
- e. een tijdsbepaling met een nauwkeurigheid van ten minste 1 seconde en synchronisatie met een geijkte externe tijdfunctie;
- f. voorzieningen om de bestuurder te authentiseren als genoemd in artikel 6;
- g. de functionaliteit om unieke identificatiecodes van diensten, ritten, pauzes en gebeurtenissen te genereren;
- h. de functionaliteit om diensten, verrichtingen en andere werkzaamheden als genoemd in artikel 83b, tweede lid, onderdeel l van het Besluit, aan en af te melden via de centrale applicatie;
- i. voorzieningen die taxivervoergegevens realtime doorsturen naar de centrale applicatie;
- j. voorzieningen die ervoor zorgen dat er geen taxivervoergegevens verloren kunnen gaan;
- k. de functionaliteit voor de bestuurder om alleen auto's te kunnen opgeven die de vervoerder voor hem heeft toegestaan;
- l. de functionaliteit voor de bestuurder om zich aan te kunnen melden voor vervoerders die hem dat toestaan.

2\. Het is niet toegestaan het registratiemiddel op een wijze te gebruiken die maakt dat taxivervoergegevens kunnen worden gewijzigd of verwijderd voordat deze zijn aangeleverd in de CDT.

### Artikel 9 — (Centrale applicatie)

1\. Het aanleveren van taxivervoergegevens vanaf het registratiemiddel aan de CDT vindt plaats via een centrale applicatie.

2\. De centrale applicatie bevat of heeft de volgende eigenschappen:

- a. een functionaliteit om alle ontvangen gegevens direct en ongewijzigd door te sturen naar de CDT Meldingen API;
- b. een functionaliteit die ervoor zorgt dat berichten in chronologische volgorde van registratie tijdens de werkzaamheden aan boord van de auto waarmee taxivervoer wordt verricht worden aangeboden aan de CDT Meldingen API;
- c. een functionaliteit die maakt dat een volgend bericht aan de CDT Meldingen API pas wordt aangeboden als het voorgaande bericht succesvol is verwerkt.

### Artikel 10 — (Informatiebeveiliging)

1\. De vervoerder maakt gebruik van een ICT-oplossing en een organisatie die zijn gecertificeerd voor ISO 27001. De certificatie wordt verricht door een certificerende instelling die is geaccrediteerd door de Raad voor Accreditatie of een andere accreditatie instelling die is erkend in een lidstaat van de Europese Unie.

2\. De certificering, bedoeld in het eerste lid, heeft als werkingsgebied alle functionaliteit die gegevens levert aan de CDT Meldingen API. De functionaliteit omvat ten minste alle registratiemiddelen en de centrale applicatie.

## § 4 — Overgangs- en slotbepalingen

### Artikel 11 — (Inwerkingtreding)

Deze regeling treedt in werking met ingang van 1 juli 2025.

### Artikel 12 — (Citeertitel)

Deze regeling wordt aangehaald als: Regeling centrale database taxivervoer.

Deze regeling zal met de toelichting in de Staatscourant worden geplaatst.

De Staatssecretaris van Infrastructuur en Waterstaat – Openbaar Vervoer en Milieu,\
C.A. Jansen

## Bijlage — Technische beschrijving van de berichtenuitwisseling voor het aanleveren van taxivervoergegevens aan de CDT Meldingen API (koppelvlakspecificatie CDT)

(bijlage als bedoeld in artikel 2, zevende lid, van de Regeling centrale database taxivervoer)

| | |
| --- | --- |
| 1 | INLEIDING |
| 1.1 | Context |
| 1.2 | Doel |
| 2 | PROCESSEN |
| 2.1 | Aanmelden dienst (relateren chauffeur, ondernemer en voertuig) |
| 2.2 | Aanmelden rit en aanmelden pauze |
| 2.3 | Afmelden rit en afmelden pauze |
| 2.4 | Afmelden dienst |
| 2.5 | Aanmelden ICT-dienstverlener |
| 2.6 | Afmelden ICT-dienstverlener |
| 2.7 | Valideren van chauffeur |
| 2.8 | Opvragen van openstaande diensten en verrichtingen |
| 2.9 | Melden van gebeurtenissen van het registratiemiddel chauffeur |
| 2.10 | Opvragen chauffeursnummer |
| 3 | BERICHTEN |
| 3.1 | Statusovergangen |
| 3.2 | Generieke berichtgegevens in headers |
| 3.3 | Functionele berichtgegevens |
| 3.3.1 | Chauffeur |
| 3.3.2 | Rijbewijs |
| 3.3.3 | Authenticatie |
| 3.3.4 | Ondernemer |
| 3.3.5 | Voertuig |
| 3.3.6 | Andere werkzaamheden |
| 3.3.7 | Locatie |
| 3.4 | Aanmelden dienst (relateren chauffeur, ondernemer en voertuig) |
| 3.5 | Afmelden dienst |
| 3.6 | Aanmelden rit |
| 3.7 | Afmelden rit |
| 3.8 | Aanmelden pauze |
| 3.9 | Afmelden pauze |
| 3.10 | Aanmelden ICT-dienstverlener |
| 3.11 | Afmelden ICT-dienstverlener |
| 3.12 | Valideren chauffeur |
| 3.13 | Opvragen van openstaande diensten en verrichtingen |
| 3.14 | Melden van gebeurtenissen van het registratiemiddel chauffeur |
| 3.15 | Opvragen chauffeursnummer |
| 3.16 | Foutmeldingscodes |
| 3.16.1 | Foutmeldingen wegens headers |
| 3.16.2 | Foutmeldingen wegens fouten in het bericht zelf |
| 3.16.3 | Foutmeldingen wegens verwerken inhoud |
| 4 | TECHNISCHE EISEN |
| 4.1 | Conventies |
| 4.1.1 | JSON conventies |
| 4.1.2 | Encoding |
| 4.1.3 | Hoofdlettergevoeligheid |
| 4.1.4 | Datum/tijd |
| 4.1.5 | Berichtenverkeer |
| 4.1.6 | Endpoints |
| 4.2 | Actualiteit van data |
| 4.3 | Beschikbaarheid en performance |
| 4.3.1 | Beschikbaarheid |
| 4.3.2 | Performance |
| 5 | LOGGING EN MONITORING VERBINDING |
| 5.1 | Logging |
| 5.2 | Connectie-monitoring |
| 6 | FOUTAFHANDELING |
| 6.1 | Algemeen |
| 6.2 | Error in aanroep dienstgerelateerde endpoints |
| 6.3 | Error in aanroep /verbinding |
| 6.4 | Duplicaat detectie |
| 7 | AUTHENTICATIE EN INFORMATIEBEVEILIGING |
| 7.1 | Authenticatie |
| 7.1.1 | PKI Certificaten |
| 7.1.2 | Authenticatie rijbewijs |
| 7.1.3 | Authenticatie kentekenbewijs |
| 7.2 | Informatiebeveiliging |
| 7.2.1 | Transport Layer Security (TLS) |
| 7.2.2 | API-keys |
| 7.3 | Headers |

### 1 — Inleiding

Deze koppelvlakspecificatie geeft een beschrijving van de volgende functies van de CDT-Meldingen-API:

- 1.) Het aanleveren van diensten, ritten en pauzes door de ondernemer;
- 2.) Het valideren van chauffeursgegevens;
- 3.) Het opvragen van openstaande diensten en verrichtingen binnen de CDT;
- 4.) Het aan- en afmelden van ICT-dienstverleners door ondernemers;
- 5.) Het melden van gebeurtenissen van het registratiemiddel chauffeur gerelateerd aan een dienst.
- 6.) Het opvragen van het chauffeursnummer van een taxichauffeur op basis van het nummer van zijn Nederlandse rijbewijs.

#### 1.1 — Context

De chauffeur maakt gebruik van een Registratiemiddel Chauffeur om realtime relevante informatie over de uitvoering van taxivervoer te registreren voor de ondernemer in de centrale applicatie, die de gegevens realtime levert aan de CDT. Voor de uitwisseling van berichten met de ILT is de CDT-Meldingen-API (op basis van REST) ontwikkeld die aangeroepen dient te worden door de Centrale Applicatie.

#### 1.2 — Doel

Dit document is een bijlage bij de Regeling CDT. Het doel van dit document is om aan partijen die gebruik willen maken van de CDT Meldingen API inzicht te verschaffen in de functies en werking van de CDT-Meldingen-API.

### 2 — Processen

In deze koppelvlakspecificatie wordt de term ‘dienst’ gebruikt zoals dat in het dagelijks spraakgebruik wordt gedaan. De betekenis van dienst in dit document is daardoor niet de definitie van Dienst in art 1.7 eerste lid onder c van de Arbeidstijdenwet. Met ‘dienst’ wordt in deze koppelvlakspecificatie ‘de werkzaamheden als taxichauffeur aan boord van de auto waarmee taxivervoer wordt verricht’ bedoeld.

De volgende processen zijn in scope voor de aanlevering bij de CDT:

- 1. Aanmelden dienst (relateren chauffeur, ondernemer en voertuig);
- 2. Melden andere werkzaamheden van de chauffeur voorafgaand aan de dienst;
- 3. Aanmelden rit of pauze;
- 4. Afmelden rit of pauze;
- 5. Afmelden dienst;
- 6. Aanmelden ICT-dienstverlener door ondernemer;
- 7. Afmelden ICT-dienstverlener door ondernemer;
- 8. Valideren van chauffeur;
- 9. Opvragen van openstaande diensten en verrichtingen;
- 10. Doorgeven van gebeurtenissen van het registratiemiddel chauffeur;
- 11. Opvragen van chauffeursnummer.

#### 2.1 — Aanmelden dienst (relateren chauffeur, ondernemer en voertuig)

Preconditie

De ondernemer heeft ervoor gezorgd dat:

- 1. De ICT-dienstverlener is aangemeld bij de CDT Meldingen API;
- 2. Het voertuig is gevalideerd;
- 3. De chauffeur is gevalideerd;
- 4. De chauffeur toegang heeft tot het 'registratiemiddel chauffeur'.

Proces

De chauffeur:

- 1. Authenticeert zich met een toegestane authenticatiemethode;
- 2. Voegt eventueel begin- en eindtijden in van andere werkzaamheden die voorafgaand aan de dienst zijn uitgevoerd;
- 3. Meldt de dienst, met daarop de ondernemer en het voertuig, via het registratiemiddel chauffeur aan bij de centrale applicatie, die vervolgens de dienst onmiddellijk aanmeldt bij de CDT-Meldingen-API.

Postconditie

De aanmelding van de dienst is geregistreerd voor de chauffeur, het voertuig en de ondernemer in de centrale applicatie en in de CDT. De optionele aanmelding van de andere werkzaamheden is geregistreerd voor de chauffeur.

#### 2.2 — Aanmelden rit en aanmelden pauze

Preconditie

- • De dienst waarbinnen de rit of pauze plaatsvindt, is aangemeld en geregistreerd in de centrale applicatie en de CDT;
- • Bij aanmelden pauze: er zijn geen niet-afgemelde ritten of pauzes binnen deze dienst;
- • Bij aanmelden rit: er zijn geen niet-afgemelde pauzes binnen deze dienst;

Proces

- • De chauffeur meldt via het registratiemiddel chauffeur de rit of pauze aan bij de centrale applicatie, die vervolgens de rit of pauze onmiddellijk aanmeldt bij de CDT-Meldingen API.
- • Bij het aanmelden van een rit is de locatie verplicht. Indien er geen actuele locatie beschikbaar is wordt de laatst bekende locatie doorgegeven.

Postconditie

De aanmelding van de rit of pauze is geregistreerd binnen de dienst van de chauffeur in de centrale applicatie en de CDT.

#### 2.3 — Afmelden rit en afmelden pauze

Preconditie

De rit of pauze is geregistreerd in de centrale applicatie en de CDT.

Proces

- • De chauffeur meldt via het registratiemiddel chauffeur de rit of pauze af bij de centrale applicatie, die vervolgens de rit of pauze onmiddellijk afmeldt bij de CDT-Meldingen-API.

Postconditie

De afmelding van de rit of pauze is geregistreerd binnen de dienst voor de chauffeur en de ondernemer in de centrale applicatie en de CDT.

#### 2.4 — Afmelden dienst

Preconditie

De dienst is geregistreerd en alle ritten en pauzes binnen de dienst zijn afgemeld in de centrale applicatie en de CDT.

Proces

De chauffeur meldt via het registratiemiddel chauffeur de dienst af bij de centrale applicatie, die vervolgens de dienst onmiddellijk afmeldt bij de CDT-Meldingen-API.

Postconditie

De afmelding van de dienst is geregistreerd in de centrale applicatie en de CDT.

#### 2.5 — Aanmelden ICT-dienstverlener

Preconditie

De ondernemer neemt een ICT-oplossing af bij de ICT-dienstverlener en heeft de ICT-dienstverlener niet aangemeld bij de CDT Meldingen API.

Proces

De centrale applicatie stuurt de aanmelding van de ondernemer voor de ICT-dienstverlener naar de CDT Meldingen API.

Postconditie

De ICT-dienstverlener is door de ondernemer aangemeld bij de CDT Meldingen API.

#### 2.6 — Afmelden ICT-dienstverlener

Preconditie

De ondernemer is gestopt met het afnemen van de ICT-oplossing van de ICT-dienstverlener en;

De ICT-dienstverlener is door de ondernemer aangemeld bij de CDT Meldingen API.

Proces

De centrale applicatie stuurt de afmelding van de ondernemer voor de ICT-dienstverlener naar de CDT Meldingen API.

Postconditie

De ICT-dienstverlener is door de ondernemer afgemeld bij de CDT Meldingen API.

#### 2.7 — Valideren van chauffeur

Preconditie

Ondernemer beschikt niet over de informatie of een chauffeur bevoegd is.

Proces

Ondernemer valideert via de Centrale applicatie de chauffeursgegevens bij de CDT.

NB: alleen bij validatiecode 0 worden de chauffeursgegevens als gevalideerd beschouwd.

Postconditie

Ondernemer beschikt over de informatie of de opgegeven chauffeursgegevens van een bevoegde chauffeur zijn.

#### 2.8 — Opvragen van openstaande diensten en verrichtingen

Preconditie

Centrale applicatie beschikt niet over de informatie welke diensten en verrichtingen langer dan een opgegeven duur open staan in de CDT.

Proces

Centrale applicatie vraagt diensten en verrichtingen op die langer dan een gespecificeerde tijdsduur (minimaal 24 uur) openstaan bij de CDT.

Postconditie

Centrale applicatie beschikt over de informatie met betrekking tot welke diensten en verrichtingen langer dan de gespecificeerde tijdsduur open staan in de CDT.

#### 2.9 — Melden van gebeurtenissen van het registratiemiddel chauffeur

Gebeurtenissen van het registratiemiddel chauffeur zijn meldingen (M). Een nadere toelichting hierop is te vinden in paragraaf 3.14 van dit document.

Preconditie

De dienst waaraan de gebeurtenis is gerelateerd, is aangemeld en geregistreerd in de centrale applicatie en de CDT.

Proces

Het registratiemiddel chauffeur meldt de gebeurtenis bij de centrale applicatie, die vervolgens de gebeurtenis onmiddellijk meldt bij de CDT-Meldingen-API.

Postconditie

De gebeurtenis is geregistreerd in de centrale applicatie en de CDT.

#### 2.10 — Opvragen chauffeursnummer

Het chauffeursnummer staat niet vermeld op de beschikking bij chauffeurskaarten die zijn uitgegeven voor 2025. Om het chauffeursnummer te achterhalen kan op basis van de gegevens van een Nederlands rijbewijs het chauffeursnummer opgevraagd worden bij de CDT Meldingen API.

Preconditie

Chauffeur en ondernemer beschikken niet over het chauffeursnummer en chauffeur heeft een geldig Nederlands rijbewijs en zijn BSN is geregistreerd bij Kiwa.

Proces

Ondernemer vraagt op basis van het Nederlandse rijbewijs van de chauffeur het chauffeursnummer op bij de CDT.

Postconditie

Indien de chauffeur beschikt over een geldige taxibevoegdheid, levert de CDT het chauffeursnummer terug aan de ondernemer.

NB: voor chauffeurs die geen Nederlands rijbewijs hebben of die bij KIWA niet met een BSN geregistreerd zijn is het niet mogelijk het chauffeursnummer op basis van rijbewijsgegevens op te vragen. Deze chauffeurs ontvangen het chauffeursnummer per brief van KIWA, en dienen het chauffeursnummer door te geven aan de ondernemer.

### 3 — Berichten

Berichten bestaan uit generieke berichtgegevens (metagegevens) en de inhoud van het bericht zelf. ILT heeft ervoor gekozen om de metagegevens als headers in het bericht op te nemen.

#### 3.1 — Statusovergangen

De logische samenhang tussen de berichten en de status van een dienst en verrichting is in onderstaande figuur weergegeven. De berichten ‘opvragen openstaande diensten’ en ‘valideren chauffeurs’ komen niet voor in onderstaand figuur omdat ze geen invloed hebben op de status van diensten en verrichtingen.

![Afbeelding](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0051129/2025-07-01_0/xml/273255.png)

Regels:

- • Diensten mogen alleen worden aangemeld door een aangemelde ICT-dienstverlener;
- • Het aanmelden van een verrichting (rit of pauze) vereist een aangemelde dienst;
- • Het aanmelden van een gebeurtenis vereist een aangemelde dienst;
- • Om een dienst te kunnen afmelden moeten alle verrichtingen binnen die dienst afgemeld zijn;
- • Gebeurtenissen kunnen worden gemeld tijdens een dienst, ongeacht of er een verrichting plaats vindt;
- • De volgende regels gelden bij overlappende verrichtingen:
  - ○ Overlappende ritten zijn toegestaan;
  - ○ Tijdens een rit kan geen pauze worden aangemeld;
  - ○ Tijdens een pauze kan geen rit worden aangemeld.
- • Een pauze kan alleen gemeld worden met een aanmeldtijdstip dat ligt na de laatst afgemelde verrichting.

#### 3.2 — Generieke berichtgegevens in headers

De velden in de onderstaande tabel staan de bericht header.

<table>
<tr><th>Veldnaam</th><th>Type/lengte</th><th>Voorbeeld</th><th>Toelichting</th></tr>
<tr><td>Dienstverlener</td><td>UUID</td><td>a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11</td><td>Door ILT uitgegeven sleutel die de aanleverende ICT-dienstverlener uniek identificeert bij de CDT-Meldingen-API.</td></tr>
<tr><td>ext_key</td><td>UUID</td><td>a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11</td><td>Unieke sleutel voor toegang tot de API-gateway</td></tr>
<tr><td>Bericht-Id</td><td>UUID</td><td>a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11</td><td>Identificatie van een bericht.<br>NB: dit dient gegenereerd te worden bij het verzenden van het bericht.</td></tr>
<tr><td>Verzendtijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>2023-03-31T14:55:44Z of<br>2023-03-31T14:55:44.444Z</td><td>Verzendtijdstip van bericht van ICT-dienstverlener naar ILT.<br>NB: dit tijdstip dient bij iedere verzendpoging geactualiseerd te worden.</td></tr>
<tr><td>Softwareversie-Registratiemiddel</td><td>String(20)<sup>1</sup></td><td>v12.23.124</td><td>Softwareversie van het registratiemiddel.</td></tr>
<tr><td>Softwareversie-Centrale-Applicatie</td><td>String(20)</td><td>v2.2.9</td><td>Softwareversie van de Centrale applicatie</td></tr>
</table>

<sup>1</sup> Softwareversie-Registratiemiddel mag een empty string zijn als het bericht niet afkomstig is van een ‘registratiemiddel chauffeur’.

#### 3.3 — Functionele berichtgegevens

De velden in de onderstaande tabel kunnen op een bericht voorkomen (in de message body), per bericht is beschreven welke van deze velden voorkomen. Daarnaast staan in paragrafen 3.3.1 tot en met 3.3.7 objecten die in berichten kunnen voorkomen.

<table>
<tr><th>Veldnaam</th><th>Type/lengte</th><th>Voorbeelden</th><th>Toelichting</th></tr>
<tr><td>id</td><td>UUID</td><td>a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11</td><td>Identificatie van een dienst, verrichting of gebeurtenis<br>NB: dit dient gegenereerd te worden bij het ontstaan van de dienst, verrichting of gebeurtenis.</td></tr>
<tr><td>aanmeldtijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>2023-03-31T14:55:44Z of<br>2023-03-31T14:55:44.444Z</td><td>Het tijdstip waarop de dienst of verrichting is gestart.<br>NB: dit is het tijdstip op het registratiemiddel.</td></tr>
<tr><td>afmeldtijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>2023-03-31T14:55:44Z of<br>2023-03-31T14:55:44.444Z</td><td>Het tijdstip waarop de dienst of verrichting is beëindigd.<br>NB: dit is het tijdstip op het registratiemiddel.</td></tr>
<tr><td>ritprijs</td><td>Integer(6)</td><td>10170</td><td>Totale eindprijs van de afgelegde rit in eurocenten. Dit is exclusief fooi.</td></tr>
<tr><td>afstand</td><td>Numeric (4,1)</td><td>12,1</td><td>Afgelegde afstand van rit</td></tr>
<tr><td>registratietijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>2023-03-31T14:55:44Z of<br>2023-03-31T14:55:44.444Z</td><td>Het tijdstip waarop registratie plaatsvindt op het registratiemiddel.</td></tr>
<tr><td>gebeurtenistijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>2023-03-31T14:55:44Z of<br>2023-03-31T14:55:44.444Z</td><td>Tijdstip dat de gebeurtenis plaatsvindt op het registratiemiddel.</td></tr>
<tr><td>gebeurteniscode</td><td>String(4)</td><td>M106</td><td>code uit tabel in paragraaf 3.14</td></tr>
</table>

**Regels**:

- • Bij het bericht is aangegeven welke velden verplicht zijn;
- • Bericht wordt afgewezen als velden niet het juiste formaat of opmaak hebben;
- • Bericht wordt afgewezen als verplichte velden ontbreken;
- • Bericht wordt afgewezen als andere dan toegestane velden aanwezig zijn;
- • Bericht wordt afgewezen als toegestane velden vaker dan gespecificeerd voorkomen.

Naast de velden in bovenstaande tabel kunnen ook objecten worden verstuurd. Deze staan in de volgende paragrafen beschreven.

##### 3.3.1 — Chauffeur

| onderdelen | type | RegEx | voorbeeld | Toelichting |
| --- | --- | --- | --- | --- |
| chauffeursnummer | String(8) | ^T\\d{7}$ | T0012345 | Chauffeursnummer zoals uitgegeven door KIWA |
| gevalideerd | boolean | | true | indicatie of rijbewijs bij CDT Meldingen API gevalideerd is. Deze mag alleen op true worden gezet als op aanroep van POST https://\[host\]/v2/chauffeurs/valideren validatiecode 0 is teruggegeven voor de combinatie chauffeur/ondernemer. |
| rijbewijs | object | | | zie paragraaf 3.3.2 |

Voorbeeld:

<table>
<tr><td colspan="3">"chauffeur": {</td></tr>
<tr><td></td><td colspan="2">"chauffeursnummer": "T0012345",<br>"gevalideerd": true,<br>"rijbewijs": {</td></tr>
<tr><td colspan="2"></td><td>"land": "NL",<br>"nummer": "123456789"</td></tr>
<tr><td></td><td colspan="2">}</td></tr>
<tr><td colspan="3">}</td></tr>
</table>

##### 3.3.2 — Rijbewijs

| onderdelen | type | RegEx | voorbeeld | Toelichting |
| --- | --- | --- | --- | --- |
| land | string2 | ^\[A-Z\]{2\]$ | NL | Landcode volgens ISO3166-1 alpha-2 |
| rijbewijsnummer | string(16) | ^\[0-9a-zA-Z\]{1,16}$ | 1234567890 | Een Nederlands rijbewijsnummer bestaat uit 10 cijfers, andere landen kunnen afwijken. Streepjes, spaties en punten worden weggelaten. |

Voorbeeld:

<table>
<tr><td colspan="3">"rijbewijs": {</td></tr>
<tr><td></td><td colspan="2">"Land": "NL",<br>"rijbewijsnummer": "123456789"</td></tr>
<tr><td colspan="3">}</td></tr>
</table>

##### 3.3.3 — Authenticatie

<table>
<tr><th>onderdelen</th><th>type</th><th>RegEx</th><th>voorbeeld</th><th>Toelichting</th></tr>
<tr><td>middel</td><td>string{4}</td><td>RBNL|BIO|<br>2FA|geen</td><td>RBNL</td><td>RBNL = Nederlands rijbewijs<br>BIO = Biometrie<br>2FA = 2-factor authenticatie<br>geen = chauffeur is niet geauthenticeerd (NB: alleen te gebruiken bij aanmelden dienst door vervoerder bij aanlevering achteraf).</td></tr>
<tr><td>kenmerk</td><td>string(32)</td><td>–</td><td>1234565677<br>vingerafdruk<br>gezichtsherkenning<br>wachtwoord-SMS<br>wachtwoord-koppelcode<br>pincode-SMS<br>pincode-koppelcode<br>geen</td><td>Bij RBNL → rijbewijsnummer<br>Bij BIO → vingerafdruk, gezichtsherkenning<br>Bij 2FA → wachtwoord-SMS,<br>wachtwoord-koppelcode,<br>pincode-SMS,<br>pincode-koppelcode<br>Bij geen → geen.</td></tr>
</table>

Voorbeelden:

<table>
<tr><td colspan="2">"authenticatie": {</td></tr>
<tr><td></td><td>"middel": "RBNL",</td></tr>
<tr><td></td><td>"kenmerk": "2090710264"</td></tr>
<tr><td colspan="2">}</td></tr>
</table>

<table>
<tr><td colspan="2">"authenticatie": {</td></tr>
<tr><td></td><td>"middel": "BIO",</td></tr>
<tr><td></td><td>"kenmerk": "gezichtsherkenning"</td></tr>
<tr><td colspan="2">}</td></tr>
</table>

<table>
<tr><td colspan="2">"authenticatie": {</td></tr>
<tr><td></td><td>"middel": "2FA",</td></tr>
<tr><td></td><td>"kenmerk": "wachtwoord-SMS"</td></tr>
<tr><td colspan="2">}</td></tr>
</table>

<table>
<tr><td colspan="2">"authenticatie": {</td></tr>
<tr><td></td><td>"middel": "geen",</td></tr>
<tr><td></td><td>"kenmerk": "geen"</td></tr>
<tr><td colspan="2">}</td></tr>
</table>

##### 3.3.4 — Ondernemer

| onderdelen | type | RegEx | voorbeeld | Toelichting |
| --- | --- | --- | --- | --- |
| kiwaNummer | string(7) | ^P\\d{4,6}$ | P123456 | nummer van KIWA taxivergunning |
| kvkNummer | string(8) | ^\\d{8}$ | 12345678 | Kamer van Koophandel nummer |

Voorbeeld:

<table>
<tr><td colspan="2">"ondernemer": {</td></tr>
<tr><td></td><td>"kvkNummer": "12345678",</td></tr>
<tr><td></td><td>"kiwaNummer": "P1234"</td></tr>
<tr><td colspan="2">}</td></tr>
</table>

##### 3.3.5 — Voertuig

<table>
<tr><th>onderdelen</th><th>type</th><th>RegEx</th><th>voorbeeld</th><th>Toelichting</th></tr>
<tr><td>kenteken</td><td>string(6)</td><td>^[0-9A-Z]{6}$</td><td>P390HV</td><td>kenteken van het voertuig</td></tr>
<tr><td>validatiemethode</td><td>string(1)</td><td>K|N</td><td>K</td><td>‘K’: kentekenkaart gelezen<br>‘N’: niet gevalideerd</td></tr>
<tr><td>validatiedatum</td><td>string(10)</td><td>^\d{4}-\d{2}-\d{2}$</td><td>2024-03-04</td><td>datum waarop validatie is uitgevoerd, format YYYY-MM-DD. Als validatie-methode = ‘N’ dan de huidige datum gebruiken.</td></tr>
</table>

Voorbeeld:

<table>
<tr><td colspan="2">"voertuig": {</td></tr>
<tr><td></td><td>"kenteken": "P390HV",</td></tr>
<tr><td></td><td>"validatiemethode": "N",</td></tr>
<tr><td></td><td>"validatiedatum": "2024-03-04"</td></tr>
<tr><td colspan="2">}</td></tr>
</table>

##### 3.3.6 — Andere werkzaamheden

<table>
<tr><th>onderdelen</th><th>type</th><th>voorbeeld</th><th>Toelichting</th></tr>
<tr><td>begintijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>2023-03-31T14:55:44Z of<br>2023-03-31T14:55:44.444Z</td><td>datum en tijdstip waarop andere werkzaamheden zijn gestart</td></tr>
<tr><td>eindetijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>2023-03-31T14:55:44Z of<br>2023-03-31T14:55:44.444Z</td><td>datum en tijdstip waarop andere werkzaamheden zijn geëindigd</td></tr>
</table>

Voorbeeld:

<table>
<tr><td colspan="4">"andereWerkzaamheden": [</td></tr>
<tr><td></td><td colspan="3">{</td></tr>
<tr><td colspan="2"></td><td colspan="2">"begintijdstip": "2023-03-31T14:44:55.000Z",</td></tr>
<tr><td colspan="2"></td><td colspan="2">"eindetijdstip": "2023-03-31T15:44:55.000Z"</td></tr>
<tr><td></td><td colspan="3">},</td></tr>
<tr><td></td><td colspan="3">{</td></tr>
<tr><td colspan="2"></td><td colspan="2">"begintijdstip": "2023-03-31T18:44:55.000Z",</td></tr>
<tr><td colspan="2"></td><td colspan="2">"eindetijdstip": "2023-03-31T19:44:55.000Z"</td></tr>
<tr><td></td><td colspan="3">}</td></tr>
<tr><td colspan="4">]</td></tr>
</table>

##### 3.3.7 — Locatie

| onderdelen | type | RegEx | voorbeeld | Toelichting |
| --- | --- | --- | --- | --- |
| breedtegraad | string | ^\[-+\]?(90(\\\\.0{4,6})?\|(\[1-8\]?\\\\d(\\\\.\\\\d{4,6})?))$ | 5.100056 | geografische breedtegraad met 4 tot 6 cijfers achter de punt |
| lengtegraad | string | ^\[-+\]?(180(\\\\.0{4,6})?\|((1\[0-7\]\|\[1-9\])?\\\\d(\\\\.\\\\d{4,6})?))$ | 52.086491 | geografische lengtegraad met 4 tot 6 cijfers achter de punt |

Voorbeeld:

<table>
<tr><td colspan="2">"locatie": {</td></tr>
<tr><td></td><td>"breedtegraad": "5.10005",</td></tr>
<tr><td></td><td>"lengtegraad": "52.08649"</td></tr>
<tr><td colspan="2">}</td></tr>
</table>

#### 3.4 — Aanmelden dienst (relateren chauffeur, ondernemer en voertuig)

Use cases:

- • Aanmelden dienst bij aanvang van de werkzaamheden aan boord van de auto waarmee taxivervoer wordt verricht, eventueel met voorafgaande andere werkzaamheden.

**Endpoint**: POST https://\[host\]/v2/diensten

Bij aanmelden dienst bevat het bericht naast alle generieke berichtgegevens de volgende functionele berichtgegevens:

| Veldnaam | Verplicht |
| --- | --- |
| id (van de dienst) | ja |
| chauffeur | ja |
| authenticatie | ja |
| ondernemer | ja |
| voertuig | ja |
| aanmeldtijdstip | ja |
| registratietijdstip | ja |
| andereWerkzaamheden | nee |

**Response sunny day**: ‘201 CREATED’

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>id</td></tr>
</table>

Meldingen in de onderstaande tabel zijn mogelijk bij een '201 CREATED' resultaatcode.

| Statuscode | Meldingcode | Meldingtekst | Opmerking |
| --- | --- | --- | --- |
| 201 | DF00 | Er zijn \[#\] diensten actief voor de chauffeur bij de ICT-dienstverlener. | Er is voor de opgegeven chauffeur nog een niet-afgesloten dienst bij ILT geregistreerd bij deze ICT-dienstverlener. NB: deze melding wordt niet getoond als de dienst voor de chauffeur open staat bij een andere ICT-dienstverlener. |
| 201 | DF06 | ‘voertuig.kenteken’ is in gebruik op een andere dienst bij de ICT-dienstverlener. | Er is voor het opgegeven voertuig nog een niet-afgesloten dienst bij ILT geregistreerd bij de ICT-dienstverlener. NB: deze melding wordt alleen teruggegeven als de dienst met het voertuig afkomstig is van de aanleverende ICT-dienstverlener. |
| 201 | DF07 | ‘chauffeur’ is niet gevalideerd terwijl deze als gevalideerd is gemarkeerd. | Een chauffeur mag alleen als gevalideerd worden gemeld als een geslaagde validatie is uitgevoerd. |
| 201 | DF08 | ‘ICT-dienstverlener’ is niet aangemeld voor ondernemer | Een ondernemer moet aanmelden welke ICT-dienstverlener voor hem levert. |

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

**Response bij openstaande diensten:** ‘201 CREATED’

gegevens van openstaande dienst(en) bij de inzendende ICT-dienstverlener staan in de message body.

Velden in de response body:

<table>
<tr><td colspan="5">data</td></tr>
<tr><td></td><td colspan="4">id (van de aangemelde dienst)</td></tr>
<tr><td colspan="5">meldingen (optioneel, één of meer)[</td></tr>
<tr><td></td><td colspan="4">code</td></tr>
<tr><td></td><td colspan="4">tekst</td></tr>
<tr><td></td><td colspan="4">details (optioneel, zal voorkomen bij DF00)</td></tr>
<tr><td colspan="2"></td><td colspan="3">openstaandeDiensten (één of meer) [</td></tr>
<tr><td colspan="3"></td><td colspan="2">id</td></tr>
<tr><td colspan="3"></td><td colspan="2">aanmeldtijdstip</td></tr>
<tr><td colspan="3"></td><td colspan="2">openstaandeVerrichtingen (optioneel, één of meer)[</td></tr>
<tr><td colspan="4"></td><td>id</td></tr>
<tr><td colspan="4"></td><td>aanmeldtijdstip</td></tr>
<tr><td colspan="3"></td><td colspan="2">]</td></tr>
<tr><td colspan="2"></td><td colspan="3">]</td></tr>
<tr><td colspan="5">]</td></tr>
</table>

#### 3.5 — Afmelden dienst

Use cases:

- • Afmelden dienst bij einde van de werkzaamheden aan boord van de auto waarmee taxivervoer wordt verricht.

**Endpoint**: POST https://\[host\]/v2/diensten/{dienst.id}/afmelden

Bij afmelden dienst bevat het bericht naast de generieke berichtgegevens in de header de volgende functionele berichtgegevens in de message body:

| Veldnaam | Verplicht |
| --- | --- |
| afmeldtijdstip | ja |
| registratietijdstip | ja |

**Response sunny day**: ‘200 OK’

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>id</td></tr>
</table>

Indien foutcode DF05 (zie paragraaf 3.15) wordt teruggegeven is de response: ‘400’.

<table>
<tr><td colspan="6">data</td></tr>
<tr><td></td><td colspan="5">foutmelding: bericht afgekeurd</td></tr>
<tr><td></td><td colspan="5">aantal: [alle foutmeldingen]</td></tr>
<tr><td></td><td colspan="5">fouten (kunnen er meer zijn)[</td></tr>
<tr><td colspan="3"></td><td colspan="3">code</td></tr>
<tr><td colspan="3"></td><td colspan="3">tekst</td></tr>
<tr><td colspan="3"></td><td colspan="3">details (optioneel)</td></tr>
<tr><td colspan="4"></td><td colspan="2">openstaandeVerrichtingen (één of meer)[</td></tr>
<tr><td colspan="5"></td><td>id</td></tr>
<tr><td colspan="5"></td><td>aanmeldtijdstip</td></tr>
<tr><td colspan="4"></td><td colspan="2">]</td></tr>
<tr><td colspan="2"></td><td colspan="4">]</td></tr>
</table>

Bij overige afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.6 — Aanmelden rit

Use cases:

- • Aanmelden rit als (eerste) passagier instapt.

**Endpoint**: POST https://\[host\]/v2/diensten/{dienst.id}/ritten

Bij aanmelden rit bevat het bericht naast alle generieke berichtgegevens de volgende functionele berichtgegevens:

| Veldnaam | Verplicht |
| --- | --- |
| id (van de rit) | ja |
| aanmeldtijdstip | ja |
| registratietijdstip | ja |
| locatie | ja |

**Response sunny day**: ‘201 CREATED’

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>id</td></tr>
</table>

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.7 — Afmelden rit

Use cases:

- • Afmelden rit als (laatste) passagier uitstapt.

**Endpoint**: POST https://\[host\]/v2/diensten/{dienst.id}/ritten/{rit.id}/afmelden

Bij afmelden rit bevat het bericht naast alle generieke berichtgegevens de volgende functionele berichtgegevens:

| Veld | Verplicht |
| --- | --- |
| afmeldtijdstip | ja |
| registratietijdstip | ja |
| afstand | ja |
| ritprijs | ja |

NB. Bij contractvervoer en groepsvervoer is de prijs niet verplicht. In dat geval mag ritprijs 0 (nul) zijn.

**Response sunny day**: ‘200 OK’

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>id</td></tr>
</table>

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.8 — Aanmelden pauze

Use cases:

- • Aanmelden pauze bij aanvang pauze;

**Endpoint**: POST https://\[host\]/v2/diensten/{dienst.id}/pauzes

Bij aanmelden pauze bevat het bericht naast alle generieke berichtgegevens de volgende functionele berichtgegevens:

| Veldnaam | Verplicht |
| --- | --- |
| id (van de pauze) | ja |
| aanmeldtijdstip | ja |
| registratietijdstip | ja |

**Response sunny day**: '201 CREATED'

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>id</td></tr>
</table>

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.9 — Afmelden pauze

Use cases:

- • Afmelden pauze bij einde pauze;

**Endpoint**: POST https://\[host\]/v2/diensten/{dienst.id}/pauzes/{pauze.id}/afmelden

Bij afmelden pauze bevat het bericht naast alle generieke berichtgegevens de volgende functionele berichtgegevens:

| Veld | Verplicht |
| --- | --- |
| afmeldtijdstip | ja |
| registratietijdstip | ja |

**Response sunny day**: ‘200 OK’

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>id</td></tr>
</table>

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.10 — Aanmelden ICT-dienstverlener

Use case:

- • ondernemer meldt zich aan voor gebruik van ICT-oplossing van ICT-dienstverlener.

**Endpoint:** POST https://\[host\]/v2/ondernemers/aanmelden

In de message body worden de gegeven van de meldende ondernemer doorgegeven.

| Veld | Verplicht |
| --- | --- |
| ondernemer | ja |

**Response sunny day**: ‘200 OK’

Velden in de response body:

<table>
<tr><td colspan="3">data</td></tr>
<tr><td></td><td colspan="2">validaties:[</td></tr>
<tr><td colspan="2"></td><td>validatiecode</td></tr>
<tr><td colspan="2"></td><td>validatieomschrijving</td></tr>
<tr><td></td><td colspan="2">]</td></tr>
</table>

<table>
<tr><th>Validatiecode</th><th>Verificatie-omschrijving</th></tr>
<tr><td>0</td><td>‘ondernemer.kiwaNummer’ is van vergunde taxiondernemer;<br>‘ondernemer.kvkNummer’ is van een bestaande onderneming</td></tr>
<tr><td>1</td><td>‘ondernemer.kiwaNummer’ is onbekend</td></tr>
<tr><td>2</td><td>‘ondernemer.kiwaNummer’ is niet van een vergunde taxiondernemer</td></tr>
<tr><td>3</td><td>‘ondernemer.kvkNummer’ is onbekend</td></tr>
<tr><td>4</td><td>‘ondernemer.kvkNummer’ is van niet-actieve onderneming</td></tr>
</table>

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.11 — Afmelden ICT-dienstverlener

Use case:

- • ondernemer stopt met gebruik maken van ICT-oplossing van ICT-dienstverlener.

**Endpoint:** POST https://\[host\]/v2/ondernemers/{ondernemer.kiwaNummer}/afmelden

**Response sunny day**: ‘200 OK’

Er is geen message body aanwezig.

Als de ondernemer onbekend is bij de ICT-dienstverlener wordt als response ‘404 – not found’ gegeven.

Bij een afwijzing zijn de meldingen te vinden te vinden in paragraaf 3.16.

#### 3.12 — Valideren chauffeur

Use cases:

- • Controleren of van een chauffeur het Nederlands rijbewijsnummer en chauffeursnummer geldig zijn en van dezelfde persoon zijn.
- • Controleren of chauffeursnummer van een chauffeur met een buitenlands rijbewijs bestaat en geldig is.

**Endpoint:** POST https://\[host\]/v2/chauffeurs/valideren

In de message body wordt de te valideren chauffeur opgegeven met zijn chauffeursnummer en Nederlandse rijbewijs, en de ondernemer die de validatie uitvoert.

| Veld | Verplicht |
| --- | --- |
| chauffeur | ja |
| ondernemer | ja |

NB: het chauffeursobject heeft het onderdeel ‘gevalideerd’. De waarde hiervan moet false zijn bij deze opvraging.

**Response sunny day**: ‘200 OK’

Velden in de response body:

<table>
<tr><td colspan="3">data</td></tr>
<tr><td></td><td colspan="2">validaties:[</td></tr>
<tr><td colspan="2"></td><td>validatiecode</td></tr>
<tr><td colspan="2"></td><td>validatieomschrijving</td></tr>
<tr><td></td><td colspan="2">]</td></tr>
</table>

<table>
<tr><th>Validatiecode</th><th>omschrijving bij Nederland rijbewijs</th><th>omschrijving bij buitenlands rijbewijs</th></tr>
<tr><td>0</td><td>‘chauffeur.chauffeursnummer’ is van bevoegde chauffeur;<br>‘chauffeur.rijbewijs.rijbewijsnummer’ is van een geldig rijbewijs en beiden zijn van dezelfde chauffeur</td><td>‘chauffeur.chauffeursnummer’ is van een bevoegde chauffeur</td></tr>
<tr><td>1</td><td>‘chauffeur.chauffeursnummer’ is van een andere chauffeur dan ‘chauffeur.rijbewijs.rijbewijsnummer’</td><td>niet van toepassing</td></tr>
<tr><td>2</td><td>‘chauffeur.chauffeursnummer’ onbekend</td><td>‘chauffeur.chauffeursnummer’ onbekend</td></tr>
<tr><td>3</td><td>‘chauffeur.rijbewijs.rijbewijsnummer’ onbekend</td><td>niet van toepassing</td></tr>
<tr><td>4</td><td>‘chauffeur.chauffeursnummer’ is van onbevoegde chauffeur</td><td>‘chauffeur.chauffeursnummer’ is van onbevoegde chauffeur</td></tr>
<tr><td>5</td><td>rijbewijs is ongeldig</td><td>niet van toepassing</td></tr>
</table>

Als op deze validatie de validatiecode 0 is geretourneerd mag bij aanmelden dienst voor deze chauffeur met chauffeur.chauffeursnummer en chauffeur.rijbewijs.nummer chauffeur.gevalideerd op true worden gezet. Alle voorgaande gebruikte combinaties van chauffeur.chauffeursnummer met chauffeur.rijbewijs.nummer gelden vanaf dat moment niet meer als gevalideerd.

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.13 — Opvragen van openstaande diensten en verrichtingen

Use case:

- • Opvragen openstaande diensten en verrichtingen.

Endpoint:

GET https://\[host\]/v2/diensten/openstaand?ouderdan=24

Deze aanvraag heeft geen message body.

Geeft alle niet-afgemelde diensten met eventueel niet-afgemelde verrichtingen met een aanmeldtijdstip langer dan x uur geleden voor ICT-dienstverlener Y, waarbij x een defaultwaarde heeft van 24, dus als ouderdan wordt weggelaten wordt 24 gebruikt. Een lagere waarde dan 24 wordt genegeerd, in plaats daarvan wordt 24 gebruikt.

Headers: Softwareversie-Registratiemiddel mag leeg (empty string) zijn indien de opvraging afkomstig is van centrale applicatie.

**Response sunny day**: ‘200 OK’

Velden in de response body:

<table>
<tr><td colspan="4">data</td></tr>
<tr><td></td><td colspan="3">openstaandeDiensten (kunnen er meer zijn) [</td></tr>
<tr><td colspan="2"></td><td colspan="2">id [</td></tr>
<tr><td colspan="2"></td><td colspan="2">aanmeldtijdstip</td></tr>
<tr><td colspan="2"></td><td colspan="2">openstaandeVerrichtingen (optioneel, kunnen er meer zijn) [</td></tr>
<tr><td colspan="3"></td><td>id,</td></tr>
<tr><td colspan="3"></td><td>aanmeldtijdstip</td></tr>
<tr><td colspan="2"></td><td colspan="2">]</td></tr>
<tr><td></td><td colspan="3">]</td></tr>
</table>

Als er geen openstaande diensten zijn dan krijgt de aanroep een ‘204 No Content’ response zonder message body.

#### 3.14 — Melden van gebeurtenissen van het registratiemiddel chauffeur

Use case:

- • Een gebeurtenis op het registratiemiddel chauffeur melden bij de ILT.

Endpoint: (alle gebeurtenissen worden als dienstgebonden beschouwd)

POST https://\[host\]/v2/diensten/{dienstId}/gebeurtenissen

Velden:

| Veld | Verplicht |
| --- | --- |
| id (van de gebeurtenis) | Ja |
| gebeurtenistijdstip | Ja |
| registratietijdstip | Ja |
| gebeurteniscode | Ja |
| authenticatie | Nee<sup>1</sup> |
| locatie | Nee<sup>1</sup> |

<sup>1</sup> zie tabel hieronder wanneer dit veld verplicht is.

De codes voor Meldingen zijn verplicht.

<table>
<tr><th>Gebeurteniscode</th><th>Omschrijving</th><th>Veld verplicht</th></tr>
<tr><td colspan="3"><b>Meldingen</b></td></tr>
<tr><td>M100<sup>1</sup></td><td>Authenticatiepoging voor en tijdens dienst niet succesvol.</td><td>authenticatie</td></tr>
<tr><td>M101</td><td>Uitval van registratiemiddel chauffeur tijdens dienst.<br>NB: deze melding zal pas kunnen worden gegenereerd als het registratiemiddel na uitval opnieuw wordt opgestart.</td><td></td></tr>
<tr><td>M102</td><td>Geen positiebepaling langer dan 3 minuten.</td><td>locatie (laatst bekende locatie)</td></tr>
<tr><td>M103</td><td>Positiebepaling succesvol na gebeurtenis M102.</td><td>locatie</td></tr>
<tr><td>M104</td><td>Tijd op registratiemiddel langer dan 10 minuten niet gesynchroniseerd.</td><td></td></tr>
<tr><td>M105</td><td>Tijd op registratiemiddel gesynchroniseerd na melding synchronisatieprobleem.</td><td></td></tr>
<tr><td>M106</td><td>Geen beweging gedetecteerd langer dan 1 minuut tijdens verrichting ‘rit’ terwijl positiebepaling beweging suggereert.</td><td></td></tr>
<tr><td>M107</td><td>beweging gedetecteerd terwijl positiebepaling beweging suggereert na melding M106.</td><td></td></tr>
<tr><td>M108<sup>2</sup></td><td>Geen gegevensverbinding langer dan 1 minuut met registratiemiddel chauffeur.</td><td></td></tr>
<tr><td>M109<sup>2</sup></td><td>Gegevensverbinding hersteld met registratiemiddel chauffeur na onderbreking.</td><td></td></tr>
<tr><td>M110<sup>2</sup></td><td>Dienst afgemeld door ondernemer</td><td></td></tr>
<tr><td>M111<sup>2</sup></td><td>Verrichting afgemeld door ondernemer</td><td></td></tr>
<tr><td>M112</td><td>Per ongeluk gestarte dienst/verrichting afgesloten.<br>NB: de functionaliteit om een per ongeluk gestarte dienst of verrichting af te sluiten is optioneel. Bij het toepassen van deze functionaliteit is het verzenden van deze gebeurteniscode verplicht.</td><td></td></tr>
<tr><td>M113</td><td>Ritprijs is handmatig opgevoerd.<br>NB: deze melding is niet nodig bij contract- of groepsvervoer, waarbij de waarde van ‘ritprijs’ 0 mag zijn.</td><td></td></tr>
</table>

<sup>1</sup> Melding doorgeven na de eerstvolgende geslaagde aanmelding dienst op het registratiemiddel chauffeur

<sup>2</sup> Melding is normaliter afkomstig van de Centrale Applicatie.

NB: bij M101 en M104 dient het gebeurtenistijdstip het tijdstip te zijn waarop de fout voor het eerst is geconstateerd en het registratietijdstip het tijdstip waarop de fout is gemeld vanuit het detecterende apparaat.

**Response sunny day**: ‘201 OK’

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>id</td></tr>
</table>

Bij een afwijzing zijn de meldingen te vinden in paragraaf 3.16.

#### 3.15 — Opvragen chauffeursnummer

Use case:

- • Opvragen van een chauffeursnummer op basis van een Nederlands rijbewijsnummer.

Endpoint:

POST https://\[host\]/v2/chauffeursnummer/opvragen

Indien voor het opgegeven Nederlandse rijbewijs het chauffeursnummer kan worden gevonden wordt dit teruggegeven. Indien een niet-Nederlands rijbewijs wordt opgegeven zal geen chauffeursnummer worden gevonden.

Headers: Softwareversie-Registratiemiddel mag leeg (empty string) zijn indien de opvraging afkomstig is van centrale applicatie.

Velden:

| Veld | Verplicht |
| --- | --- |
| rijbewijs | Ja |

**Response als gevonden**: ‘200 OK’

Velden in de response body:

<table>
<tr><td colspan="2">data</td></tr>
<tr><td></td><td>chauffeursnummer</td></tr>
</table>

Bij een afwijzing of geen gevonden resultaat zijn de meldingen te vinden in paragraaf 3.16.

#### 3.16 — Foutmeldingscodes

De CDT Meldingen API kent de onderstaande foutmeldingscodes. Bij iedere errorcode is de http-status code weergegeven en op welke aanroepen deze kan komen.

Codering error codes:

| Code prefix | Soort fout |
| --- | --- |
| Hxxx | technische fout in (een van de) header(s). |
| HFxx | functionele fout in (een van de) header(s). |
| Gxxx | generieke (technische) fout. |
| DFxx | functionele fout in dienstbericht. |
| VFxx | functionele fout in verrichtingbericht. |
| BFxx | functionele fout in gebeurtenisbericht. |
| OFxx | functionele fout in opvraging |

Fouten worden teruggegeven in de response body in het onderstaande format:

<table>
<tr><td colspan="4">data</td></tr>
<tr><td></td><td colspan="3">foutmelding</td></tr>
<tr><td></td><td colspan="3">aantal</td></tr>
<tr><td></td><td colspan="3">fouten [</td></tr>
<tr><td colspan="2"></td><td colspan="2">code</td></tr>
<tr><td colspan="2"></td><td colspan="2">tekst</td></tr>
<tr><td colspan="2"></td><td colspan="2">details (optioneel)</td></tr>
<tr><td colspan="2"></td><td colspan="2">openstaandeVerrichtingen (één of meer)[</td></tr>
<tr><td colspan="3"></td><td>id</td></tr>
<tr><td colspan="3"></td><td>aanmeldtijdstip</td></tr>
<tr><td colspan="2"></td><td colspan="2">]</td></tr>
<tr><td></td><td colspan="3">]</td></tr>
</table>

##### 3.16.1 — Foutmeldingen wegens headers

De onderstaande meldingen kunnen op alle aanroepen worden teruggegeven:

| Status | Melding | Meldingtekst | Toelichting |
| --- | --- | --- | --- |
| 400 | H000 | Ontbrekende header \<headernaam\>. | Dienstverlener, Bericht-Id, Softwareversie-Registratiemiddel, Softwareversie-Centrale-Applicatie of Verzendtijdstip ontbreekt. |
| 400 | H001 | Waarde van ‘Bericht-Id’ voldoet niet aan de opmaak. | Moet UUID zijn |
| 400 | H002 | Waarde van ‘Verzendtijdstip’ voldoet niet aan de opmaak. | IETF RFC3339 ‘date-time’ specificatie. |
| 400 | H003 | Waarde van ‘Verzendtijdstip’ is in de toekomst. | Een bericht kan niet in de toekomst zijn verzonden. |
| 400 | H004 | Waarde van ‘Softwareversie-Registratiemiddel’ voldoet niet aan de opmaak. | ^\[0-9A-Za-z.-\]{2,20}$, mag in specifieke gevallen empty string zijn. |
| 400 | H005 | Waarde van ‘Softwareversie-Centrale-Applicatie’ voldoet niet aan de opmaak. | ^\[0-9A-Za-z.-\]{2,20}$ |
| 400 | H006 | Waarde van ‘Dienstverlener’ voldoet niet aan de opmaak. | Moet UUID zijn |
| 400 | HF00 | Onbekende Dienstverlener. | Dienstverlenercode is niet actief of onbekend. |
| 400 | HF10 | Bericht-Id is niet uniek. | De Bericht-Id op de header moet uniek zijn |

NB: Door de manier waarop de validaties worden uitgevoerd komen de header-foutmeldingen alleen voor op berichten die geen andere foutmeldingen geven.

Gegevens meldingen:

| Code | Aanroep |
| --- | --- |
| A | Aanmelden dienst |
| B | Afmelden dienst |
| C | Aanmelden rit |
| D | Afmelden rit |
| E | Aanmelden pauze |
| F | Afmelden pauze |
| G | Aanmelden ICT-dienstverlener |
| H | Valideren chauffeur |
| I | Melden gebeurtenissen |
| J | Opvragen chauffeursnummer |

NB: ‘Opvragen openstaande diensten’ en ‘afmelden ICT-dienstverlener’ zijn niet opgenomen in de tabellen omdat deze beide geen message body bevatten waarop de foutcodes betrekking hebben.

##### 3.16.2 — Foutmeldingen wegens fouten in het bericht zelf

<table>
<tr><th>Status</th><th>Code</th><th>Tekst</th><th>Toelichting</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th></tr>
<tr><td>400</td><td>G000</td><td>Ongeldige JSON.</td><td>Geldt voor het hele bericht: ongeldige JSON formattering.</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>
<tr><td>400</td><td>G001</td><td>Dubbel veld.</td><td>Gegevens moeten éénduidig zijn, het is niet toegestaan hetzelfde gegeven meer dan één keer in een bericht op te nemen.</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>
<tr><td>400</td><td>G010</td><td>‘aanmeldtijdstip’ ontbreekt.</td><td>verplicht veld</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G011</td><td>Waarde van ‘aanmeldtijdstip’ voldoet niet aan de opmaak.</td><td>De datum/tijd is in UTC, ISO-format yyyy-MM-ddThh:mm:ss.sssZ</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G012</td><td>Waarde van ‘aanmeldtijdstip’ is in de toekomst.</td><td>De datum/tijd mag niet in de toekomst zijn.</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G020</td><td>‘registratietijdstip’ ontbreekt.</td><td>verplicht veld</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G021</td><td>Waarde van ‘registratietijdstip’ voldoet niet aan de opmaak.</td><td>De datum/tijd is in UTC, ISO-format yyyy-MM-ddThh:mm:ss.sssZ</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G022</td><td>Waarde van ‘registratietijdstip’ is in de toekomst.</td><td>De datum/tijd mag niet in de toekomst zijn.</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G030</td><td>‘afmeldtijdstip’ ontbreekt.</td><td>Verplicht veld</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G031</td><td>Waarde van ‘afmeldtijdstip’ voldoet niet aan de opmaak.</td><td>De datum/tijd is in UTC, ISO-format yyyy-MM-ddThh:mm:ss.sssZ</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G032</td><td>Waarde van ‘afmeldtijdstip’ is in de toekomst.</td><td>De datum/tijd mag niet in de toekomst zijn.</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G040</td><td>‘id’ ontbreekt.</td><td>verplicht veld</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G041</td><td>Waarde van ‘id’ voldoet niet aan de opmaak.</td><td>UUID</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G050</td><td>Waarde van padparameter ‘dienst’ voldoet niet aan de opmaak.</td><td>UUID</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G060</td><td>‘chauffeur’ ontbreekt.</td><td>Verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G061</td><td>‘chauffeur.chauffeursnummer’ ontbreekt.</td><td>Verplicht veld</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G062</td><td>Waarde van ‘chauffeur.chauffeursnummer’ voldoet niet aan de opmaak.</td><td>Format ^T\d{7}$, bijv. T0012345.</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G063</td><td>‘chauffeur.gevalideerd’ ontbreekt.</td><td>Verplicht veld</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G064</td><td>Waarde van ‘chauffeur.gevalideerd’ voldoet niet aan de opmaak.</td><td>Boolean, true of false</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G070</td><td>‘chauffeur.rijbewijs’ ontbreekt.</td><td>verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td></tr>
<tr><td>400</td><td>G071</td><td>‘chauffeur.rijbewijs.rijbewijsnummer’ ontbreekt.</td><td>Verplicht veld</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td></tr>
<tr><td>400</td><td>G072</td><td>Waarde van ‘chauffeur.rijbewijs.rijbewijsnummer’ voldoet niet aan de opmaak.</td><td>Veld is maximaal 16 alfanumeriek.</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td></tr>
<tr><td>400</td><td>G073</td><td>‘chauffeur.rijbewijs.land’ ontbreekt.</td><td>Verplicht veld</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td></tr>
<tr><td>400</td><td>G074</td><td>Waarde van ‘chauffeur.rijbewijs.land’ voldoet niet aan de opmaak.</td><td>landcode conform ISO3166-1 alpha-2</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td></tr>
<tr><td>400</td><td>G080</td><td>‘authenticatie’ ontbreekt.</td><td>verplicht bij I als gebeurteniscode = M100</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G081</td><td>‘authenticatie.middel’ ontbreekt.</td><td>verplicht bij I als gebeurteniscode = M100</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G082</td><td>Waarde van 'authenticatie.middel' voldoet niet aan de opmaak.</td><td>Zie paragraaf 3.3 voor toegestane waarden</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G083</td><td>‘authenticatie.kenmerk’ ontbreekt.</td><td>verplicht bij I als gebeurteniscode = M100</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G084</td><td>Waarde van ‘authenticatie.kenmerk’ voldoet niet aan de opmaak.</td><td>Veld is maximaal 32 alfanumeriek.</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G090</td><td>‘ondernemer’ ontbreekt.</td><td>Verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G091</td><td>‘ondernemer.kiwaNummer’ ontbreekt.</td><td>Verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G092</td><td>Waarde van ‘ondernemer.kiwaNummer’ voldoet niet aan de opmaak.</td><td>Eerste positie is altijd een 'P', overige 6 posities zijn cijfers, wanneer de cijferreeks korter is dan 6 posities dient deze uitgevuld te zijn met voorloop- nullen (0).</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G093</td><td>‘ondernemer.kvkNummer’ ontbreekt.</td><td>verplicht veld.</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G094</td><td>Waarde van ‘ondernemer.kvkNummer’ voldoet niet aan de opmaak.</td><td>Wanneer de cijferreeks korter is dan 8 dan dient deze uitgevuld te zijn met voorloopnullen (0).</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr>
<tr><td>400</td><td>G100</td><td>‘voertuig’ ontbreekt.</td><td>Verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G101</td><td>‘voertuig.kenteken’ ontbreekt.</td><td>Verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G103</td><td>Waarde van 'voertuig.kenteken' voldoet niet aan de opmaak.</td><td>Regex ^[0-9A-Z]{6}$</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G104</td><td>‘voertuig.validatiemethode’ ontbreekt.</td><td>Verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G105</td><td>Waarde van ‘voertuig.validatiemethode’ voldoet niet aan de opmaak.</td><td>enumeratie</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G106</td><td>‘voertuig.validatiedatum’ ontbreekt.</td><td>Verplicht</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G107</td><td>Waarde van ‘voertuig.validatiedatum’ voldoet niet aan de opmaak.</td><td>YYYY-MM-DD</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G108</td><td>Waarde van ‘voertuig.validatiedatum’ is in de toekomst.</td><td>De validatiedatum kan niet in de toekomst liggen</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G110</td><td>‘andereWerkzaamheden.begintijdstip’ ontbreekt.</td><td>Verplicht als andereWerkzaamheden aanwezig is</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G111</td><td>Waarde van 'andereWerkzaamheden.begintijdstip' voldoet niet aan de opmaak.</td><td>De datum/tijd is in UTC, ISO-format yyyy-MM-ddThh:mm:ss.sssZ</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G120</td><td>‘andereWerkzaamheden.eindetijdstip’ ontbreekt.</td><td>Verplicht als andereWerkzaamheden aanwezig is</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G121</td><td>Waarde van ‘andereWerkzaamheden.eindetijdstip’ voldoet niet aan de opmaak.</td><td>De datum/tijd is in UTC, ISO-format yyyy-MM-ddThh:mm:ss.sssZ</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G122</td><td>‘andereWerkzaamheden.eindetijdstip’ is voor ‘andereWerkzaamheden.starttijdstip’.</td><td>Start moet voor einde liggen</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G123</td><td>Waarde van ‘andereWerkzaamheden.eindetijdstip’ is na ‘dienst.aanmeldtijdstip’.</td><td>Einde andere werkzaamheden moet voor aanmeldtijdstip dienst liggen</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G130</td><td>‘locatie’ ontbreekt.</td><td>verplicht object bij:<br>- aanmelden rit (C)<br>- gebeurteniscode M102 en M103</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G131</td><td>‘locatie.breedtegraad’ ontbreekt.</td><td>verplicht op locatie</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G132</td><td>Waarde van ‘locatie.breedtegraad’ voldoet niet aan de opmaak.</td><td><u>Numeric(8,6)</u></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G133</td><td>‘locatie.lengtegraad’ ontbreekt.</td><td>verplicht op locatie</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G134</td><td>Waarde van ‘locatie.lengtegraad’ voldoet niet aan de opmaak.</td><td>Numeric(9,6)</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G140</td><td>‘afstand’ ontbreekt.</td><td>verplicht bij afmelden rit</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G141</td><td>Waarde van ‘afstand’ voldoet niet aan de opmaak.</td><td>Numeric</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G150</td><td>‘ritprijs’ ontbreekt.</td><td>verplicht bij rit</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G151</td><td>Waarde van ‘ritprijs’ voldoet niet aan de opmaak.</td><td>Integer</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G160</td><td>Waarde van padparameter ‘rit’ voldoet niet aan de opmaak.</td><td>UUID</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G170</td><td>Waarde van padparameter ‘pauze’ voldoet niet aan de opmaak.</td><td>UUID</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>G180</td><td>‘gebeurtenistijdstip’ ontbreekt.</td><td>Verplicht op melden gebeurtenis</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G181</td><td>Waarde van ‘gebeurtenistijdstip’ voldoet niet aan de opmaak.</td><td>De datum/tijd is in UTC, ISO-format yyyy-MM-ddThh:mm:ss.sssZ</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G182</td><td>Waarde van ‘gebeurtenistijdstip’ is in de toekomst.</td><td>Gebeurtenissen kunnen niet voor het gebeurtenistijdstip worden gemeld.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G190</td><td>‘gebeurteniscode’ ontbreekt.</td><td>verplicht veld</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>G191</td><td>Waarde van ‘gebeurteniscode’ voldoet niet aan de opmaak.</td><td>String(4)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr>
</table>

##### 3.16.3 — Foutmeldingen wegens verwerken inhoud

<table>
<tr><th>status</th><th>Code</th><th>Tekst</th><th>toelichting</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th></tr>
<tr><td>400</td><td>DF01</td><td>Waarde van ‘aanmeldtijdstip’ is binnen een andere dienst.</td><td>Een dienst kan alleen aangemeld worden wanneer de begintijd van de dienst niet overlapt met een afgemelde dienst voor dezelfde chauffeur.</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>DF02</td><td>Waarde van ‘id’ is niet uniek.</td><td>Identificatie moet uniek zijn</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>DF03</td><td>Dienst kan niet worden gevonden op basis van het opgegeven id.</td><td>Een melding binnen een dienst kan alleen worden gedaan wanneer de dienst gevonden kan worden.</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td></tr>
<tr><td>400</td><td>DF04</td><td>Dienst is reeds afgemeld.</td><td>Een dienst kan alleen afgemeld worden wanneer de dienst niet reeds afgemeld is.</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>DF05<sup>1</sup></td><td>Er zijn niet-afgemelde verrichtingen op deze dienst.</td><td>Een dienst kan worden afgemeld als alle verrichtingen op die dienst zijn afgemeld.</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>DF09</td><td>Waarde van ‘afmeldtijdstip’ ligt voor ‘aanmeldtijdstip’ van de dienst</td><td>Een dienst kan niet worden afgemeld voor een tijdstip dat ligt voor het aanmeldtijdstip</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>DF10</td><td>Waarde van ‘afmeldtijdstip’ ligt voor ‘afmeldtijdstip’ van verrichtingen in de dienst</td><td>Een afmeldtijdstip van een dienst kan niet liggen voor aan- of afmeldtijdstippen van verrichtingen binnen de dienst.</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>DF11</td><td>Waarde van ‘afmeldtijdstip’ valt binnen een andere dienst</td><td>Deze kan alleen voorkomen bij achteraf aangeleverde diensten.</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF01</td><td>Waarde van ‘aanmeldtijdstip’ is voor 'dienst.aanmeldtijdstip'.</td><td>Verrichting binnen dienst kan niet eerder beginnen dan dienst</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF02</td><td>Verrichting kan niet worden gevonden op basis van het opgegeven id.</td><td>Een verrichting (rit/pauze) kan alleen worden afgemeld wanneer deze is aangemeld.</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF03</td><td>Verrichting is reeds afgemeld.</td><td>Een afgemelde verrichting (rit/pauze) kan niet worden afgemeld.</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF04</td><td>Waarde van ‘afmeldtijdstip’ is voor ‘aanmeldtijdstip’ van verrichting.</td><td>Een verrichting binnen een dienst kan niet eindigen voor het begin van de verrichting</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF05</td><td>Het maximale aantal verrichtingen is bereikt voor deze dienst.</td><td>Het aantal verrichtingen per dienst is gemaximaliseerd op 100.</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF06</td><td>Waarde van ‘aanmeldtijdstip’ van pauze is binnen rit of pauze.</td><td>Een pauze mag niet overlappen met een andere verrichting.</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF07</td><td>Waarde van ‘aanmeldtijdstip’ van rit is binnen gemelde pauze.</td><td>Een rit kan niet worden gestart als:<br>• eerder een pauze is aangemeld en niet afgemeld;<br>• het aanmeldtijdstip valt binnen een aan- en afgemelde pauze.</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF08</td><td>Waarde van ‘afmeldtijdstip’ van pauze is binnen rit of pauze.</td><td>Een pauze mag niet overlappen met een andere verrichting. NB: deze fout kan in principe alleen voorkomen als achteraf een pauze wordt gemeld.</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF09</td><td>Waarde van ‘afmeldtijdstip’ van rit niet toegestaan, pauze tijdens rit.</td><td>Een rit kan niet worden afgemeld als daardoor een pauze tijdens de rit komt te vallen.</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF10</td><td>Verrichting niet gevonden binnen de opgegeven dienst</td><td>Er wordt een rit of pauze afgemeld waarvan de ID niet bekend is op de dienst</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>VF11</td><td>Waarde van ‘aanmeldtijdstip’ van pauze is voor aangemelde verrichting</td><td>Het is niet toegestaan een pauze te melden met een aanmeldtijdstip voor het aanmeldtijdstip van een andere verrichting.</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>BF01</td><td>Het maximale aantal gebeurtenissen is bereikt voor deze dienst.</td><td>Het aantal gebeurtenissen per dienst is gemaximaliseerd op 100.</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>400</td><td>OF01</td><td>Maximum aantal opvragingen bereikt</td><td>Er geldt een maximaal aantal opvragingen van 500 per dag per ICT-dienstverlener</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr>
</table>

<sup>1</sup> Bij deze code wordt ook de betreffende verrichting(en) teruggegeven in de response.

### 4 — Technische eisen

#### 4.1 — Conventies

##### 4.1.1 — JSON conventies

De Centrale applicatie dient de berichten aan te bieden aan de endpoints van CDT-Meldingen-API door middel van JSON (JavaScript Object Notation) berichten en REST (Representational State Transfer).

Voor een complete technische specificatie van de JSON berichten kan de OpenAPI-specificatie geraadpleegd worden, dit is REF-1.

Velden die geen waarde hebben worden weggelaten.

##### 4.1.2 — Encoding

De character-encoding standaard van de berichten is UTF-8.

##### 4.1.3 — Hoofdlettergevoeligheid

De backend service CDT is WEL hoofdlettergevoelig.

##### 4.1.4 — Datum/tijd

Voor datum en tijd wordt IETF RFC 3339 standaard gehanteerd, specifiek de specificatie van de ‘date-time’ waarde. Alle tijdstippen zijn in UTC.

##### 4.1.5 — Berichtenverkeer

Het berichtenverkeer wordt synchroon afgehandeld. Indien er sprake is van een time-out dient de Centrale applicatie het bericht opnieuw aan te bieden. Een transactie is pas afgerond als een response is ontvangen.

De aanroeper van een transactie dient minimaal 15 seconden te wachten voordat de transactie als timed-out mag worden beschouwd.

##### 4.1.6 — Endpoints

Alle endpoints zijn gespecifieerd in de OpenAPI specificatie \[REF-1\].

#### 4.2 — Actualiteit van data

Berichten dienen zonder vertraging aangeleverd te worden aan de backend service CDT. Elk bericht bevat twee tijdstempels: het moment waarop het feit heeft plaatsgevonden (aanmeldtijdstip of afmeldtijdstip) en het moment waarop het bericht over deze actie wordt aangemaakt (registratietijdstip). In de header ‘verzendtijdstip’ staat het tijdstip waarop de centrale applicatie de aanroep naar de CDT Meldingen API doet.

De ICT-dienstverlener is ervoor verantwoordelijk dat berichten op chronologische volgorde van *registratietijdstip* worden aangeleverd.

#### 4.3 — Beschikbaarheid en performance

##### 4.3.1 — Beschikbaarheid

De API heeft een gegarandeerde beschikbaarheid van 98%.

##### 4.3.2 — Performance

De streeftijd voor het afhandelen van een bericht is \< 2 seconden.

### 5 — Logging en monitoring verbinding

#### 5.1 — Logging

Voor beheerdoeleinden verwacht ILT dat de ICT-dienstverlener alle transacties op de CDT-Meldingen-API logt, inclusief de response van ILT. Deze gegevens dienen minimaal 1 maand te worden bewaard.

#### 5.2 — Connectie-monitoring

Om te monitoren of verbinding tussen de ICT-dienstverlener en ILT mogelijk is, stuurt de ICT-dienstverlener als er langer dan 60 seconden geen andere melding is gestuurd een GET naar https://\[host\]/v2/verbinding, waarop ILT een 200 OK zal terugsturen als teken dat de verbinding tot stand is gekomen. Op deze manier kunnen de beheerorganisaties van beide partijen monitoren of de connectie in orde is.

NB: indien de aanroep naar dit endpoint niet slaagt mogen andere transacties niet worden aangeroepen totdat deze aanroep weer slaagt.

### 6 — Foutafhandeling

Het kan gebeuren dat er fouten optreden in één of meer berichten. Dit hoofdstuk beschrijft wat in welk geval moet gebeuren.

#### 6.1 — Algemeen

Als een bericht met betrekking op een dienst wordt afgewezen dienen berichten voor dezelfde dienst, die chronologisch na dat bericht moeten worden verstuurd, te worden vastgehouden totdat het afgewezen bericht (al dan niet gecorrigeerd) succesvol door de CDT-Meldingen-API is verwerkt.

Als het */verbinding-endpoint* een 500-error geeft is er naar alle waarschijnlijkheid sprake van een verbindingsfout. Er dienen dan geen andere berichten verstuurd te worden naar de CDT Meldingen API en dient er in plaats hiervan iedere minuut een nieuwe oproep naar */verbinding* gedaan te worden totdat deze oproep slaagt. Hierna kan het verzenden van de andere berichten weer hervat worden.

#### 6.2 — Error in aanroep dienstgerelateerde endpoints

Als in één van de aanroepen een foutsituatie optreedt dan worden acties aanbevolen zoals hieronder in de tabel beschreven.

| Status code | Aanbevolen acties. |
| --- | --- |
| 403 | Ongeautoriseerde oproep. Er zijn verkeerde credentials of een onbekend endpoint opgegeven. Herstel is noodzakelijk voor een nieuwe poging. |
| 400 | Bij een 400 wegens fouten in de header of het bericht: herstel eerst de fout en stuur dan een nieuw bericht met de herstelde gegevens. |
| 50x | De CDT Meldingen API is niet bereikbaar. Probeer na 1 minuut opnieuw (zelfde message body, ander-tijdstip, zelfde berichtId). |

#### 6.3 — Error in aanroep /verbinding

Het /verbinding endpoint wordt gebruikt om te controleren of de CDT Meldingen API operationeel is. Dit is een apart geval en is daarom apart behandeld. Als er andere berichten naar de CDT Meldingen API worden verstuurd dient het /verbinding endpoint niet aangeroepen te worden.

| Status code | Aanbevolen acties. |
| --- | --- |
| 40x | Er is een fout gemaakt in de aanroep. Probeer opnieuw met een nieuw bericht. |
| 50x | De CDT Meldingen API is niet bereikbaar. Probeer na 1 minuut opnieuw met een nieuwe aanroep van /verbinding, de huidige oproep mag niet opnieuw aangeboden worden (geen retry voor /verbinding) |

#### 6.4 — Duplicaat detectie

Er is geen duplicaat-detectie, een bericht dat voor de tweede keer wordt aangeboden wordt functioneel afgewezen.

### 7 — Authenticatie en informatiebeveiliging

#### 7.1 — Authenticatie

##### 7.1.1 — PKI Certificaten

De informatie-uitwisseling met de CDT meldingen-API verloopt via de centrale API Security gateway van de ILT waarop alle ICT-dienstverleners aangesloten dienen te worden. Authenticatie door de ICT-dienstverleners vindt plaats met behulp van PKI overheid servercertificaten en clientcertificaten bij de ICT-dienstverlener. Voor meer informatie zie de website van Logius.

##### 7.1.2 — Authenticatie rijbewijs

Bij iedere dienst die wordt gestart dient het Nederlandse rijbewijs van de chauffeur elektronisch te worden geauthenticeerd via NFC. Dit wordt gedaan door de ‘Active Authentication’ van het rijbewijs uit te voeren zoals beschreven in \[REF-2\]. Als dit met succes is uitgevoerd wordt op het aanmelden dienst-bericht het authenticatie-object gevuld met authenticatie.middel: ‘RBNL’ en authenticatie.kenmerk: het uitgelezen rijbewijsnummer. Als de chauffeur niet beschikt over een Nederlands rijbewijs dient op één van de overige wijzen geauthenticeerd te worden. Deze zijn beschreven in paragraaf 3.3.3.

NB: voor het uitlezen van de specimen rijbewijzen die beschikbaar zijn dient u gebruik te maken van aparte certificaten die niet op de website van de RDW beschikbaar zijn. Deze kunt u verkrijgen bij de aansluitcoördinatoren van de ILT.

##### 7.1.3 — Authenticatie kentekenbewijs

Bij het aanmelden van een voertuig voor een vervoerder dient het kentekenbewijs van het voertuig te worden geauthenticeerd middels de ‘Active Authentication’ zoals beschreven in \[REF-3\]. Hierbij wordt het kenteken van het voertuig uitgelezen middels een smartcard-lezer. Hierna mag het kenteken worden gebruikt voor diensten en ritten van deze vervoerder.

Het is mogelijk dat een voertuig door verschillende vervoerders wordt gebruikt, voor iedere vervoerder dient het kentekenbewijs éénmalig te worden geauthenticeerd voor het in gebruik nemen van het voertuig.

NB: voor het uitlezen van de specimen kentekenbewijzen die beschikbaar zijn dient u gebruik te maken van aparte certificaten die niet op de website van de RDW beschikbaar zijn. Deze kunt u verkrijgen bij de aansluitcoördinatoren van de ILT.

#### 7.2 — Informatiebeveiliging

De informatie-uitwisseling gaat van de aanleverende ICT-dienstverleners via het openbare internet naar de beveiligde API-gateway. Alleen vooraf vrijgegeven IP-adressen kunnen berichten hierop aanbieden. De gateway bevindt zich binnen de overheidsinfrastructuur.

##### 7.2.1 — Transport Layer Security (TLS)

Het verkeer vindt plaats over TLS met certificaten aan verzendende en ontvangende zijde. Hiervoor wordt gebruik gemaakt van de actuele standaarden zoals voorgeschreven door Forum Standaardisatie. De certificaten aan ontvangende zijde zijn van de Certificate Authority (CA) van de Rijksoverheid, de certificaten aan verzendende zijde moeten van een publieke CA zijn; de meeste CA's zijn bij de Rijksoverheid bekend en worden geaccepteerd. Mocht er twijfel zijn over een CA neemt u dan contact op de ILT. De meest actuele richtlijnen zijn door het NCSC beschreven in het document ICT-beveiligingsrichtlijnen voor Transport Layer Security (TLS) v2.1.

NB: de acceptatie-omgeving wijkt af van de productieomgeving: in de acceptatieomgeving is geen client-certificaat vereist.

##### 7.2.2 — API-keys

De ILT geeft per ICT-dienstverlener een API-key (ext\_key-header) uit, de ICT-dienstverlener gebruikt de API-key om zich bij de ILT API-gateway te identificeren.

#### 7.3 — Headers

De CDT-Meldingen API verwacht de volgende headers:

<table>
<tr><th>Header</th><th>Waarde</th><th>voorbeeld</th></tr>
<tr><td>Accept</td><td>Vaste waarde</td><td>Accept: application/json</td></tr>
<tr><td>Content-Type</td><td>Vaste waarde</td><td>Content-Type: application/json</td></tr>
<tr><td>Dienstverlener</td><td>UUID</td><td>Dienstverlener: &lt;uuid&gt;</td></tr>
<tr><td>ext_key</td><td>UUID</td><td>ext_key: &lt;uuid&gt;</td></tr>
<tr><td>Bericht-Id</td><td>UUID</td><td>Bericht-Id: &lt;uuid&gt;</td></tr>
<tr><td>Verzendtijdstip</td><td>date-time in UTC conform IETF RFC3339</td><td>Verzendtijdstip: 20241120T17:51:01Z<br>of<br>Verzendtijdstip: 20241120T17:51:01.556Z</td></tr>
<tr><td>Softwareversie-Registratiemiddel</td><td>Max 20 posities</td><td>Softwareversie-Registratiemiddel: v1.0.3</td></tr>
<tr><td>Softwareversie-Centrale-Applicatie</td><td>Max. 20 posities</td><td>Softwareversie-Centrale-Applicatie: v12.6.5</td></tr>
</table>

Zie ook paragraaf 3.2.
