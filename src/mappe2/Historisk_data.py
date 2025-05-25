import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
import plotly.express as px
from prettytable import PrettyTable
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from bokeh.palettes import Category10


client_id = "aff7c34e-993d-4132-81bc-1df3e81d7868" 
end_date = datetime.today().date()
start_date = end_date - timedelta(days=365)  
station_id = "SN18700"


def fetch_and_analyze_weather(client_id, station_id, start_date, end_date):

    elements = [
        ("mean(air_temperature P1D)", "Temperatur", "°C"),
        ("mean(relative_humidity P1D)", "Fuktighet", "%"),
        ("sum(precipitation_amount P1D)", "Nedbør", "mm"),
        ("mean(wind_speed P1D)", "Vindhastighet", "m/s"),
    ]

    results = []

    for element_id, name, unit in elements:
        # Henter dataen fra API
        url = "https://frost.met.no/observations/v0.jsonld"
        params = {
            "sources": station_id,
            "elements": element_id,
            "referencetime": f"{start_date}/{end_date}"
        }

        try:
            response = requests.get(url, params=params, auth=(client_id, ""), timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Feil ved henting av {name}: {e}")
            results.append((name, unit, "Feil", "Feil", "Feil"))
            continue

        data = response.json()
        values = []

        # Trekker ut verdier
        for obs in data.get("data", []):
            for el in obs.get("observations", []):
                if el["elementId"] == element_id and "value" in el:
                    values.append(el["value"])

        if values:
            mean_val = round(np.mean(values), 2)
            median_val = round(np.median(values), 2)
            std_val = round(np.std(values), 2)
        else:
            mean_val = median_val = std_val = "Ingen data"

        results.append((name, unit, mean_val, median_val, std_val))

    # Lager en fin tabell
    table = PrettyTable()
    table.field_names = ["Element", "Enhet", "Gjennomsnitt", "Median", "Std.avvik"]
    for row in results:
        table.add_row(row)

    print(table)

fetch_and_analyze_weather(client_id, station_id, start_date, end_date)


def fetch_weather_data(client_id, station_id, start_date, end_date, elements):
    url = "https://frost.met.no/observations/v0.jsonld"
    params = {
        "sources": station_id,
        "elements": ",".join(elements),
        "referencetime": f"{start_date}/{end_date}"
    }

    try:
        response = requests.get(url, params=params, auth=(client_id, ""), timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
        print("Response text:", response.text)
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error fetching data: {err}")
        return None

    return response.json()

def parse_weather_data(data, element_id):
    if not data or "data" not in data:
        print("No data returned from API.")
        return pd.DataFrame()

    observations = []
    for obs in data["data"]:
        for element in obs["observations"]:
            if element["elementId"] == element_id:
                observations.append({
                    "date": obs["referenceTime"],
                    "value": element["value"]
                })

    df = pd.DataFrame(observations)
    if df.empty:
        print("No data available for this element.")
        return df

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    return df

def plot_weather_data(df, element_name, station_name, start_date, end_date, unit=""):
    if df.empty:
        return

    fig = px.line(
        df,
        x="date",
        y="value",
        title=f"{element_name} – {station_name} ({start_date} til {end_date})",
        labels={"date": "Dato", "value": f"{element_name} ({unit})"},
        template="plotly_white"
    )

    fig.update_traces(
        mode="lines",
        hovertemplate="Dato: %{x|%Y-%m-%d}<br>Verdi: %{y:.1f} {unit}"
    )
    fig.update_layout(
        xaxis_title="Dato",
        yaxis_title=f"{element_name} ({unit})",
        hovermode="x unified",
        showlegend=False
    )

    fig.show(renderer="vscode") # Åpne i interactiv modus i VSCode

element_id = "mean(air_temperature P1D)"
element_name = "Gjennomsnittlig temperatur"
unit = "C"
json_data = fetch_weather_data(client_id, station_id, start_date, end_date, [element_id])
df = parse_weather_data(json_data, element_id)
plot_weather_data(df, element_name, "Oslo - Blindern", start_date, end_date, unit)

element_id = "mean(relative_humidity P1D)"
element_name = "Relativ fuktighet"
unit = "%"
json_data = fetch_weather_data(client_id, station_id, start_date, end_date, [element_id])
df = parse_weather_data(json_data, element_id)
plot_weather_data(df, element_name, "Oslo - Blindern", start_date, end_date, unit)

element_id = "mean(wind_speed P1D)"
element_name = "Vindhastighet"
unit = "m/s"
json_data = fetch_weather_data(client_id, station_id, start_date, end_date, [element_id])
df = parse_weather_data(json_data, element_id)
plot_weather_data(df, element_name, "Oslo - Blindern", start_date, end_date, unit)



element_id = "sum(precipitation_amount P1D)"
element_name = "Nedbør"
unit = "mm"

def plot_weather_Barplot(df, element_name, station_name, start_date, end_date, unit=""):
    if df.empty:
        print("Ingen data å vise.")
        return

    fig = px.bar(
        df,
        x="date",
        y="value",
        title=f"{element_name} - {station_name} ({start_date} til {end_date})",
        labels={"date": "Dato", "value": f"{element_name} ({unit})"},
        template="plotly_white"
    )

    fig.update_traces(
        hovertemplate="Dato: %{x|%Y-%m-%d}<br>Verdi: %{y:.1f} {unit}"
    )
    fig.update_layout(
        xaxis_title="Dato",
        yaxis_title=f"{element_name} ({unit})",
        hovermode="x unified",
        showlegend=False
    )

    fig.show(renderer="vscode") # Åpne i interactiv modus i VSCode

json_data = fetch_weather_data(client_id, station_id, start_date, end_date, [element_id])
df = parse_weather_data(json_data, element_id)
plot_weather_Barplot(df, element_name, "Oslo - Blindern", start_date, end_date, unit)














