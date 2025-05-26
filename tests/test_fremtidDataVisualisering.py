import unittest
from unittest.mock import patch
import pandas as pd

import src.mappe2.current_visualization as fun

# Lager en falsk JSON som gjør at vi ikke er avhengig av API-dataen
fake_api = {
    "properties": {
        "timeseries": [
            {
                "time": "2024-05-25T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_temperature": 15.0,
                            "relative_humidity": 70.0,
                            "wind_speed": 5.0,
                            "precipitation_amount": 0.2
                        }
                    }
                }
            },
            {
                "time": "2024-05-25T13:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_temperature": 17.0,
                            "relative_humidity": 65.0,
                            "wind_speed": 4.5,
                            "precipitation_amount": 0.0
                        }
                    }
                }
            }
        ]
    }
}


class TestCurrentVisualization(unittest.TestCase):

    # Sjekker om funksjonen fungerer som forventet med fake_api
    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_get_weatherDataframe(self, mock_api):
        mock_api.return_value = fake_api
        df = fun.get_weatherDataframe("Oslo")

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), ["Tid"] + fun.value_weather_entry)
        self.assertEqual(len(df), 2)


    # Tester for å sjekke de statistiske målene
    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_get_statistics_valid_entry(self, mock_api):
        mock_api.return_value = fake_api
        result = fun.get_statistics("Oslo", "Temperatur (C°)")
        self.assertIn("Gjennomsnitt", result)
        self.assertIn("Standardavvik", result)

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_get_statistics_invalid_entry(self, mock_api):
        mock_api.return_value = fake_api
        with self.assertRaises(ValueError):
            fun.get_statistics("Oslo", "Ugyldig måling")


    # Sjekker at korrelasjonene er som forventet
    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_correlation_valid(self, mock_api):
        mock_api.return_value = fake_api
        result = fun.correlation("Oslo", "Temperatur (C°)", "Fuktighet (%)")
        self.assertIn("Korrelasjon mellom", result)

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_correlation_invalid_entry(self, mock_api):
        mock_api.return_value = fake_api
        with self.assertRaises(Exception):
            fun.correlation("Oslo", "Temp", "Fuktighet (%)")



if __name__ == '__main__':
    unittest.main()
