import requests
import os
import pandas as pd
from datetime import date, timedelta, datetime
from pandasql import sqldf

# Input parameterene
client_id = "aff7c34e-993d-4132-81bc-1df3e81d7868" 
station_id = "SN18700"  # Blindern, Oslo
elements = ["air_temperature", "relative_humidity", "wind_speed", "precipitation_amount"]
start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
end_date = datetime.now().strftime("%Y-%m-%d")


def visualiserer_data(client_id):
    sources_url = "https://frost.met.no/sources/v0.jsonld"
    try:
        response = requests.get(sources_url, auth=(client_id, ""), timeout=10)
        response.raise_for_status()
        sources_data = response.json()

    except requests.exceptions.RequestException as err:
        print(f"Feil ved innhenting av stasjon data: {err}")
        return None

    stations = []
    for source in sources_data["data"]:
        if "name" in source and "id" in source:
            stations.append({
                "id": source["id"],
                "name": source["name"],
                "country": source.get("country", "")
            })
    
    stations_df = pd.DataFrame(stations)
    norway_stations = stations_df[stations_df["country"] == "Norge"]
    
    if norway_stations.empty:
        print("No Norwegian stations found.")
        return None
    
    return norway_stations

# Kall funksjonen og skriv ut resultatet
result = visualiserer_data(client_id)
if result is not None:
    print(result)


def get_station_id_by_name(client_id, search_name):
    stations = visualiserer_data(client_id)
    if stations is None or stations.empty:
        print("Fant ingen stasjoner.")
        return None

    # Søker etter stasjoner med navn som inneholder søketeksten
    mask = stations["name"].str.lower().str.contains(search_name.lower())
    matches = stations[mask]

    if matches.empty:
        print(f"Ingen stasjoner matchet {search_name}")
        return None

    if len(matches) == 1:
        station_id = matches.iloc[0]["id"]
        print(f"Fant stasjon: {matches.iloc[0]['name']} → ID: {station_id}")
        
    else:
        print("Flere mulige stasjoner funnet:")
        print(matches[["id", "name"]])
        # Velger første som default så noe blir gjort
        station_id = matches.iloc[0]["id"]
        print(f"Velger den første: {station_id}")

get_station_id_by_name(client_id, "Oslo - Blindern")

# Henter stasjons-ID for Oslo - Blindern
def fetch_hourly_weather_to_csv(client_id, station_id, station_name, start_date, end_date, filename="../../data/weather_data.csv"):
    elements = {
        "Lufttemperatur": "air_temperature",
        "Relativ luftfuktighet": "relative_humidity",
        "Middelvind": "wind_speed",
        # "Nedbør": "sum(precipitation_amount P1H)"  ← fjernet denne, dette blir forklart i README.md
    }

    base_url = "https://frost.met.no/observations/v0.jsonld"
    full_data = {}

    for label, element in elements.items():
        params = {
            "sources": station_id,
            "elements": element,
            "referencetime": f"{start_date}/{end_date}",
            "timeoffsets": "default",
            "timeresolutions": "PT1H"
        }

        try:
            response = requests.get(base_url, params=params, auth=(client_id, ""), timeout=30)
            response.raise_for_status()
            data = response.json().get("data", [])
            print(f"Hentet {label}: {len(data)} observasjoner")
            if not data:
                print(f"Ingen data for {label} i perioden {start_date} til {end_date}")
        except requests.exceptions.RequestException as e:
            print(f"Feil ved henting av {label.lower()}: {e}")
            print(f"Responsstatus: {response.status_code if response else 'Ingen respons'}")
            continue

        for entry in data:
            time = pd.to_datetime(entry["referenceTime"]).tz_localize(None)
            value = entry["observations"][0]["value"]

            if time not in full_data:
                full_data[time] = {}
            full_data[time][label] = value

    # Konverterer til DataFrame
    records = []
    for time, values in sorted(full_data.items()):
        record = {
            "Navn": station_name,
            "Stasjon": station_id,
            "Tid (t)": time.strftime("%d.%m.%Y %H:00"),
            "Lufttemperatur (C)": values.get("Lufttemperatur", ""),
            "Middelvind (m/s)": values.get("Middelvind", ""),
            "Relativ luftfuktighet (g/m³)": values.get("Relativ luftfuktighet", "")
            # "Nedbør (mm)": values.get("Nedbør", "")  ← fjernet her også
        }
        records.append(record)

    df = pd.DataFrame(records)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, sep=";", index=False, encoding="utf-8")
    print(f"Data lagret i: {filename}")

