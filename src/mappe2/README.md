
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
- [Refleksjonsnotat](/docs/Refleksjonsnotat.pdf)

Tilhørende test filer:
- [Test av Historisk_data_visualisering](/tests/test_historiskDataVisualisering.py)
- [Test av prediktiv_analyse](/tests/test_prediktivAnalyse.py)
- [Test av current_visualization](/tests/test_fremtidDataVisualisering.py)

#
### Oppgave 4 - Dataanalyse
1)
Vi valgte å ta i bruk standardmetodene numpy.mean(), .median() og .std() for å beregne gjennomsnitt, median, og standardavvik. Vi tok i bruk disse metodene fordi vi har brukt dem tidligere, og de er lette å ta i bruk med tanke på hvordan vi har håndtert dataen så langt. Pandas har liknende formler, med blant annet fordelene at de ignorerer mangler i datasettet, men med tanke på databehandlingen som er blitt gjennomført trengte vi ikke å ta i bruk noen av disse fordelene. Å finne disse statistiske målene bidrar i seg selv til en grunnleggende analyse av dataen. De er også grunnleggende for de flest mer avanserte statistisk data-analyser. 

2)
For å implementere enda en relevant type statisk analyse kunne vi ha gjennomført en prediktiv analyse basert på MSE (mean_squared_error) og R^2 (determinasjons koeffisient). De verktøyene er mest interessante da de er lett å ta i bruk i Python, og vi har erfaring med dem fra samtlige Excel TLOG fag, samt statistikk. For å gjennomføre analysen ville vi først ha identifisert hvilke variabler den skulle gjennomføres på, og delt opp dataen på disse punktene i trening og test data. Deretter ville vi brukt lineær regresjon på treningsdataen for å skaffe et prediktivt datagrunnlag. Deretter ville vi ha ansett analysens nøyaktighetsgrad med MSE og R^2. 

3) 
Dersom skjevhet finnes i datanen kommer det av naturlige fenomen. Skjevhet trenger ikke være resultat av feil eller mangler i datasettet, og når en analyserer et såpass komplekst system som vær vil resultatene nok ikke vise til en helt speilet distribusjon. For å håndtere dette vil jeg bruke statistiske metoder som normalisering eller tidsserieanalyse for å korrigere for naturlige variasjoner. Påliteligheten i analysen vil sikres gjennom kryssvalidering og sammenligning med uavhengige datakilder.

4) 
For å presentere analysen kan man bruke tabeller eller grafer. I [data_visulisering_historisk](/src/mappe2/data_visulisering_historisk.ipynb), oppgave 4, ble dataene visualisert i en tabell og grafer, for fremtidige data brukte vi også en lignende struktur. Ferdig analyserte data bør alltid presenteres på en måte som er enkel å forstå. Grafer egner seg godt for å vise data over tid, mens små tabeller gjør det enklere å finne spesifikke, utregnede verdier. Vi vekslet mellom grafer og tabeller for å sikre lesbarhet og gi kontekst der det var nødvendig. Når dataene har flere dimensjoner, bør grafer nesten alltid brukes for å tydeliggjøre sammenhenger mellom datapunkter.


#
### Oppgave 5 - Visualisering
1) 
For Temperaturutvikling, Luftfuktighet og vindhastighet tok vi i bruk linjediagram, mens vi tok i bruk et spredningsdiagram for korrelasjonsdiagrammet mellom nedbør og luftfuktighet. Linjediagram ville tillate oss å vise til en utvikling over tid, og vil gjøre det lett å se temperaturutvikling og sesongsvarasjoner. Spredningsdiagrammet har liknende fordeler, men lar oss også se korrelasjon og mønstre. 

2) 
Begge tillater oppbyggelse av grafer etter egne verdier. Vi brukte for eksempel sns.lineplot og plt.grid, med tilhørende beskrivende kodesnutter for å spesifisere grafutsene. Under def plot_fuktighet brukte vi også begge i kombinasjon for å lage selve plottet med seaborn, for så å videre legge til infromasjon og printe via matplotlib. Viktigs er vel plt.show for å faktisk printe selv grafen. 

3) 
Som nevnt under tidligere oppgaver i mappe 1 håndterer vi manglende data ved med en rekke metoder. Disse inkluderer blant annet moving average og liknende metoder, vi tar i bruk forskjellige metoder forskjellige steder i mappen ettersom alle har distinkte fordeler og ulemper. Av den grunn kan vi "tette hull" med relativt riktig infromasjon. Grafene vil derimot ikke være like informative som om vi hadde hatt den manglende dataen. 

