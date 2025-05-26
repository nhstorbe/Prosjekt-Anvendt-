import unittest
from unittest.mock import patch
import pandas as pd
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Forhindrer at plt.show() åpner vindu under test

import os
import sys

project_root = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, project_root)

import src.mappe2.current_visualization as fun

# lager en Mock() JSON som gjør at vi ikke er avhengig av API-dataen
mock_api_response = {
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

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_get_weatherDataframe(self, mock_api):
        mock_api.return_value = mock_api_response
        df = fun.get_weatherDataframe("Oslo")

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), ["Tid"] + fun.value_weather_entry)
        self.assertEqual(len(df), 2)
        self.assertAlmostEqual(df["Temperatur (C°)"].iloc[0], 15.0)

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_get_statistics_valid_entry(self, mock_api):
        mock_api.return_value = mock_api_response
        result = fun.get_statistics("Oslo", "Temperatur (C°)")
        self.assertIn("Gjennomsnitt", result)
        self.assertIn("Standardavvik", result)

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_get_statistics_invalid_entry(self, mock_api):
        mock_api.return_value = mock_api_response
        with self.assertRaises(ValueError):
            fun.get_statistics("Oslo", "Ugyldig måling")

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_correlation_valid(self, mock_api):
        mock_api.return_value = mock_api_response
        result = fun.correlation("Oslo", "Temperatur (C°)", "Fuktighet (%)")
        self.assertIn("Korrelasjon mellom", result)

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_correlation_invalid_entry(self, mock_api):
        mock_api.return_value = mock_api_response
        with self.assertRaises(Exception):
            fun.correlation("Oslo", "Temp", "Fuktighet (%)")

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_plot_weather_valid(self, mock_api):
        mock_api.return_value = mock_api_response
        try:
            fun.plot_weather("Oslo", "Temperatur (C°)")
        except Exception:
            self.fail("plot_weather() raised Exception unexpectedly!")

    @patch('src.mappe1.API_fremtid.make_weatherJSON')
    def test_plot_weather_invalid_entry(self, mock_api):
        mock_api.return_value = mock_api_response
        with self.assertRaises(Exception):
            fun.plot_weather("Oslo", "Ugyldig")

if __name__ == '__main__':
    unittest.main()
