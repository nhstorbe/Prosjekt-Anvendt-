import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import norm

import src.mappe1.API_fremtid as API


# Listen gir oversikt over hvilke instanser (weather_entry) som er gydlige for JSON-filen
value_weather_entry = ["Temperatur (C°)", "Fuktighet (%)" ,"Vindhastighet (m/s)", "Nedbør (mm)"]


# Lager Dataframes av dataen
def get_weatherDataframe(place):
    data = API.make_weatherJSON(place)

    timeseries = data["properties"]["timeseries"]

    weather_lst = [
        {
            "Tid": entry["time"],
            value_weather_entry[0]: entry["data"]["instant"]["details"].get("air_temperature"),
            value_weather_entry[1]: entry["data"]["instant"]["details"].get("relative_humidity"),
            value_weather_entry[2]: entry["data"]["instant"]["details"].get("wind_speed"), 
            value_weather_entry[3]: entry["data"]["instant"]["details"].get("precipitation_amount")
            
        }
        for entry in timeseries
    ]

    df = pd.DataFrame(weather_lst)
    df["Tid"] = pd.to_datetime(df["Tid"])
    df.fillna(0, inplace=True)  #erstatter NaN-verdier med 0
    return df

#get_weatherDataframe("New York")



def get_statistics(place, weather_entry):
    df = pd.DataFrame(get_weatherDataframe(place))

    #sjekker om entry er i datasettet
    if weather_entry not in df.columns:
        raise ValueError(f"{weather_entry} finnes ikke i datasettet.")


    #beregner ønskede verdier
    average = df[weather_entry].mean()  
    median = df[weather_entry].median()  
    std = df[weather_entry].std() 
    string = f"Gjennomsnitt: {round(average, 3)}, Median: {round(median, 3)}, Standardavvik: {round(std, 3)}"


    #plotter histogram og normalfordeling
    plt.figure(figsize=(15,6))
    sns.histplot(df[weather_entry], color='b', stat="density", bins=30)
    xmin, xmax = plt.xlim()  
    x = np.linspace(xmin, xmax, 100) #baserer diagrammet på største og minste verdi i datasettet
    p = norm.pdf(x, average, std) 
    plt.plot(x, p, 'r', label="Normalfordeling")
    plt.xlabel(weather_entry)
    plt.ylabel("Antall instanser (tetthet)")
    plt.title(f"Normalfordeling av '{weather_entry}' for {place}")
    plt.grid()
    plt.legend()
    plt.show() 

    return string


#get_statistics(locations["New York"][0], "temp") #(feilmelding)
#get_statistics("New York", value_weather_entry[1])



def correlation(place, weather_entry1, weather_entry2):
    df = get_weatherDataframe(place)


    #sjekker om entry er en instans i filen
    if weather_entry1 not in df.columns or weather_entry2 not in df.columns:
        raise Exception("Instans(ene) finnes ikke i datasettet")
    

    #regner ut korrelasjon
    correlation = df[weather_entry1].corr(df[weather_entry2])
    string = f"Korrelasjon mellom '{weather_entry1}' og '{weather_entry2}' er ({round(correlation,3)}) for {place}"


    plt.figure(figsize=(15,6))
    sns.regplot(x=df[weather_entry1], y=df[weather_entry2])
    plt.xlabel(weather_entry1)
    plt.ylabel(weather_entry2)
    plt.title(string)
    plt.grid()
    plt.show()

    return string


#print(correlation("Cape Town", value_weather_entry[0], value_weather_entry[1]))



#lager grafer som beskriver været over tid for en gitt plass
def plot_weather(place, weather_entry):
    df = get_weatherDataframe(place)

    #sjekker om entry er en instans i filen
    if weather_entry not in df.columns:
        raise Exception("Instans(ene) finnes ikke i datasettet")

    plt.figure(figsize=(15, 6))   
    sns.lineplot(data=df, x="Tid", y=weather_entry) 
    plt.xlabel("Tid")
    plt.ylabel(weather_entry)
    plt.title(f"Yr.no - Mål for '{weather_entry}' over tid for '{place}'")
    plt.grid()
    plt.show()

#print(locations.keys())
plot_weather("London", value_weather_entry[0])
plot_weather("Cape Town", value_weather_entry[1])
plot_weather("New York", value_weather_entry[2])
plot_weather("Paris", value_weather_entry[3])

