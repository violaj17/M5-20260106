import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from scripts.data_clean import enrich_dateDuration

# Test for enrich_dateDuration function
class TestEnrichDateDuration(unittest.TestCase):
    def test_enrich_dateDuration(self):
        # Create a sample dataframe
        data = {
            'Book checkout': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-02-28']),
            'Book Returned': pd.to_datetime(['2023-01-10', '2023-01-20', '2023-03-04'])
        }
        df = pd.DataFrame(data)

        # Expected date_delta values
        expected_deltas = ([9, -12, 4])

        # Calculate date_delta values using enrich_dateDuration function
        result = enrich_dateDuration(colA='Book checkout', colB='Book Returned', df=df)

        # Assert that the result matches the expected deltas
        self.assertListEqual(result['date_delta'].tolist(), expected_deltas)

        
if __name__ == "__main__":
    unittest.main()

