
# 🌍 Mappe 2: Dataanalyse og visualisering
I den andre mappen i prosjektet var formålet å visualisere dataen, beregne statistiske verdier og lage en prediktiv  analyse.

![Bilde](/resources/maskinlæring.jpg)
Bildet er hentet fra ([NTNU](https://www.ntnu.no/eit/ttk4852-utg%C3%85r), n.a.)


#
### Innhold 
Gruppen har valgt å dele alle oppgavene i to deler, da analysen gjennomføres med to ulike datasett: historiske data og fremtidsrettet data. Begge datasettene er hentet fra Yr.no og analyseres separat. Oppgavene og implementeringen er dokumentert i følgende filer: 

Besvarelse for oppgave 4, oppgave 5 og oppgave 6:
- [Datavisualisering av historisk data](/src/Mappe%202/data_visualisering_historisk.ipynb)
- [Datavisualisering av fremtidsrettet data](/src/Mappe%202/data_visualisering_fremtid.ipynb)

Besvarelse for oppgave 7:
- [Refleksjonsnotat](filepath)

Tilhørende CSV-filer:
- [CSV tabel - Oslo](/data/Oslo.csv)
- [CSV tabel - Tromsø](/data/Tromsø.csv)
- [CSV tabel - Stryn](/data/Stryn.csv)



#
### Oppgave 4 - Dataanalyse
1)
Vi valgte å ta i bruk standardmetodene numpy.mean(), .median() og .std() for å beregne gejnnomsnitt, median, og standardavvik. Vi tok i bruk disse metodene fordi vi har brukt dem tidligere, og de er lette å ta i bruk med tanke på hvordan vi har håndtert dataen sålangt. Pandas har liknende formler, med blant annet fordelene at de ignorerer mangler i datasettet, men med tanke på databehandlingen som er blitt gjennomført trengte vi ikke å ta i bruk noen av disse fordelene. Å finne disse statistiske målene bidrar i seg selv til en grunnleggende analyse av dataen. De er også grunnleggende for de flest mer avanserte statistisk data-analyser. 

2)
For å imlementere enda en relevant type statisk analyse kunne vi ha gjennomført en predektiv analyse basert på MSE (mean_squared_error) og R^2 (determinasjonskoefficient). De verktøyene er mest interresante da de er lett å ta i bruk i phython, og vi har erfaring med dem fra samtlige excel TLOG fag, samt statistikk. For å gjennomføre analysen ville vi først ha identifiser hvilke variabler den skulle gjennomføres på, og delt opp dataen på disse punktene i trening og test data. Deretter ville vi brukt lineær regresjon på treningsdataen for å skaffe et prediktivt datagrunnlag. Deretter ville vi ha ansett analysens nøyaktighetsgrad med MSE og R^2. 

3) Hvordan planlegger du å håndtere eventuelle skjevheter i dataene under analysen, og hvilke metoder vil du bruke for å sikre at analysen er pålitelig?
Dersom skjevhet finnes i datanen kommer det av naturlige fenomen. Skjevhet trenger ikke være resultat av feil eller mangler i datasettet, og når en analyserer et såpass komplekst system som vær vil resultatene nok ikke vise til en helt speilet distribusjon. ????????????????

4) 
For å vise frem analysen kan man bruke blant annet tabeller eller grafer. I FrostAPI oppgave 4 brukte visualiseres datene i en tabell, mens med de fremtidige dataene brukte vi først tabell og så graf. Data i ferdig analysert form burde alltid presenteres for lettest forståelse. Grafer vil tillate lettere presentasjon av data over en tidsperiode, samt små tabeller tillater en å lettere finne relevant utregnet data. Vi valgt grafer og tabeller om hverandre for leselighet, og for å skape en kontekst der nødvendig. Er det mer enn en dimensjon til dataene som presenteres burde den derimot ta i bruk graf nesten uavhengig for å vise til mulige samhold mellom datapunkter. 
 
#
### Oppgave 5 - Visualisering
1) Hvilke spesifikke typer visualiseringer planlegger du å lage for å representere eksempelvis endringer i luftkvalitet og temperaturdata, og hvorfor valgte du disse?


2) Hvordan kan Matplotlib og Seaborn brukes til å forbedre forståelsen av de analyserte dataene, og hvilke funksjoner i disse bibliotekene vil være mest nyttige?


3) Hvordan vil du håndtere og visualisere manglende data i grafene dine for å sikre at de fortsatt er informative?


4) Kan du beskrive prosessen for å lage interaktive visualiseringer med Widgets, Plotly eller Bokeh, og hvilke fordeler dette kan gi i forhold til statiske visualiseringer?


5) Hvordan vil du evaluere effektiviteten av visualiseringene dine i å formidle de viktigste funnene fra dataanalysen til et bredere publikum?


### Oppgave 6 - Prediktiv analyse 
1) Lag minst tre forskjellige typer visualiseringer (f.eks. linjediagrammer, søylediagrammer og scatterplots) for å representere endringer i eksempelvis luftkvalitet og temperaturdata over tid. Forklar valget av visualiseringstype for hver graf.


2) Implementer visualiseringer ved hjelp av Matplotlib og Seaborn. Inkluder tilpassede akser, titler, og fargepaletter for å forbedre lesbarheten og estetikk.


3) Demonstrer hvordan manglende data håndteres i visualiseringene. Lag en graf som viser hvordan manglende verdier påvirker datatrender, og diskuter hvordan dette kan påvirke tolkningen av dataene.


4) Skriv en kort evaluering av de utviklede visualiseringene. Diskuter hvilke visualiseringer som var mest effektive for å formidle informasjon, og hvorfor. Reflekter over tilbakemeldinger fra medstudenter eller veileder.


### Oppgave 7 - Reflesjonsnotat
- [Refleksjonsnotat PDF](filepath)


#
### Innhold i prosjekt
- [Informasjon om mapper](/README.md)
- [Mappe 1](/src/Mappe%201/README.md)
- [Mappe 2](/src/Mappe%202/README.md)