fetch_hourly_weather_to_csv(client_id, station_id, "Oslo - Blindern", start_date, end_date)

# Henter ut varme dager med list comprehension
def hent_varme_dager(df, temperaturgrense):
    
    varme_dager = [(rad["Tid (t)"], rad["Lufttemperatur (C)"]) 
                   for i, rad in df.iterrows() 
                   if rad["Lufttemperatur (C)"] > temperaturgrense]
    return varme_dager

df = pd.read_csv("../../data/weather_data.csv", sep=";", encoding="utf-8")
varme_dager = hent_varme_dager(df,temperaturgrense=27)
print(varme_dager[:10]) 


# Itterer gjennom DataFrame og skriver ut de første 5 observasjonene
def vis_observasjoner(df, antall=5):
    print(f"Viser de første {antall+1} observasjonene:\n")
    for index, row in df.iterrows():
        print(f"Stasjon: {row['Stasjon']}, Tid: {row['Tid (t)']}, Relativ Fuktighet: {row['Relativ luftfuktighet (g/m³)']}(g/m³)")
        if index == antall:
            break

df = pd.read_csv("../../data/weather_data.csv", sep=";", encoding="utf-8")
vis_observasjoner(df, antall=5)

# Pandasql for å hente ut data
def sterk_vind(df, grense):
    
    df = df.rename(columns={
        "Middelvind (m/s)": "middelvind",
        "Tid (t)": "tid"
    })
    vind = f"SELECT tid, middelvind FROM df WHERE middelvind > {grense}"
    result = sqldf(vind)
    return result

df = pd.read_csv("../../data/weather_data.csv", sep=";", encoding="utf-8")
sterk_vind(df, grense=10)


# Henter ut data fra CSV og filtrerer
def datafiltrering(filepath):
    try:
        df = pd.read_csv(filepath, delimiter=";", encoding="utf-8")

        df["Tid (t)"] = pd.to_datetime(df["Tid (t)"], format="%d.%m.%Y %H:%M", errors="coerce")

        ønskede_kolonner = ["Nedbør (mm)", "Lufttemperatur (C)", "Middelvind (m/s)", "Relativ luftfuktighet (g/m³)"]
        eksisterende_kolonner = [col for col in ønskede_kolonner if col in df.columns]

        if eksisterende_kolonner:
            df[eksisterende_kolonner] = df[eksisterende_kolonner].astype(float)
            df.fillna(df.mean(numeric_only=True), inplace=True)
        else:
            print("Ingen av de numeriske kolonnene finnes i datasettet.")

    except FileNotFoundError:
        print(f"Filen {filepath} ble ikke funnet.")
        return None

    return df

filepath = "../../data/weather_data.csv"
df_cleaned = datafiltrering(filepath)
print(df_cleaned.head())


# Fjern ekstreme verdier
def ekstremVerdier(df):
    df = df[(df["Lufttemperatur (C)"].between(-50, 50))] 
    df = df[(df["Middelvind (m/s)"].between(0, 115))] 
    
    return df

df_cleaned = ekstremVerdier(df_cleaned)

# Tar i bruk 3 metoder for å fylle inn manglende data
def manglendeData(df, method="mean"):

    if method == "mean":
        df.fillna(df.mean(numeric_only=True), inplace=True)
    elif method == "median":
        df.fillna(df.median(numeric_only=True), inplace=True)
    elif method == "zero":
        df.fillna(0, inplace=True)
    
    return df

df_cleaned = manglendeData(df_cleaned, method="mean")

