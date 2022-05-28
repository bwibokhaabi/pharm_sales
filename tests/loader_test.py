import unittest
from unittest import result
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.data_loader import load_df_from_csv, load_df_from_excel, optimize_df

data = {'float_values': [5.28, 2.48], 'int_values': [1, 2], 'str_values': ['daisy','okacha']}
df = pd.DataFrame(data)

class TestCases(unittest.TestCase):
    def test_test_data_availability(self):
        df.to_csv('test.csv')
        self.assertTrue('test.csv' in os.listdir())

    def test_load_df_from_csv(self):
        """
        Test that it retunrs the average of a given list
        """
        df.to_csv('test.csv')
        result = load_df_from_csv('test.csv')
        data = optimize_df(df)
        self.assertEqual(result.info(), data.info())

   


if __name__ == '__main__':
    unittest.main()

