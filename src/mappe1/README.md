
# 🌍 Mappe 1: Datainnsamling og forberedelse
I den første mappen i prosjektet var formålet å sette opp et utviklingsmiljø, samle inn data og behandle og analysere den. 

![Bilde](/resources/Bilde2.webp)
Bildet er hentet fra ([AlphaTarget](https://alphatarget.com/resources/a-primer-on-artificial-intelligence/), 2024)



#
### Innhold 
Gruppen har valgt å dele alle oppgavene i to deler, da analysen gjennomføres med to ulike datasett: historiske data og fremtidsrettet data. Begge datasettene er hentet fra Yr.no og analyseres separat. Oppgavene og implementeringen er dokumentert i følgende filer: 

Besvarelse for oppgave 1:
- [Testing av utviklingsmiljø](/src/mappe1/utviklingsmiljø.ipynb)

Besvarelse for oppgave 2 og oppgave 3:
- [Databehandling av historisk data](/src/mappe1/data_behandling_historisk.ipynb)
- [Databehandling av fremtidsrettet data](/src/mappe1/data_behandling_fremtid.ipynb)

Overføring til python for testing:
- [Databehandling av historisk data](/src/mappe1/API_historisk.py)
- [Databehandling av fremtidsrettet data](/src/mappe1/API_fremtid.py)

Tilhørende test filer:
- [Test for historisk data](/tests/test_APIhistorisk.py)
- [Test for fremtidig data](/tests/test_APIfremtid.py)

Tilhørende CSV-filer:
- [Værdata i csv format](/data/weather_data.csv)




#
### Oppgave 2 - Datainnsamling

[Url til git repository:](https://github.com/nhstorbe/Prosjekt-Anvendt-)

1) På internett finnes det en stor mengde brukbare kilder på relevant data for værmeldinger. Gruppen har valgt å bruke værdata fra [Yr.no](https://hjelp.yr.no/hc/no/articles/206550539-Om-Yr) for å løse alle oppgavene i prosjektet. Yr.no drives i samarbeid mellom NRK og Meteorologisk institutt, og anses som en pålitelig datakilde ettersom begge aktørene er statlige institusjoner. 

2) For valg av dataformat, gav Yr.no mulighet for å velge mellom ulike formater for nedlastning av data. Det var mulig å brke blant annet JSON-filer, CSV-filer og XML-filer.For den historiske dataen ble CSV-filer benyttet, ettersom dette formatet var lett tilgjengelig fra Yr og enkelt å integrere med Pandas.
For fremtidsrettet data ble Yr sitt API benyttet. Dataen ble hentet i JSON-format da dette formatet er strukturert og enkelt å anvende i Python. I tillegg var gruppen kjent med dictonery fra tidligere kurs. 

3) APIen, i fremtidsrettet data, henter ned en JSON-fil på spesifiserte lengde- og breddegrader (som kan endres i en link) fra meterologisk institutt sin nettside. Den tillater oss å kjøre programmet med oppdatert forecasts data hver gang programmet kjøres for spesifike steder, noe som gir enorm fleksibilitet. De ble hentet ned dato-tidsgruppe, temperatur, nedbørsmengde og vindhastighet fra dataen. 

4) Om Funkjsonene:
- visualiser_data: henter informasjon om værstasjoner fra Frost API ved hjelp av brukerens klient-ID. Den sender en forespørsel til API-et for å få en oversikt over alle tilgjengelige stasjoner. Deretter filtrerer den ut og strukturerer relevante data, som stasjons-ID, navn og land, og konverterer dette til en pandas DataFrame. Til slutt filtreres kun de stasjonene som ligger i Norge, slik at vi får en oversikt over norske værstasjoner som kan brukes videre i datainnsamling eller analyse. Funksjonen returnerer en tabell (DataFrame) med informasjon om disse norske stasjonene.
- get_station_id_by_name: tar en klient-ID og et søkebegrep som input for å finne en værstasjon basert på navnet. Den henter først en liste over alle tilgjengelige stasjoner i Norge ved hjelp av funksjonen visualiserer_data. Deretter søker den etter stasjoner som har et navn som inneholder søkebegrepet, uavhengig av store og små bokstaver. Hvis én matchende stasjon finnes, returneres dens ID. Hvis flere stasjoner matcher, vises en liste med disse stasjonene, og den første stasjonen velges som standard. Hvis ingen stasjoner matcher, får brukeren beskjed om at ingen resultater ble funnet.
- fetch_hourly_weather_to_csv brukes til å hente timesoppløste værdata fra Meteorologisk institutts Frost API, basert på en spesifikk stasjon, dato-intervall og ønskede værparametere. Den henter data for lufttemperatur, relativ luftfuktighet, middelvind og nedbør, og lagrer resultatene i en CSV-fil. For hver av de valgte værparametrene defineres passende elementkoder som benyttes i forespørslene til API-et. Dataene behandles og struktureres i en felles datastruktur før de lagres i fil.
I forsøket på å hente timesbaserte nedbørsdata fra Frost API fikk vi en "412 Precondition Failed"-feil. Dette tror vi skyldes at Meteorologisk institutt ikke benytter seg av en timeoppløsning for nedbør på den valgte stasjonen. Vi testet med flere stasjoner og fikk fortsatt ikke tak i nedbørsdata i timesoppløsning, og antar derfor at Meteorologisk institutt kun leverer nedbør på døgnbasis. I tillegg må man bruke sum når man henter ut nedbørsdata, da nedbør registreres som en akkumulert verdi over tid. For de øvrige variablene som lufttemperatur, relativ luftfuktighet og middelvind benyttes derimot mean, ettersom disse verdiene representerer gjennomsnitt i løpet av en gitt time. Det er likevel verdt å merke seg at kolonnen for nedbør fortsatt eksisterer i CSV-filen, men den inneholder ingen verdier. Dette gir fleksibilitet for fremtidig utfylling dersom nedbørsdata i ønsket oppløsning skulle bli tilgjengelig.

