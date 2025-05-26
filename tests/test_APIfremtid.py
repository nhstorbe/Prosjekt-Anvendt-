import unittest
from unittest.mock import patch
import os
import sys

project_root = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, project_root)

import src.mappe1.API_fremtid as API


class TestMakeWeatherJSON(unittest.TestCase):

    # Vi bruker mock funksjoner for å slippe å kalle på ekte API-er
    # @patch erstatter API-ene med en falsk versjon
    @patch("src.mappe1.API_fremtid.requests.get")
    def test_make_weatherJSON_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "properties": {
                "timeseries": []
            }
        }

        result = API.make_weatherJSON("London")
        self.assertIn("properties", result)
        self.assertIn("timeseries", result["properties"])


    # Tester et sted som ikke finnes i locations dictonery -> skal retunrere "ikke funnet"
    def test_make_weatherJSON_invalid_place(self):
        with self.assertRaises(Exception) as context:
            API.make_weatherJSON("Gløshaugen")
        self.assertIn("ikke funnet", str(context.exception))


    # Simmulerer en error med koden 404, for å sjekke om koden tar det opp
    @patch("src.mappe1.API_fremtid.requests.get")
    def test_make_weatherJSON_bad_status_code(self, mock_get):
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception) as context:
            API.make_weatherJSON("Paris")
        self.assertIn("API call failed", str(context.exception))


    # Lager en tom JSON fil
    @patch("src.mappe1.API_fremtid.requests.get")
    def test_make_weatherJSON_empty_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}

        with self.assertRaises(Exception) as context:
            API.make_weatherJSON("Tokyo")
        self.assertIn("Ingen data", str(context.exception))



if __name__ == "__main__":
    unittest.main()
