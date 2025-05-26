import unittest

# Filsti til funksjonen som skal testes
from src.mappe1.API_current import make_weatherJSON

class TestMakeWeatherJSON(unittest.TestCase):

    def test_make_weatherJSON_success(self):
        result = make_weatherJSON("London") # Ligger i locations
        self.assertIn("properties", result)
        self.assertEqual(result["geometry"]["coordinates"][0], 15.6256) # Sjekker om koordiantene er like


    def test_make_weatherJSON_invalid_place(self):
        with self.assertRaises(Exception) as context:
            make_weatherJSON("Place with no name")  # Ikke i locations
        self.assertIn("ikke funnet", str(context.exception))
        

if __name__ == '__main__':
    unittest.main()







