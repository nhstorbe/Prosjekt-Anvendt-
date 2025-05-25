import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


client_id = "aff7c34e-993d-4132-81bc-1df3e81d7868" 
end_date = datetime.today().date()
start_date = end_date - timedelta(days=365)  
station_id = "SN18700"

def fetch_hourly_data(client_id, station_id, start_date, end_date):
    url = "https://frost.met.no/observations/v0.jsonld"
    elements = ["air_temperature", "relative_humidity", "wind_speed"]
    
    params = {
        "sources": station_id,
        "elements": ",".join(elements),
        "referencetime": f"{start_date}/{end_date}",
        "timeresolutions": "PT1H",
        "timeoffsets": "default"
    }
    try:
        response = requests.get(url, params=params, auth=(client_id, ""), timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Feil ved henting av timesdata: {e}")
        return pd.DataFrame()

    data = response.json().get("data", [])
    records = {}

    for item in data:
        time = pd.to_datetime(item["referenceTime"]).tz_localize(None)
        if time not in records:
            records[time] = {"date": time}

        for obs in item["observations"]:
            element_id = obs["elementId"]
            value = obs.get("value", None)
            records[time][element_id] = value

    df = pd.DataFrame.from_dict(records, orient="index")
    df = df.sort_values("date").reset_index(drop=True)
    
    return df

def prepare_weather_data(df):
    """Rens og forbered timesbasert værdata for analyse og modellering."""
    df = df.copy()
    
    # Konverter 'date' til datetime og sett som indeks for interpolasjon
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")

    # Logg og fyll inn manglende verdier for hver værvariabel
    for column in df.columns:
        missing = df[column].isna().sum()
        if missing > 0:
            print(f"Manglende verdier i '{column}': {missing}")
            df[column] = df[column].interpolate(method="time")
    
    # Sett tilbake 'date' som kolonne
    df = df.reset_index()

    # Legg til tidsbaserte funksjoner
    df["hour"] = df["date"].dt.hour
    df["month"] = df["date"].dt.month
    df["day_of_year"] = df["date"].dt.dayofyear

    df = df.dropna()
    return df

df_hourly = fetch_hourly_data(client_id, station_id, start_date, end_date)
df = prepare_weather_data(df_hourly)
print(df.head())


def train_regression_model(df, target="air_temperature", features=["relative_humidity", "wind_speed", "hour", "month", "day_of_year"]):
    # Definer funksjoner (X) og målvariabel (y)
    X = df[features]
    y = df[target]
    
    # Splitt data i trenings- og testsett (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialiser og tren modellen
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Prediksjoner på testsettet
    y_pred = model.predict(X_test)
    
    # Evaluer modellens ytelse
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R² Score: {r2:.2f}")
    
    return model, X_train, X_test, y_train, y_test, y_pred

# Trener modellen
model, X_train, X_test, y_train, y_test, y_pred = train_regression_model(df)

def plot_temperature_over_time(df, X_test, y_test, y_pred):
    """Plott faktisk og predikert temperatur over tid."""
    # Koble X_test tilbake til det opprinnelige datasettet for å hente 'date'
    # Vi antar at X_test indekser er de samme som i df etter splitting
    test_indices = X_test.index
    test_dates = df.loc[test_indices, "date"]
    
    # Sørg for at test_dates, y_test og y_pred er i samme rekkefølge
    plot_df = pd.DataFrame({
        "date": test_dates,
        "actual_temperature": y_test,
        "predicted_temperature": y_pred
    }).sort_values("date")  # Sorter etter dato for å sikre riktig tidsrekkefølge
    
    # Plott
    plt.figure(figsize=(12, 6))
    plt.plot(plot_df["date"], plot_df["actual_temperature"], label="Faktisk temperatur", color="blue")
    plt.plot(plot_df["date"], plot_df["predicted_temperature"], label="Predikert temperatur", color="orange", linestyle="--")
    plt.xlabel("Dato")
    plt.ylabel("Temperatur (°C)")
    plt.title("Faktisk og predikert temperatur over tid")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Etter at jeg har trent modellen, plotter jeg resultatene
plot_temperature_over_time(df, X_test, y_test, y_pred)


def plot_temperature_over_time(df, X_test, y_test, y_pred):
    """Plott faktisk og predikert temperatur over tid, aggregert til daglig nivå."""
    # Koble X_test tilbake til det opprinnelige datasettet for å hente 'date'
    test_indices = X_test.index
    test_dates = df.loc[test_indices, "date"]
    
    # Lag en DataFrame med datoer og temperaturer
    plot_df = pd.DataFrame({
        "date": test_dates,
        "actual_temperature": y_test,
        "predicted_temperature": y_pred
    })
    
    # Aggregere til daglig nivå ved å ta gjennomsnittet per dag
    plot_df["date"] = pd.to_datetime(plot_df["date"]).dt.date  # Konverter til bare dato (fjern tid)
    plot_df = plot_df.groupby("date").mean().reset_index()
    plot_df["date"] = pd.to_datetime(plot_df["date"])  # Konverter tilbake til datetime for plotting
    
    # Plott
    plt.figure(figsize=(12, 6))
    plt.plot(plot_df["date"], plot_df["actual_temperature"], label="Faktisk temperatur", color="blue")
    plt.plot(plot_df["date"], plot_df["predicted_temperature"], label="Predikert temperatur", color="orange", linestyle="--")
    plt.xlabel("Dato")
    plt.ylabel("Temperatur (°C)")
    plt.title("Faktisk og predikert temperatur over tid (daglig gjennomsnitt)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Her er den oppdaterte funksjonen for å plotte daglig gjennomsnitt
plot_temperature_over_time(df, X_test, y_test, y_pred)


def predict_future_conditions(model, start_date, days=7, df_historical=None):
    """Prediker fremtidige miljøforhold for en gitt periode med simulert variasjon."""
    future_dates = pd.date_range(start=start_date, periods=days*24, freq="H")
    future_df = pd.DataFrame({"date": future_dates})
    
    # Legg til tidsbaserte funksjoner
    future_df["hour"] = future_df["date"].dt.hour
    future_df["month"] = future_df["date"].dt.month
    future_df["day_of_year"] = future_df["date"].dt.dayofyear
    
    # Simuler værvariabler basert på historiske mønstre
    if df_historical is not None:
        # Beregn gjennomsnitt og standardavvik for relative_humidity og wind_speed per time
        hourly_stats = df_historical.groupby(df_historical["date"].dt.hour).agg({
            "relative_humidity": ["mean", "std"],
            "wind_speed": ["mean", "std"]
        })
        
        # Legg til simulert variasjon basert på time på dagen
        future_df["relative_humidity"] = future_df["hour"].map(hourly_stats["relative_humidity"]["mean"])
        future_df["wind_speed"] = future_df["hour"].map(hourly_stats["wind_speed"]["mean"])
        
        # Legg til tilfeldig støy basert på standardavvik
        np.random.seed(42)  # For reproduserbarhet
        future_df["relative_humidity"] += np.random.normal(
            0, 
            future_df["hour"].map(hourly_stats["relative_humidity"]["std"]),
            size=len(future_df)
        )
        future_df["wind_speed"] += np.random.normal(
            0, 
            future_df["hour"].map(hourly_stats["wind_speed"]["std"]),
            size=len(future_df)
        )
        
        # Sørg for at verdiene er innenfor realistiske grenser
        future_df["relative_humidity"] = future_df["relative_humidity"].clip(0, 100)  # Fuktighet mellom 0 og 100 %
        future_df["wind_speed"] = future_df["wind_speed"].clip(0, None)  # Vindhastighet kan ikke være negativ
    else:
        # Fallback-verdier
        future_df["relative_humidity"] = 70.0
        future_df["wind_speed"] = 5.0
    
    # Velg funksjoner i riktig rekkefølge
    features = ["relative_humidity", "wind_speed", "hour", "month", "day_of_year"]
    X_future = future_df[features]
    
    # Gjør prediksjoner
    future_df["predicted_temperature"] = model.predict(X_future)
    
    return future_df

# Prediker fremtidige forhold
future_start = end_date + timedelta(days=1)
future_df = predict_future_conditions(model, future_start, days=7, df_historical=df)

# Plott fremtidige prediksjoner
plt.figure(figsize=(12, 6))
plt.plot(future_df["date"], future_df["predicted_temperature"], label="Predikert temperatur", color="blue")
plt.xlabel("Dato")
plt.ylabel("Temperatur (°C)")
plt.title("Prediksjon av temperatur for neste uke")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