4) 
Vi tar i bruk Plotly i for å lage en interaktiv graf som viser Historisk og prediktiv nedbør i samme tidsperiode. Å lage en plotly graf er litt mer avansert enn å lage en matlib eller seaborn graf, da den har interaktive funksjoner. Interaktiviteten man får ved å bruke Plotly tillater brukeren å undersøke dataen nærmere uten å ta i bruk kode selv. Den kan også tillate zooming, hover informasjon og endring av hva slags data som vises om en har flere datasett som følger samme akse. For et stegvis forklaring på koden se innlagte kommentarer under def predict_and_plot_nedbør_bar. 

5) 
Vi synes vi klart og effektivt formidler dataen vi har å presentere gjennom de grafene vi har lagd. Om en skulle sett på videre arbeid kunne vi ha sammenkjørt farger for samme data på tvers av grafene, for eksempel bare brukt grønn for luftfuktighet, da det kunne gitt en bedre samlet leserforståelse. 

### Oppgave 6 - Prediktiv analyse 
1) 
[data_visualisering_historisk](/src/mappe2/data_visulisering_historisk.ipynb)
Se oppgave 6 under data_visualisering_historisk. Som en kan se bruker vi forskjellige graftyper for å representere forskjellige typer data. Når en viss graftype er tatt i bruk er det fordi vi mener dataen presenteres på best mulig måte gjennom den graftypen. For eksempel vil en kunne se data presentert på samme måte i både linjediagram og scatterplot-diagram. Av den grunn har vi tatt i bruk de nødvendige diagramtypene der de er mest naturlige. I noen tilfeller tillater det mindre variasjon enn ønsket, men det har kommet på bekostning av leselighet, og der med brukervennlighet. 

2) 
[data_visualisering_historisk](/src/mappe2/data_visulisering_historisk.ipynb)
Se oppgave 6 under data_visualisering_historisk. Grafene våre viser en variasjon som kan refere til dag/natt syklus i temperatur, og gir en høyestemålig på 13-14 grader på dagtid og et lavmål på 4-6 grader på nattestid i perioden 27/5-3/6. Disse tallene faller relativt nærme de presentert av yr.no for samme periode. Det er noen problemer i hvor drastiske svingningene er, men over en ukes-perioder virker dataene mer tilstrekkelige. Vi tenker temperaturutviklingen i Oslo er god fra opplevelsesperspektiv. Derimot vil en også måtte ta i betraktning at vi henter data fra blindern, da potensielt fra et boligfelt i en storby. Av den grunn vil temperatursvingninger være redusert grunnet den store mengden lekkende varme fra menneskelig aktivitet og de ombringenede husstandene. 

3) 
Vi henter data fra meget politelige kilder og tar i bruk funksjoner med evne til å oppdage hull i datasettet. Vi har ikke opplevd dette problemet enda grunnet disse faktorene. Av den grunn forsøkte vi å skape en graf hvor vi med vilje har fjernet deler av datasettet. Vi beste oss for å ikke beholde denne da den ikke ga noe særlig. Selv med 20% av datapunktene tilfeldig fjernet var prognosen knapt påvirket. Vi antar at grunnen til det er den relativte tettheten til de eksisterende datapunktene. En reduksjon på 20% fra tilnærmet 9000 datapunkter vil ha lav sjanse til å lede til større utslag ved å fjerne en relativt større andel av de lave eller høye uteliggerne relativt til et datasett på 20 punkt. Et mer konsentrert utslag over en viss periode, typ å fjerne 20 dager med informasjon, hadde liknende resultat. 

4) 
Vi ser at linjegrafer i deres simplisitet kombinert med plotly sin interaktivitet som ledet til best informasjonsformidling. Ettersom linjegrafene er simple er det lett å lese av data fra dem og forstå hva de viser. Når en måler vær måler en også kontinuerlig, noe denne graftypen representerer godt. Ved å introdusere plotly sin interaktivitet vil man da også legge til en funksjon som tillater økt datamengde per graf. Siden grafen vil kunne endres i henhold til brukerens ønsker kan en også lettere se sammenhenger mellom datapunktene en ønsker å undersøke. Vi har diskutert saken med flere av vår medstudenter, og de har sagt seg vel enige. enkelte mente at scatterplot kunne ta seg bedre ut, men grunnet at de ikke er kontinuerlig mener vi linjegrafer er best for det ønskede formålet. 

### Oppgave 7 - Reflesjonsnotat
- [Refleksjonsnotat PDF](/docs/Refleksjonsnotat.pdf)


#
### Innhold i prosjekt
- [Informasjon om mapper](/README.md)
- [Mappe 1](/src/Mappe%201/README.md)
- [Mappe 2](/src/Mappe%202/README.md)
- [Informasjon om tester](/tests/README.md)



