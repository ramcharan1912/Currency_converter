import unittest
from currency_converter import dollar_to_rupee 

class TestCurrencyConversion(unittest.TestCase):

      def test_dollar_to_rupee(self):
        self.assertAlmostEqual(dollar_to_rupee(10), 740)
        self.assertAlmostEqual(dollar_to_rupee(20), 1480)

      def test_blank_input_dollar_to_rupee(self):
        with self.assertRaises(ValueError):
            dollar_to_rupee('')  
   

if __name__ == '__main__':
    unittest.main()
