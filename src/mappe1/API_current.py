import pandas as pd
import pandasql as sqldf
import requests

# Breddegrad og lengdegrad er hentet fra Google Maps
locations = {
    "Stryn": (61.903901, 6.706899),
    "Longyearbyen": (78.225920, 15.625622),
    "Paris": (48.854289, 2.342042),
    "London": (51.501814, -0.140605),
    "Cape Town": (-33.922348, 18.424031),
    "New York": (40.710676, -74.006219),
    "Tokyo" : (35.681599, 139.767185)
}

# Dersom man ønsker å legge til ekstra steder, kan man gjøre det her.
def add_location(place, lat, lon):
    
    if place not in locations.keys():
        locations[place] = (lat, lon)
        print(f"{place} ble lagt til med koordinater ({lat}, {lon})")

    else:
        print(f"{place} finnes allerede i dictionary.")

    return locations

print(locations)


# Koden lager en JSON fil ut i fra koordinatene som blir puttet inn i linken.
def make_weatherJSON(place):

    if place not in locations.keys():
        raise Exception(f"{place} ikke funnet i {locations.keys()}")

    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={locations[place][0]}&lon={locations[place][1]}"
    headers = {'User-Agent': 'my-weather-app/1.0'}  #nødvendig for Yr API
    response = requests.get(url, headers=headers)
    
    
    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}")
    
    data = response.json()

    if not data:
        raise Exception("Ingen data i JSON-objekt")
    
    return data

#make_weatherJSON("Løngyearbyen") #(feilmenlding)
#make_weatherJSON("Longyearbyen")



# Rydder manglende verdier med fillna()
def clean_weather_data(place):
    data = make_weatherJSON(place)
    timeseries = data["properties"]["timeseries"]

    lst = []
    for entry in timeseries:
        time = entry["time"]
        details = entry["data"]["instant"]["details"]
        lst.append({
            "Time": time,
            "Temperature": details.get("air_temperature"),
            "Rain": entry["data"].get("next_1_hours", {}).get("details", {}).get("precipitation_amount"),
            "Wind speed": details.get("wind_speed")
        })

    
    # Lager JSON-filen om til en DataFrame (lister)
    df = pd.DataFrame(lst)

    #gjør om "Time" til datetime
    df["Time"] = pd.to_datetime(df["Time"], errors="coerce")

    #fyller inn evt. hull (NaN) med medianen
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    return df


clean_weather_data("London")


# Sjekker om det er noen hull i datasettet etterpå
def check_NaN_counter(place):
    data = clean_weather_data(place)
    missing_counts = data.isna().sum()
    
    print("Antall NaN-verdier per kolonne:")
    print(missing_counts)
    return missing_counts



# Henter ut temeraturer for de neste 24 timene
def get_temperatures_24(place):
    data = make_weatherJSON(place)
    timeseries = data["properties"]["timeseries"]
    
    temperatures = [
        (entry["time"], entry["data"]["instant"]["details"]["air_temperature"])
        for entry in timeseries[:24]
    ]
    
    return temperatures

get_temperatures_24("Paris")