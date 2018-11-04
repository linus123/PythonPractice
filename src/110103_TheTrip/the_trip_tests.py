import unittest


class BalanceMoneyTests(unittest.TestCase):
    def test_should_return_expected_number_of_items(self):
        from the_trip import balance_money
        result = balance_money([1000, 2000, 3000])
        self.assertEqual(len(result), 3)

    def test_should_return_expected_items_when_average_is_perfect(self):
        from the_trip import balance_money
        result = balance_money([1000, 1000, 1000])
        self.assertEqual(result[0], 1000)
        self.assertEqual(result[1], 1000)
        self.assertEqual(result[2], 1000)

    def test_should_balance_numbers_when_there_is_no_remainder(self):
        from the_trip import balance_money
        result = balance_money([500, 1000, 1500])
        self.assertEqual(result[0], 1000)
        self.assertEqual(result[1], 1000)
        self.assertEqual(result[2], 1000)

    def test_should_balance_numbers_when_there_is_remainder(self):
        from the_trip import balance_money
        result = balance_money([501, 1001, 1500])
        self.assertEqual(result[0], 1001)
        self.assertEqual(result[1], 1001)
        self.assertEqual(result[2], 1000)

    def test_should_balance_numbers_when_there_is_remainder_2(self):
        from the_trip import balance_money
        result = balance_money([3003, 200, 204, 600])
        self.assertEqual(result[0], 1002)
        self.assertEqual(result[1], 1002)
        self.assertEqual(result[2], 1002)
        self.assertEqual(result[3], 1001)

    def test_should_have_bias_toward_larges_amount(self):
        from the_trip import balance_money
        result = balance_money([1, 3, 3])
        self.assertEqual(result[0], 3)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 2)

    def test_should_return_the_correct_minimum_amount_of_moving_money(self):
        from the_trip import get_minimum_exchange

        result = get_minimum_exchange([5.01, 10.01, 15.00])
        self.assertEqual(result, 4.99)

        result = get_minimum_exchange([10.07, 10, 10, 10])
        self.assertEqual(result, 0.05)

        result = get_minimum_exchange([0.03, 0.03, 0.01])
        self.assertEqual(result, 0.01)

        result = get_minimum_exchange([0.01, 0.03, 0.03])
        self.assertEqual(result, 0.01)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
