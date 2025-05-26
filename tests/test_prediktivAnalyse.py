import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import sys

project_root = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, project_root)

import src.mappe2.PrediktivAnalyse as PA


class WeatherModelTest(unittest.TestCase):
    def setUp(self):
        # Lager et lite datasett for testing (24 timer)
        base_time = datetime(2024, 5, 1)
        self.df = pd.DataFrame({
            "date": [base_time + timedelta(hours=i) for i in range(24)],
            "air_temperature": np.random.normal(10, 2, 24),
            "relative_humidity": np.random.uniform(40, 90, 24),
            "wind_speed": np.random.uniform(0, 10, 24)
        })
        self.df_missing = self.df.copy()
        self.df_missing.loc[5:7, "air_temperature"] = None  # Introduser mangler

    def test_prepare_weather_data_clean(self): # Tester at ren data forblir intakt 
        clean_df = PA.prepare_weather_data(self.df)
        self.assertIn("hour", clean_df.columns)
        self.assertIn("month", clean_df.columns)
        self.assertIn("day_of_year", clean_df.columns)
        self.assertFalse(clean_df.isna().any().any())

    def test_prepare_weather_data_missing(self): # Tester at manglende data blir interpolert
        processed_df = PA.prepare_weather_data(self.df_missing)
        self.assertFalse(processed_df["air_temperature"].isna().any())

    def test_train_regression_model_valid(self): # Tester at regresjonsmodell kan trenes og gir resultater
        df_ready = PA.prepare_weather_data(self.df)
        model, X_train, X_test, y_train, y_test, y_pred = PA.train_regression_model(df_ready)
        self.assertEqual(len(y_pred), len(X_test))
        self.assertGreaterEqual(len(X_test), 1)

    def test_train_regression_model_missing_column(self): # Tester at feilmelding kommer hvis nødvendige kolonner mangler
        df_invalid = self.df.drop(columns=["wind_speed"])
        df_invalid = PA.prepare_weather_data(df_invalid)
        with self.assertRaises(KeyError):
            PA.train_regression_model(df_invalid)

    def test_predict_future_conditions_structure(self): # Tester at fremtidsdatasettet har riktig struktur
            df_ready = PA.prepare_weather_data(self.df)
            model, *_ = PA.train_regression_model(df_ready)
            future_start = datetime(2024, 6, 1)
            future_df = PA.predict_future_conditions(model, future_start, days=3, df_historical=df_ready)

            # Sjekk at vi får forventet antall rader: 3 dager * 24 timer = 72
            self.assertEqual(len(future_df), 72)

            # Sjekk at kolonnen for predikert temperatur finnes
            self.assertIn("predicted_temperature", future_df.columns)

            # Sjekk at relativ luftfuktighet er innenfor 0–100
            self.assertTrue((future_df["relative_humidity"] >= 0).all(), "Luftfuktighet har verdier under 0.")
            self.assertTrue((future_df["relative_humidity"] <= 100).all(), "Luftfuktighet har verdier over 100.")

            # Sjekk at vindhastighet er ikke-negativ
            self.assertTrue((future_df["wind_speed"] >= 0).all(), "Vindhastighet har negative verdier.")

            self.assertFalse(future_df.isna().any().any(), "Fremtidsdatasettet inneholder NaN-verdier.")



    def test_predict_future_conditions_no_historical(self): # Tester at funksjonen fortsatt fungerer hvis ingen historiske data er gitt
        df_ready = PA.prepare_weather_data(self.df)
        model, *_ = PA.train_regression_model(df_ready)
        future_df = PA.predict_future_conditions(model, datetime(2024, 6, 1), days=1)
        self.assertAlmostEqual(future_df["relative_humidity"].mean(), 70, delta=10)
        self.assertAlmostEqual(future_df["wind_speed"].mean(), 5, delta=5)


if __name__ == "__main__":
    unittest.main()


