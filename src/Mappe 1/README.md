
# 🌍 Mappe 1: Datainnsamling og forberedelse
I den første mappen i prosjektet var formålet å sette opp et utviklingsmiljø, samle inn data og behandle og analysere den. Gruppen har brukt værdata fra de følgende plassene for å analysere de historiske dataene:


#
### Innhold 
Gruppen har valgt å dele alle oppgavene i to deler, da analysen gjennomføres med to ulike datasett: historiske data og fremtidsrettet data. Begge datasettene er hentet fra Yr.no og analyseres separat. Oppgavene og implementeringen er dokumentert i følgende filer: 
- [Testing av utviklingsmiljø](../Mappe%201/utviklingsmiljø.ipynb)
- [Databehandling av historisk data](../Mappe%201/data_behandling_fremtid.ipynb)
- [Databehandling av fremtidsrettet data](../Mappe%201/data_behandling_fremtid.ipynb)
- [CSV tabel - Oslo](../../data/Oslo.csv)
- [CSV tabel - Tromsø](../../data/Tromsø.csv)
- [CSV tabel - Stryn](../../data/Stryn.csv)

#
### Oppgave 1
Oppgave 1 av mappen var å sette opp et utviklingsmiljø. Det ble gjort i filen under.
- [Testing av utviklingsmiljø](../Mappe%201/utviklingsmiljø.ipynb)



#
### Oppgave 2 - Datainnsamling

1) På internett finnes det en stor mengde brukbare kilder på relevant data for værmeldinger. Gruppen har valgt å bruke værdata fra [Yr.no](https://hjelp.yr.no/hc/no/articles/206550539-Om-Yr) for å løse alle oppgavene i prosjektet. Yr.no drives i samarbeid mellom NRK og Meteorologisk institutt, og anses som en pålitelig datakilde ettersom begge aktørene er statlige institusjoner. 

2) For valg av dataformat, gav Yr.no mulighet for å velge mellom ulike formater for nedlastning av data. Det var mulig å brke blant annet JSON-filer, CSV-filer og XML-filer.For den historiske dataen ble CSV-filer benyttet, ettersom dette formatet var lett tilgjengelig fra Yr og enkelt å integrere med Pandas.
For fremtidsrettet data ble Yr sitt API benyttet. Dataen ble hentet i JSON-format da dette formatet er strukturert og enkelt å anvende i Python. I tillegg var gruppen kjent med dictonery fra tidligere kurs. 

3) APIen, i fremtidsrettet data, henter ned en JSON-fil på spesifiserte lengde- og breddegrader (som kan endres i en link) fra meterologisk institutt sin nettside. Den tillater oss å kjøre programmet med oppdatert forecasts data hver gang programmet kjøres for spesifike steder, noe som gir enorm fleksibilitet. De ble hentet ned dato-tidsgruppe, temperatur, nedbørsmengde og vindhastighet fra dataen. 

 
#
### Oppgave 3 - Databehandling
1) For å håndtere manglende verdier, benyttet vi fillna() i Pandas. I de fleste tilfeller ble gjennomsnittet brukt som erstatning, men for den historiske dataen testet vi også med median og 0 som alternativer.

Vi har brukt flere forskjellige metoder for å håndtere manglende verdier i verdissettet. Ettersom vi har forventet noe manglende data er dette noe vi har skånet oss mot i større grad. Både den historiske og fremtidige dataen blir behandlet med fillna for å identifisere og erstatte manglende data. I begge filene bruker vi gjennomsnittet for å erstatte den manglende verdien, men i den historiske dataen har vi også satt opp mulighet for å erstatte den med 0 eller medianen. Den historiske dataen er blitt gitt flere muligheter, da datasettet for å skape disse er større. Grunnen til det er at om en tar gjennomsnittsdataen, selv fra samme tidspunkt andre dager, bliir det vanskelig å gjenskape rimelig data. Været endrer seg mye fra dag til dag, noe som gjør det vanskelig. I fremtiden kunne vi eventuelt sett på å lage analysere for å finne en rimelig graf for temperaturendring på tvers av et døgn, for så å sette den over de nærmeste datapunktene. Vi kunne også sett på historisk værdata for samme tidsperiode i tidligere år. Derimot hadde det blitt komplekst, og vi amngler den relevante datamengden, så metodene vi for nå har tatt i bruk er gode nok for en tilnæring. 

Vi har brukt list comprehentions for å hente ut og analysere temperaturdata (datasettet vi fokuserer mest på) i både fremtidig og historisk analyse. Historisk sett brukte vi det hovedsakelig for å hente ut og filtrere dataen tidlig i koden. Fremtidig sett brukte vi det veldig lignende, men uttrykket på en nogenlunde annerledes metode. Et sterkt punkt for list comprehentions er å hente ut og analysere data, noe vi fro sterk nytte av. 

I forhold til vanlig Pandas tillater Pandas SQL håndtering med mer SQL orientert språk. Pandas SQL tillater også mer fleksibelitet og alternativer ved datahåndteringen, i tilloegg til at koden blir mer intuitiv å skrive. Kodens leslighet gjelder spesielt når en ønsker å jobbe inn flere kriterier samtidig. For eksempel blir det at vi henter ut middelvind over 5 i verdi gjort mer leslig og oversiktelig enn i vanlig pandas. 

De to hovedproblemene datasett pleier å inkludere er manglende verdier, og uteliggende verdier. Slik var situasjonen for våre datasett også. Vi har i begge datasettene filtrert for manglende verdier via den tidligere nevnte fillna. I historisk databehandling har vi også filtrert for ekstremverider, via funksjonen ekstremVerdier. Da den fremtidige dataen er skapt gjennom en vnasklig mattematisk prediktiv modell anser vi at om noen ekstremverdier har sluppet gjennom prosessen og utgjevningen meterologisk institutt har tatt i bruk er de nok verdt å beholde. Vi har også lagt inn automatisk rettende kode for formateringsfeil.




 
