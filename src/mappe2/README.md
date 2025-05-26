
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
1) 
For Temperaturutvikling, Luftfuktighet og vindhastighet tok vi i bruk linjediagram, mens vi tok i bruk et spredningsdiagram for korrelasjonsdiagrammet mellom nedbør og luftfuktighet. Linjedagram ville tillate oss å vise til en utvikling over tid, og vil gjøre det lett å se temperaturutvikling og sesongsvarasjoner. Spredningsdiagrammet har liknende fordeler, men lar oss også se korrelasjon og mønstre. 

2) 
Begge tillater oppbyggelse av grafer etter egne verdier. Vi brukte for eksempel sns.lineplot og plt.grid, med tilhørende beskrivende kodesnutter for å spesifisere grafutsene. Under def plot_fuktighet brukte vi også begge i kombinasjon for å lage selve plottet med seaborn, for så å videre legge til infromasjon og printe via matplotlib. Viktigs er vel plt.show for å faktisk printe selv grafen. 

3) 
Som nevnt under tidligere oppgaver i mappe 1 håndterer vi manglende data ved med en rekke metoder. Disse inkluderer blant annet moving average og liknende metoder, vi tar i bruk forskjellige metoder forskjellige steder i mappen ettersom alle har distinkte fordeler og ulemper. Av den grunn kan vi "tette hull" med relativt riktig infromasjon. Grafene vil derimot ikke være like informative som om vi hadde hatt den manglende dataen. 

4) 

Vi tar i bruk Plotly i for å lage en interaktiv graf som viser Historisk og prediktiv nedbør i samme tidsperiode. Å lage en plotly graf er litt mer avansert enn å lage en matlib eller seaborn graf, da den har interaktive funksjoner. Interaktiviteten man får ved å bruke Plotly tillater brukeren å undersøke dataen nærmere uten å ta i bruk kode selv. Den kan også tillate zooming, hover informasjon og endring av hva slags data som vises om en har flere datasett som følger samme akse. For et stegvis forklaring på koden se innlagte kommentarer under def predict_and_plot_nedbør_bar. 

5) 
Vi synes vi klart og effektivt formidler dataen vi har å presentere gjennom de grafene vi har lagd. Om en skulle sett på videre arbeid kunne vi ha sammenkjørt fargeer for samme data på tvers av grafene, for eksempel bare brukt grønn for luftfuktighet, da det kunne gitt en bedre samlet leserforståelse. 

### Oppgave 6 - Prediktiv analyse 
1) 
Se oppgave 6 under FrostAPI.ipynb. ?????

2) 
Se oppgave 6 under FrostAPI.ipynb.

3) Demonstrer hvordan manglende data håndteres i visualiseringene. Lag en graf som viser hvordan manglende verdier påvirker datatrender, og diskuter hvordan dette kan påvirke tolkningen av dataene.

????????

4) Skriv en kort evaluering av de utviklede visualiseringene. Diskuter hvilke visualiseringer som var mest effektive for å formidle informasjon, og hvorfor. Reflekter over tilbakemeldinger fra medstudenter eller veileder.

TBD

### Oppgave 7 - Reflesjonsnotat
- [Refleksjonsnotat PDF](filepath)


#
### Innhold i prosjekt
- [Informasjon om mapper](/README.md)
- [Mappe 1](/src/Mappe%201/README.md)
- [Mappe 2](/src/Mappe%202/README.md)
- [Informasjon om tester](/tests/README.md)



