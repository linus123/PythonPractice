import unittest
from TheTrip import balance_money

class BalanceMoneyTests(unittest.TestCase):
    def test_should_return_expected_number_of_items(self):
        result = balance_money([10.00, 20.00, 30.00])
        self.assertEqual(len(result), 3)

    def test_should_return_expected_items_when_average_is_perfect(self):
        result = balance_money([10.00, 10.00, 10.00])
        self.assertEqual(result[0], 10.00)
        self.assertEqual(result[1], 10.00)
        self.assertEqual(result[2], 10.00)

    def test_should_rebalance_numbers_when_there_is_no_remainder(self):
        result = balance_money([5.00, 10.00, 15.00])
        self.assertEqual(result[0], 10.00)
        self.assertEqual(result[1], 10.00)
        self.assertEqual(result[2], 10.00)

    def test_should_rebalance_numbers_when_there_is_remainder(self):
        result = balance_money([5.01, 10.01, 15.00])
        self.assertEqual(result[0], 10.01)
        self.assertEqual(result[1], 10.01)
        self.assertEqual(result[2], 10.00)

    def test_should_rebalance_numbers_when_there_is_remainder(self):
        result = balance_money([30.03, 2.00, 2.04, 6.00])
        self.assertEqual(result[0], 10.02)
        self.assertEqual(result[1], 10.02)
        self.assertEqual(result[2], 10.02)
        self.assertEqual(result[3], 10.01)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

