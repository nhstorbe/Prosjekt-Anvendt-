import unittest
import src.mappe2.Historisk_data as HD


class TestWeatherPlotting(unittest.TestCase):

    def setUp(self):
        # Eksempeldata
        self.valid_json = {
            "data": [
                {
                    "referenceTime": "2024-05-01T00:00:00Z",
                    "observations": [{"elementId": "mean(air_temperature P1D)", "value": 15.2}]
                },
                {
                    "referenceTime": "2024-05-02T00:00:00Z",
                    "observations": [{"elementId": "mean(air_temperature P1D)", "value": 16.3}]
                }
            ]
        }

        self.invalid_json = {"info": []}
        self.element_id = "mean(air_temperature P1D)"
        self.element_name = "Temperatur"
        self.unit = "C"

    def test_parse_weather_data_valid(self): # Tester at parsing returnerer riktig DataFrame med riktig kolonner
        df = HD.parse_weather_data(self.valid_json, self.element_id)
        self.assertFalse(df.empty)
        self.assertIn("value", df.columns)
        self.assertIn("date", df.columns)
        self.assertEqual(len(df), 2)

    def test_parse_weather_data_invalid(self): # Tester at parsing returnerer tom DataFrame hvis den blir matet med ugyldig data
        df = HD.parse_weather_data(self.invalid_json, self.element_id)
        self.assertTrue(df.empty)

    def test_plot_weather_data_runs(self): # Tester at plot-funksjonen ikke krasjer når den mates med gyldig data
        df = HD.parse_weather_data(self.valid_json, self.element_id)
        try:
            HD.plot_weather_data(df, self.element_name, "Oslo", "2024-05-01", "2024-05-02", self.unit)
        except Exception as e:
            self.fail(f"plot_weather_data krasjet: {e}")

    def test_plot_weather_Barplot_runs(self): # Tester at barplot-funksjonen ikke krasjer når den mates med gyldig data
        df = HD.parse_weather_data(self.valid_json, self.element_id)
        try:
            HD.plot_weather_Barplot(df, self.element_name, "Oslo", "2024-05-01", "2024-05-02", self.unit)
        except Exception as e:
            self.fail(f"plot_weather_Barplot krasjet: {e}")


if __name__ == "__main__":
    unittest.main()
