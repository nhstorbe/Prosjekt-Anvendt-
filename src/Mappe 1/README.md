
# 🌍 Mappe 1: Datainnsamling og forberedelse
I den første mappen i prosjektet var formålet å sette opp et utviklingsmiljø, samle inn data og behandle og analysere den. 

Gruppen bestemt seg for å dele alle oppgavene i to deler, da alle oppgavene blir gjort to ganger med to ulike datasett. Det på  der både historisk data og fremtidsrettet data blir analysert, da dette var tilgjengelig på Yr sine nettsider. Oppgavene blir beskrevet og gjennomført i hver sin respektive fil. 


#
### Innhold i mappen
- [Testing av utviklingsmiljø](../Mappe%201/utviklingsmiljø.ipynb)
- [Databehandling av historisk data](../Mappe%201/data_behandling_fremtid.ipynb)
- [Databehandling av fremtidsrettet data](../Mappe%201/data_behandling_fremtid.ipynb)

#
### ✉️ Datainnsamling og databehandling av historisk værdata

- [CSV fil med værdata i Stryn fra 1 Mars 2024 til 1 Mars 2025](data/table.csv)
- [Datainnsamling og databehandling av historisk værdata](src/data_behandling_historisk.ipynb)
- I tillegg til en csv fil som tar for seg historisk data har vi også tatt i bruk en API fra Meteoroliske institutt der vi samler inn sanntidsdata hver time for de neste 10 dagene. 

