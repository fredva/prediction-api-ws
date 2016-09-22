# Introduksjon til Google Prediction API

## Oppsett

- Logg inn på [console.cloud.google.com](http://console.cloud.google.com)
- Opprett et prosjekt
- _Enable and manage APIs_
  - Enable API
  - Google Cloud APIs
  - Prediction API
- Vi skal bruke API Explorer, og trenger derfor ikke opprette credentials
- Opprett en bucket på Cloud Storage (bruk default settings)

## Oppgave 1 – Regresjon

Meteorologisk institutt lar deg laste ned [værdata](eklima.met.no) av ulike typer. Jeg har laget et datasett som inneholder døgnmiddeltemperaturen hver dag de siste ti år for fire målestasjoner i Norge.

Datasettet finner du på https://storage.googleapis.com/ml-intro.appspot.com/temperatures.txt.

### Format
Datasettet er på følgende format:  
`temperatur,breddegrad,datoordinal`.

Utsnitt:

```
-2.0,68.9968,57
-4.8,68.9968,58
-23.0,68.9968,63
-24.1,68.9968,64
```
Kolonne 0 er døgnmiddeltemperaturen for én dag.  
Kolonne 1 er breddegraden til målestasjonen.  
Kolonne 2 er nummeret på dagen i året. 15. april er 105, 2. juni er 153, etc. (Se [Wikipedia](https://en.wikipedia.org/wiki/Ordinal_date#Table))

#### Stasjoner
- 59.9423: Blindern
- 57.9826: Lindesnes
- 63.4596: Værnes
- 68.9968: Kautokeino

#### Kode
Originalfila fra MET, og scriptet for å konvertere den til et format som er kompatibelt med Prediction API, ligger i `data/temperatures`.

### Tren modell og test den

- Last opp fila i en bucket i Cloud Storage
- Gå til [APIs Explorer](https://developers.google.com/apis-explorer/) og finn Prediction API
- Kall `prediction.trainedmodels.insert` med `id` og `storageLocation` for å opprette modellen.
- Kall `prediction.trainedmodels.get` med `id` for å se status på treningen.
- Når den er ferdig trent, kall `prediction.trainedmodels.predict` for å gjøre spørringer/prediksjoner.

## Oppgave 2 – Klassifisering

Google har laget et [enkelt datasett med merkede språkprøver](https://cloud.google.com/prediction/docs/language_id.txt).

Gjenta stegene fra forrige oppgave på dettte datasettet også.

## Fri lek

Finn deg et datasett, eller lag ditt eget. Noen kilder:

- [Meteorologisk institutt](eklima.met.no)
- [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/)
- [Kaggle](https://www.kaggle.com)
- [mldata.org](http://mldata.org/repository/data/)
- [deeplearning.net](http://deeplearning.net/datasets/)
