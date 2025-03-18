import json
import os 
from pandasql import sqldf
import pandas as pd 

base_dir = os.path.dirname(os.path.abspath(__file__))  # Finner stien til 'src'
file_path = os.path.join(base_dir, "..", "data", "weather.json")

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f) # Leser inn JSON-dataene fra filen

json.dumps(data, indent=4) # Formaterer JSON-dataene for å gjøre dem lettere å lese


weather_list = [
    {"time": entry["time"], "temperature": entry["data"]["instant"]["details"]["air_temperature"]}
    for entry in data["properties"]["timeseries"]
]

df = pd.DataFrame(weather_list)  
print(df.head()) 

df_iterator = df.iterrows()

# Hente ut første rad ved hjelp av next()
index, first_row = next(df_iterator)
print("Første rad i datasettet:")
print(first_row)

# Definere SQL-spørring for å hente ut data hvor temperaturen er over 5°C
query = "SELECT * FROM df WHERE temperature < -5"
result = sqldf(query, globals())

print("Temperaturer over 5°C:")
print(result)
