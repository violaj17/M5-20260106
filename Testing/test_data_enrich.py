import unittest
import pandas as pd
from scripts.data_clean import dataEnrich

class TestDataEnrich(unittest.TestCase):

    def test_data_enrich(self):
        # Create a sample dataframe
        data = {
            'Book checkout': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-02-28']),
            'Book Returned': pd.to_datetime(['2023-01-10', '2023-02-17', '2023-03-04'])
        }
        df = pd.DataFrame(data)

        # Expected loan duration
        expected_duration = pd.Series([9, 16, 4])

        # Calculate loan duration using dataEnrich function (in days)
        result = dataEnrich(df).dt.days

        # Assert that the result matches the expected duration
        pd.testing.assert_series_equal(result, expected_duration, check_names=False)

if __name__ == "__main":
    unittest.main()

