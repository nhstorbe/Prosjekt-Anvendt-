
# 🌍 Mappe 1: Datainnsamling og forberedelse
I den første mappen i prosjektet var formålet å sette opp et utviklingsmiljø, samle inn data og behandle og analysere den. 

![Bilde](/resources/Bilde2.webp)
Bildet er hentet fra ([AlphaTarget](https://alphatarget.com/resources/a-primer-on-artificial-intelligence/), 2024)



#
### Innhold 
Gruppen har valgt å dele alle oppgavene i to deler, da analysen gjennomføres med to ulike datasett: historiske data og fremtidsrettet data. Begge datasettene er hentet fra Yr.no og analyseres separat. Oppgavene og implementeringen er dokumentert i følgende filer: 

Besvarelse for oppgave 1:
- [Testing av utviklingsmiljø](../Mappe%201/utviklingsmiljø.ipynb)

Besvarelse for oppgave 2 og oppgave 3:
- [Databehandling av historisk data](/src/Mappe%201/data_behandling_historisk.ipynb)
- [Databehandling av fremtidsrettet data](/src/Mappe%201/data_behandling_fremtid.ipynb)

Tilhørende CSV-filer:
- [CSV tabel - Oslo](/data/Oslo.csv)
- [CSV tabel - Tromsø](/data/Tromsø.csv)
- [CSV tabel - Stryn](/data/Stryn.csv)


#
### Oppgave 2 - Datainnsamling

1) På internett finnes det en stor mengde brukbare kilder på relevant data for værmeldinger. Gruppen har valgt å bruke værdata fra [Yr.no](https://hjelp.yr.no/hc/no/articles/206550539-Om-Yr) for å løse alle oppgavene i prosjektet. Yr.no drives i samarbeid mellom NRK og Meteorologisk institutt, og anses som en pålitelig datakilde ettersom begge aktørene er statlige institusjoner. 

2) For valg av dataformat, gav Yr.no mulighet for å velge mellom ulike formater for nedlastning av data. Det var mulig å brke blant annet JSON-filer, CSV-filer og XML-filer.For den historiske dataen ble CSV-filer benyttet, ettersom dette formatet var lett tilgjengelig fra Yr og enkelt å integrere med Pandas.
For fremtidsrettet data ble Yr sitt API benyttet. Dataen ble hentet i JSON-format da dette formatet er strukturert og enkelt å anvende i Python. I tillegg var gruppen kjent med dictonery fra tidligere kurs. 

3) APIen, i fremtidsrettet data, henter ned en JSON-fil på spesifiserte lengde- og breddegrader (som kan endres i en link) fra meterologisk institutt sin nettside. Den tillater oss å kjøre programmet med oppdatert forecasts data hver gang programmet kjøres for spesifike steder, noe som gir enorm fleksibilitet. De ble hentet ned dato-tidsgruppe, temperatur, nedbørsmengde og vindhastighet fra dataen. 

 
#
### Oppgave 3 - Databehandling
1) For å håndtere manglende verdier i datasettet, benyttet vi flere metoder. I både ["Historisk databehnadling](/src/Mappe%201/data_behandling_historisk.ipynb) og ["Fremtidig databehandling"](/src/Mappe%201/data_behandling_fremtid.ipynb) startet vi med å undersøke om det fantes hull i dataene. Til dette brukte vi funksjoner som _check_NaN_counter(place)_ og _print(df.isnull().sum())_ for å identifisere antall manglende verdier i datasettet. Når manglende verdier ble oppdaget, tok vi i bruk Pandas-funksjonen fillna(), som erstatter NaN-verdier med spesifiserte verdier. I de fleste tilfeller brukte vi median som erstatning, men i behandlingen av historiske data testet vi også med gjennomsnitt og null som alternativer. Det er viktig å være klar over at slike metoder kan introdusere unøyaktigheter. Værdata varierer betydelig fra dag til dag, og det er derfor vanskelig å erstatte manglende verdier uten å risikere å forvrenge virkeligheten. Spesielt i tilfeller med ekstreme verdier i datasettet kan gjennomsnitt være en dårlig erstatning, ettersom det er svært sensitivt for slike avvik. I slike situasjoner kan median være et bedre valg, da den er mer robust mot ekstreme verdier og gir et mer representativt bilde av datasettet.


2) Vi har brukt list comprehentions for å hente ut og analysere temperaturdata (datasettet vi fokuserer mest på) i både fremtidig og historisk analyse. Historisk sett brukte vi det hovedsakelig for å hente ut og filtrere dataen tidlig i koden. Fremtidig sett brukte vi det veldig lignende, men uttrykket på en nogenlunde annerledes metode. Et sterkt punkt for list comprehentions er å hente ut og analysere data, noe vi fikk sterk nytte av. 

3) I forhold til vanlig Pandas tillater Pandas SQL håndtering med mer SQL orientert språk. Pandas SQL tillater også mer fleksibelitet og alternativer ved datahåndteringen, i tilloegg til at koden blir mer intuitiv å skrive. Kodens leslighet gjelder spesielt når en ønsker å jobbe inn flere kriterier samtidig. For eksempel blir det at vi henter ut middelvind over 5 i verdi gjort mer leslig og oversiktelig enn i vanlig pandas. 

4) De to hovedproblemene datasett pleier å inkludere er manglende verdier, og uteliggende verdier. Slik var situasjonen for våre datasett også. Vi har i begge datasettene filtrert for manglende verdier via den tidligere nevnte fillna. I historisk databehandling har vi også filtrert for ekstremverider, via funksjonen ekstremVerdier. Da den fremtidige dataen er skapt gjennom en vnasklig mattematisk prediktiv modell anser vi at om noen ekstremverdier har sluppet gjennom prosessen og utgjevningen meterologisk institutt har tatt i bruk er de nok verdt å beholde. Vi har også lagt inn automatisk rettende kode for formateringsfeil.


#
### Innhold i prosjekt
- [Informasjon om mapper](/README.md)
- [Mappe 1](/src/Mappe%201/README.md)
- [Mappe 2](/src/Mappe%202/README.md)




 
