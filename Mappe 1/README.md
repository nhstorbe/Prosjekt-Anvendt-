
# 🌍 Miljødataanalyseapplikasjon

Dette prosjektet analyserer værdata fra datakilden Yr, ved hjelp av meteorologiske API-er. Programmet henter, prosesserer og analyserer værinformasjon i Stryn ved hjelp av Python.


![bilde](resources/IMG_7762.JPG)


## Innhold

- [Oppgave 1: Sett opp utviklingsmiljø](#Oppgave1)
- [Oppgave 2: Datainnsamling](#Oppgave2)
- [Oppgave 3: Databehandling](#Oppgave3)

---

## 🛠️ Oppgave 1 Utviklings miljø 

Spørsmål for øvingstime:
- Hvordan fungerer er PEP 8?
- Hva er det som ønskes å oppnå ut ifra oppgave 2?
- Samme spørsmål for oppgave 3?
- Hvordan vil en vise at vi har tatt i bruk list comprehensions, iterators og pandassqlfd?
- Hvordan skal vi utforske og forstå dataens struktur og innhold?
- Hva for noe svar ønskes det?
- Skal spørsmålene nederst på hver oppgavetekst besvares i relevant kodefil, samlet pdf, eller i det hele tatt? 
- Når får vi tilbakemelding på mappe 1? Med tanke på oppfølgningsfeil 

hente dataen 
filtrere dataen, pandas null 
søke opp hvordan filtrere store mengder vær data pandas.null 
gjøre det generelt mer clean 
gjøre det mer finere 



[Test at utviklingsmiljøet fungerer](src/utviklingsmiljø.ipynb)

## ✉️ Datainnsamling og databehandling av historisk værdata

[CSV fil med værdata i Stryn fra 1 Mars 2024 til 1 Mars 2025](data/table.csv)
- I tillegg til en csv fil som tar for seg historisk data har vi også tatt i bruk en API fra Meteoroliske institutt der vi samler inn sanntidsdata hver time for de neste 10 dagene. 

## 🤖 Datainnsamling og databehandling av fremtidig værdata












##Datakilder

Gjennom internett kan en finne en stor mengde brukbare kilder på relevant data til dette prosjektet. Av den grunn trenger en å spisse seg inn mot den mest relevante. Det viktigste kriteriet i relasjon til kildevalg for oss er kildeautoritet. Av den grunn så vi først på offentlige, og statlige kilder. Vi så av den grunn på [yr](https://www.yr.no), [NOAA](https://www.ncei.noaa.gov/cdo-web/datasets) og [Meterologiask institutt](https://www.met.no/en/free-meteorological-data). Vi valgte i første omgang disse nettstedene da de enten er internasjonalt annerkjente organisasjoner, eller statlige meterologiske institusjoner. Vi følte av den grunn at alle tre var pålitelige kilder med god autoritet og datatilgang. Da dataene fra sidene enten er hentet fra eller brukes til aktiv forskning har vi også god tiltro til kvaliteten på dataen. Vi valgte å bruke yr grunnet at de tok i bruk .json format, og at å få tak i dataen fra deres nettside var lettest. 

Vi vlagte .json format av flere grunner. De grunnleggende formene en ofte tar i bruk for prosjekter av denne typen virket å være .csv, .json og .xml. Da vi ikke har mye kunnskap til .xml, og formatet har en mulig kompleksitet som går langt forbi våre krav, på god bekostning av filstørrelse. .csv(comma seperated values)-filer er den simpleste typen data-fil som er vanlig å ta i bruk. En .csv-fil inneholder linjer med data separert med "," og er derfor svært leselige for mennesker, og veldig lett å sette inn i excel-filer. .json(Javascript Object Notation)-filer er tekstbaserte, simple og effektive. .json er ikke like effektive størrelsesmessig som .csv, men nært..json er bygd opp av arrays og objekter. En ser ofte objekt etter objekt som inneholder lik data om tilsvarende situasjon over tid, f.eks 

{
    "temp": "30*C",
    "wind": "5m/s",
    "wind.direction": "NE"
}

.json er også ganske leselig for mennesker, og relativt lett å håndtere datamessig. Formatet er også flexibelt og bredt kompatibelt med forskjellige formler. Vi valgte .json fordi det ga økt flexibilitet og kompatibilitet i forhold til .csv, med minimal økninig i filstørrelse og leselighet. 

Vi har brukt en API støttet .json fil nettopp fordi vi da alltid vil ha filen automatisk oppdatert.  
