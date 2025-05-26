import unittest
from unittest.mock import patch, Mock
import pandas as pd
from datetime import datetime

from mappe2.current_visualization import get_weatherDataframe, get_statistics, correlation


fake_json = {
    "properties": {
        "timeseries": [
            {
                "time": "2025-05-25T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_temperature": 15.0,
                            "relative_humidity": 55.0,
                            "wind_speed": 3.5,
                            "precipitation_amount": 0.2
                        }
                    }
                }
            },
            {
                "time": "2025-05-25T13:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_temperature": 16.0,
                            "relative_humidity": 50.0,
                            "wind_speed": 4.0,
                            "precipitation_amount": 0.0
                        }
                    }
                }
            }
        ]
    }
}

class TestCurrentVisualization(unittest.TestCase):

    @patch('mappe2.current_visualization.make_weatherJSON')
    def test_get_weatherDataframe(self, mock_make_weatherJSON):
        mock_make_weatherJSON.return_value = fake_json
        df = get_weatherDataframe("London")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("Tid", df.columns)
        self.assertEqual(len(df), 2)

    @patch('mappe2.current_visualization.make_weatherJSON')
    @patch('matplotlib.pyplot.show')  # Forhindre visning av plott
    def test_get_statistics(self, mock_show, mock_make_weatherJSON):
        mock_make_weatherJSON.return_value = fake_json
        result = get_statistics("London", "Temperatur (C°)")
        self.assertIn("Gjennomsnitt", result)

    @patch('mappe2.current_visualization.make_weatherJSON')
    @patch('matplotlib.pyplot.show')  # Forhindre visning av plott
    def test_correlation(self, mock_show, mock_make_weatherJSON):
        mock_make_weatherJSON.return_value = fake_json
        result = correlation("London", "Temperatur (C°)", "Fuktighet (%)")
        self.assertIn("Korrelasjon", result)

    @patch('mappe2.current_visualization.make_weatherJSON')
    def test_invalid_entry_statistics(self, mock_make_weatherJSON):
        mock_make_weatherJSON.return_value = fake_json
        with self.assertRaises(ValueError):
            get_statistics("London", "FeilEntry")

    @patch('mappe2.current_visualization.make_weatherJSON')
    def test_invalid_entry_correlation(self, mock_make_weatherJSON):
        mock_make_weatherJSON.return_value = fake_json
        with self.assertRaises(Exception):
            correlation("London", "Feil1", "Feil2")


if __name__ == '__main__':
    unittest.main()