Gjennom internett kan en finne en stor mengde brukbare kilder på relevant data til dette prosjektet. Av den grunn trenger en å spisse seg inn mot den mest relevante. Det viktigste kriteriet i relasjon til kildevalg for oss er kildeautoritet. Av den grunn så vi først på offentlige, og statlige kilder. Vi så av den grunn på [yr](https://www.yr.no), [NOAA](https://www.ncei.noaa.gov/cdo-web/datasets) og [Meterologiask institutt](https://www.met.no/en/free-meteorological-data). Vi valgte i første omgang disse nettstedene da de enten er internasjonalt annerkjente organisasjoner, eller statlige meterologiske institusjoner. Vi følte av den grunn at alle tre var pålitelige kilder med god autoritet og datatilgang. Da dataene fra sidene enten er hentet fra eller brukes til aktiv forskning har vi også god tiltro til kvaliteten på dataen. Vi valgte å bruke meterologisk institutt for fremtidsrettet dataanalyse grunnet at de tok i bruk .json format, og at å få tak i dataen fra deres nettside var lettest. For historisk ananlyse, hvor vi ikke trengte å holde dataen oppdatert, men heller ønsekt en større mengde tilgjengelig, valgte vi å ta i bruk .csv fra yr. Hvorfor utdyper vi under. 

Vi vlagte .json format for analyse av fremtidig data av flere grunner. De grunnleggende formene en ofte tar i bruk for prosjekter av denne typen virket å være .csv, .json og .xml. Vi har ikke mye kunnskap til .xml, og formatet har en mulig kompleksitet som går langt forbi våre krav, på god bekostning av filstørrelse. .csv(comma seperated values)-filer er den simpleste typen data-fil som er vanlig å ta i bruk. En .csv-fil inneholder linjer med data separert med "," og er derfor svært leselige for mennesker, og veldig lett å sette inn i excel-filer. .json(Javascript Object Notation)-filer er tekstbaserte, simple og effektive. .json er ikke like effektive størrelsesmessig som .csv, men er ganske nært..json er bygd opp av arrays og objekter. En ser ofte objekt etter objekt som inneholder lik data om tilsvarende situasjon over tid, f.eks 

{
    "temp": "30*C",
    "wind": "5m/s",
    "wind.direction": "NE"
}

.json er også ganske leselig for mennesker, og relativt lett å håndtere datamessig. Formatet er også flexibelt og bredt kompatibelt med forskjellige formler. Vi valgte .json fordi det ga økt flexibilitet og kompatibilitet i forhold til .csv, med minimal økninig i filstørrelse og leselighet. .json var også lettere å støtte med API-er for å holde dataen konstant oppdatert, noe vi må for å holde dataen konstant fremtidsrettet. Vi har brukt en API støttet .json fil nettopp fordi vi da alltid vil ha filen automatisk oppdatert. 

For den historiske dataen ga det mening å ta i bruk en .csv fil fordi den er mindre i størrelse per datapunkt enn en .json, og vi ikke trengte en den API-integrert. .csv filer kan API-integreres, men de fleste bruker for tiden .json for proseser og API-er på nett, noe som hadde gjort dette vanskligere å finne. 

Vi har brukt en API som henter ned en .json på spesifiserte lengde- og breddegrader fra meterologisk institutt sin nettside. Den tillater oss å kjøre programmet med oppdatert forecasts data hver gang programmet kjøres. Vi henter ned tidspunkt, temperatur, regnmengde og vindhastighet. Siden vi har de samme datapunktene i vår historiske data kan vi bruke alle for analyser. Siden vi har tilsvarende historisk data kan vi gjennomføre analyser for å både se om vi sier oss enige med våre analytiske verktøy, men også for å kunne bruke historisk data for å hjelpe å erstatte manglende data i .json datasettet. 

## 🤖 Datainnsamling og databehandling av fremtidig værdata

[Datainnsamling og databehandling av fremtidig værdata](src/data_behandling_fremtid.ipynb)

Vi har brukt flere forskjellige metoder for å håndtere manglende verdier i verdissettet. Ettersom vi har forventet noe manglende data er dette noe vi har skånet oss mot i større grad. Både den historiske og fremtidige dataen blir behandlet med fillna for å identifisere og erstatte manglende data. I begge filene bruker vi gjennomsnittet for å erstatte den manglende verdien, men i den historiske dataen har vi også satt opp mulighet for å erstatte den med 0 eller medianen. Den historiske dataen er blitt gitt flere muligheter, da datasettet for å skape disse er større. Grunnen til det er at om en tar gjennomsnittsdataen, selv fra samme tidspunkt andre dager, bliir det vanskelig å gjenskape rimelig data. Været endrer seg mye fra dag til dag, noe som gjør det vanskelig. I fremtiden kunne vi eventuelt sett på å lage analysere for å finne en rimelig graf for temperaturendring på tvers av et døgn, for så å sette den over de nærmeste datapunktene. Vi kunne også sett på historisk værdata for samme tidsperiode i tidligere år. Derimot hadde det blitt komplekst, og vi amngler den relevante datamengden, så metodene vi for nå har tatt i bruk er gode nok for en tilnæring. 

Vi har brukt list comprehentions for å hente ut og analysere temperaturdata (datasettet vi fokuserer mest på) i både fremtidig og historisk analyse. Historisk sett brukte vi det hovedsakelig for å hente ut og filtrere dataen tidlig i koden. Fremtidig sett brukte vi det veldig lignende, men uttrykket på en nogenlunde annerledes metode. Et sterkt punkt for list comprehentions er å hente ut og analysere data, noe vi fro sterk nytte av. 

I forhold til vanlig Pandas tillater Pandas SQL håndtering med mer SQL orientert språk. Pandas SQL tillater også mer fleksibelitet og alternativer ved datahåndteringen, i tilloegg til at koden blir mer intuitiv å skrive. Kodens leslighet gjelder spesielt når en ønsker å jobbe inn flere kriterier samtidig. For eksempel blir det at vi henter ut middelvind over 5 i verdi gjort mer leslig og oversiktelig enn i vanlig pandas. 

De to hovedproblemene datasett pleier å inkludere er manglende verdier, og uteliggende verdier. Slik var situasjonen for våre datasett også. Vi har i begge datasettene filtrert for manglende verdier via den tidligere nevnte fillna. I historisk databehandling har vi også filtrert for ekstremverider, via funksjonen ekstremVerdier. Da den fremtidige dataen er skapt gjennom en vnasklig mattematisk prediktiv modell anser vi at om noen ekstremverdier har sluppet gjennom prosessen og utgjevningen meterologisk institutt har tatt i bruk er de nok verdt å beholde. Vi har også lagt inn automatisk rettende kode for formateringsfeil. 
