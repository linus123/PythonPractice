import unittest


class JollyJumperTests(unittest.TestCase):

    def test_should_error_given_empty_array(self):
        from jolly_jumper import is_jolly_jumper

        def empty_array_call():
            is_jolly_jumper([])

        self.assertRaises(ValueError, empty_array_call)

    def test_should_return_true_when_given_array_with_single_item(self):
        from jolly_jumper import is_jolly_jumper

        result = is_jolly_jumper([1])
        self.assertTrue(result)

    def test_should_return_false_when_diff_of_two_items_is_not_one(self):
        from jolly_jumper import is_jolly_jumper

        result = is_jolly_jumper([100, 122])
        self.assertFalse(result)

        result = is_jolly_jumper([-100, 122])
        self.assertFalse(result)

        result = is_jolly_jumper([100, -122])
        self.assertFalse(result)

        result = is_jolly_jumper([-100, -122])
        self.assertFalse(result)

    def test_should_return_false_when_diff_more_than_one_give_three_values(self):
        from jolly_jumper import is_jolly_jumper

        result = is_jolly_jumper([1, 2, 5])
        self.assertFalse(result)

        result = is_jolly_jumper([1, 2, -5])
        self.assertFalse(result)

        result = is_jolly_jumper([-1, -2, -5])
        self.assertFalse(result)

        result = is_jolly_jumper([4, 1, 3])
        self.assertFalse(result)

        result = is_jolly_jumper([7, -6, -9])
        self.assertFalse(result)

    def test_should_return_true_when_two_values_are_give_and_diff_is_one(self):
        from jolly_jumper import is_jolly_jumper

        result = is_jolly_jumper([0, 1])
        self.assertTrue(result)

        result = is_jolly_jumper([0, -1])
        self.assertTrue(result)

        result = is_jolly_jumper([-1, 0])
        self.assertTrue(result)

        result = is_jolly_jumper([1, 0])
        self.assertTrue(result)

        result = is_jolly_jumper([1, 2])
        self.assertTrue(result)

        result = is_jolly_jumper([-2, -3])
        self.assertTrue(result)

    def test_should_return_true_given_three_values(self):
        from jolly_jumper import is_jolly_jumper

        result = is_jolly_jumper([0, 1, 3])
        self.assertTrue(result)

        result = is_jolly_jumper([0, -1, 1])
        self.assertTrue(result)

        result = is_jolly_jumper([0, -1, -3])
        self.assertTrue(result)

        result = is_jolly_jumper([6, 7, 9])
        self.assertTrue(result)

        result = is_jolly_jumper([-6, -7, -9])
        self.assertTrue(result)

    def test_random_true_test(self):
        from jolly_jumper import is_jolly_jumper

        result = is_jolly_jumper([1, 4, 2, 3])
        self.assertTrue(result)

        result = is_jolly_jumper([4, 6, -1, 2, -4, 0, 1, 6, -2])
        self.assertTrue(result)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
