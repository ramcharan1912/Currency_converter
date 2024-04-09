import unittest
from currency_converter import dollar_to_rupee, rupee_to_dollar

class TestCurrencyConversion(unittest.TestCase):

     def test_dollar_to_rupee(self):
        self.assertAlmostEqual(dollar_to_rupee(10), 740)
        self.assertAlmostEqual(dollar_to_rupee(20), 1480)
        

if __name__ == '__main__':
    unittest.main()
