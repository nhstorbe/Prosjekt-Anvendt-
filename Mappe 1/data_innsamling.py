import json

with open("værdata_Stryn.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Se på dataens struktur
print(json.dumps(data, indent=4))  # Formaterer JSON-dataene for å gjøre dem lettere å lese


import os
print(os.getcwd())  # Sjekker hvilken mappe Python kjører fra