For å forstå dataens struktur og innhold har vi benyttet oss av diverse funksjoner 
- Vi startet med å bruke list comprehensions for å trekke ut spesifikke verdier, som for eksempel temperaturene, direkte fra DataFrame-en på en effektiv måte. Et eksempel på dette er funksjonen hent_varme_dager, som returnerer en liste over tidspunkt og temperatur for alle observasjoner der temperaturen overstiger en gitt grense.
- Deretter tok vi i bruk en iterator med df.iterrows() for å bla gjennom DataFrame-radene én etter én. Dette gjør det mulig å hente ut og presentere flere kolonneverdier samtidig på en oversiktlig måte. Vi laget en funksjon vis_observasjoner, som skriver ut stasjonsnavn, tidspunkt og relativ fuktighet for de første observasjonene i datasettet.
- Til slutt benyttet vi pandasql for å filtrere og analysere datasettet ved hjelp av SQL-syntaks direkte på DataFrame-en. Dette gjør det enklere å trekke ut spesifikke verdier basert på betingelser, som for eksempel alle tilfeller der middelvinden overstiger 10 m/s. Vi laget funksjonen hent_vind_over_grense for å gjøre dette på en fin måte.
 
#
### Oppgave 3 - Databehandling
1) For å håndtere manglende verdier i datasettet, benyttet vi flere metoder. I både ["Historisk databehnadling](/src/Mappe%201/data_behandling_historisk.ipynb) og ["Fremtidig databehandling"](/src/Mappe%201/data_behandling_fremtid.ipynb) startet vi med å undersøke om det fantes hull i dataene. Til dette brukte vi funksjoner som _check_NaN_counter(place)_ og _print(df.isnull().sum())_ for å identifisere antall manglende verdier i datasettet. Når manglende verdier ble oppdaget, tok vi i bruk Pandas-funksjonen fillna(), som erstatter NaN-verdier med spesifiserte verdier. I de fleste tilfeller brukte vi median som erstatning, men i behandlingen av historiske data testet vi også med gjennomsnitt og null som alternativer. Det er viktig å være klar over at slike metoder kan introdusere unøyaktigheter. Værdata varierer betydelig fra dag til dag, og det er derfor vanskelig å erstatte manglende verdier uten å risikere å forvrenge virkeligheten. Spesielt i tilfeller med ekstreme verdier i datasettet kan gjennomsnitt være en dårlig erstatning, ettersom det er svært sensitivt for slike avvik. I slike situasjoner kan median være et bedre valg, da den er mer robust mot ekstreme verdier og gir et mer representativt bilde av datasettet.


2) Vi har brukt list comprehentions for å hente ut og analysere temperaturdata (datasettet vi fokuserer mest på) i både fremtidig og historisk analyse. Historisk sett brukte vi det hovedsakelig for å hente ut og filtrere dataen tidlig i koden. Fremtidig sett brukte vi det veldig lignende, men uttrykket på en nogenlunde annerledes metode. Et sterkt punkt for list comprehentions er å hente ut og analysere data, noe vi fikk sterk nytte av. 

3) I forhold til vanlig Pandas tillater Pandas SQL håndtering med mer SQL orientert språk. Pandas SQL tillater også mer fleksibelitet og alternativer ved datahåndteringen, i tilloegg til at koden blir mer intuitiv å skrive. Kodens leslighet gjelder spesielt når en ønsker å jobbe inn flere kriterier samtidig. For eksempel blir det at vi henter ut middelvind over 5 i verdi gjort mer leslig og oversiktelig enn i vanlig pandas. 

4) De to hovedproblemene datasett pleier å inkludere er manglende verdier, og uteliggende verdier. Slik var situasjonen for våre datasett også. Vi har i begge datasettene filtrert for manglende verdier via den tidligere nevnte fillna. I historisk databehandling har vi også filtrert for ekstremverider, via funksjonen ekstremVerdier. Da den fremtidige dataen er skapt gjennom en vnasklig mattematisk prediktiv modell anser vi at om noen ekstremverdier har sluppet gjennom prosessen og utgjevningen meterologisk institutt har tatt i bruk er de nok verdt å beholde. Vi har også lagt inn automatisk rettende kode for formateringsfeil.

5) Om Funksjonene:
- Funksjonen datafiltrering leser inn værdata fra en CSV-fil, konverterer tidskolonnen til riktig datoformat, sørger for at numeriske kolonner har riktig datatype (float), og fyller inn eventuelle manglende verdier med kolonnegjennomsnittet. Dette sikrer at datasettet er strukturert og klart for videre analyse.
- Funksjonen ekstremVerdier fjerner unormale eller ekstreme verdier i datasettet ved å filtrere temperaturer utenfor området -50 til 50 grader Celsius og vindhastigheter utenfor området 0 til 115 m/s. Dette bidrar til å sikre at dataene er realistiske og pålitelige for videre analyse.
- Funksjonen manglendeData håndterer manglende verdier i datasettet ved å bruke forskjellige metoder, avhengig av hva som er valgt:
    - "mean": Fyller inn manglende verdier med gjennomsnittet for den aktuelle kolonnen.
    - "median": Fyller inn med medianverdien for kolonnen.
    - "zero": Fyller inn med 0 for manglende verdier.





#
### Innhold i prosjekt
- [Informasjon om mapper](/README.md)
- [Mappe 1](/src/Mappe%201/README.md)
- [Mappe 2](/src/Mappe%202/README.md)




 
