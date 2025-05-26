import unittest
import pandas as pd
from io import StringIO
import os
import sys

project_root = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, project_root)

import src.mappe1.API_historisk as API

class TestAPI(unittest.TestCase):

    def setUp(self): #Lager en enkel test-DataFrame som vi kan bruke i flere tester
        self.test_data = pd.DataFrame({
            "Tid (t)": ["01.01.2025 14:00", "01.01.2025 15:00"],
            "Lufttemperatur (C)": [28, 22],
            "Middelvind (m/s)": [12, 5],
            "Relativ luftfuktighet (g/m³)": [60, 65]
        })

    def test_hent_varme_dager_positive(self): #Skal finne én varme dag over 27 grader
        result = API.hent_varme_dager(self.test_data, temperaturgrense=27)
        self.assertEqual(len(result), 1)

    def test_hent_varme_dager_negative(self): #Skal ikke finne noen varme dager over 30 grader
        result = API.hent_varme_dager(self.test_data, temperaturgrense=30)
        self.assertEqual(len(result), 0)


    def test_sterk_vind_positive(self): #Skal finne én observasjon med middelvind over 10 m/s
        result = API.sterk_vind(self.test_data, grense=10)
        self.assertEqual(len(result), 1)

    def test_sterk_vind_negative(self): #Skal ikke finne noen observasjoner med middelvind over 20 m/s
        result = API.sterk_vind(self.test_data, grense=20)
        self.assertTrue(result.empty)

    def test_datafiltrering_positive(self): #Tester at vi kan lese en CSV-fil og at den ikke er tom
        csv_text = StringIO("""Tid (t);Lufttemperatur (C);Middelvind (m/s);Relativ luftfuktighet (g/m³)
01.01.2025 14:00;20;5;60""")
        df = pd.read_csv(csv_text, sep=";", encoding="utf-8")
        df.to_csv("test_weather.csv", sep=";", index=False)
        result = API.datafiltrering("test_weather.csv")
        self.assertFalse(result.empty)

    def test_datafiltrering_negative(self): #Tester at vi får None når filen ikke finnes
        result = API.datafiltrering("ikke_eksisterende.csv")
        self.assertIsNone(result)

    def test_ekstremVerdier_positive(self): #Tester at alle verdier er normale og beholder de dersom de er innenfor grensen
        """Test: Alle verdier er normale → behold alle"""
        result = API.ekstremVerdier(self.test_data)
        self.assertEqual(len(result), 2)

    def test_ekstremVerdier_negative(self): #Tester om verdiene er ekstreme og fjerner de
        df = pd.DataFrame({
            "Lufttemperatur (C)": [100],
            "Middelvind (m/s)": [200]
        })
        result = API.ekstremVerdier(df)
        self.assertEqual(len(result), 0)

    def test_manglendeData_mean(self): #Tester at vi kan fylle inn NaN med gjennomsnitt
        df = pd.DataFrame({
            "Lufttemperatur (C)": [None, 20],
            "Middelvind (m/s)": [5, None]
        })
        df_filled = API.manglendeData(df.copy(), method="mean")
        self.assertFalse(df_filled.isnull().values.any())

    def test_manglendeData_zero(self): #Tester at vi kan fylle inn NaN med 0
        df = pd.DataFrame({
            "Lufttemperatur (C)": [None],
            "Middelvind (m/s)": [None]
        })
        df_filled = API.manglendeData(df.copy(), method="zero")
        self.assertTrue((df_filled == 0).all().all())


if __name__ == "__main__":
    unittest.main()


