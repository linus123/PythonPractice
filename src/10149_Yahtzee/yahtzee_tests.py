import unittest

from yahtzee import ThrowRoll, Category


class ThrowRollTest(unittest.TestCase):
    def test_001(self):
        """get_score should return false when non full house"""
        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertEqual(0, roll.get_score(Category.FULL_HOUSE))

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertEqual(0, roll.get_score(Category.FULL_HOUSE))

        roll = ThrowRoll([2, 2, 3, 4, 4])
        self.assertEqual(0, roll.get_score(Category.FULL_HOUSE))

    def test_002(self):
        """get_score should return true given full_house_numbers"""

        roll = ThrowRoll([1, 1, 2, 2, 2])
        self.assertEqual(40, roll.get_score(Category.FULL_HOUSE))

        roll = ThrowRoll([2, 2, 3, 3, 3])
        self.assertEqual(40, roll.get_score(Category.FULL_HOUSE))

        roll = ThrowRoll([6, 2, 2, 2, 6])
        self.assertEqual(40, roll.get_score(Category.FULL_HOUSE))

    def test_003(self):
        """is_long_straight should return false when not sequence"""

        roll = ThrowRoll([1, 1, 2, 2, 2])
        self.assertFalse(roll.is_long_straight())

        roll = ThrowRoll([1, 2, 3, 4, 4])
        self.assertFalse(roll.is_long_straight())

        roll = ThrowRoll([1, 1, 2, 3, 4])
        self.assertFalse(roll.is_long_straight())

    def test_004(self):
        """is_long_straight should return true when is sequence"""

        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertTrue(roll.is_long_straight())

        roll = ThrowRoll([2, 3, 4, 5, 6])
        self.assertTrue(roll.is_long_straight())

        roll = ThrowRoll([1, 5, 2, 4, 3])
        self.assertTrue(roll.is_long_straight())

        roll = ThrowRoll([6, 5, 4, 3, 2])
        self.assertTrue(roll.is_long_straight())

    def test_005(self):
        """is_short_straight should return false when there is no 4 sequence"""

        roll = ThrowRoll([1, 2, 3, 2, 2])
        self.assertFalse(roll.is_short_straight())

        roll = ThrowRoll([2, 1, 1, 2, 3])
        self.assertFalse(roll.is_short_straight())

    def test_006(self):
        """is_short_straight should return true when roll has sequence of 4"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertTrue(roll.is_short_straight())

        roll = ThrowRoll([6, 1, 2, 3, 4])
        self.assertTrue(roll.is_short_straight())

        roll = ThrowRoll([1, 3, 4, 2, 1])
        self.assertTrue(roll.is_short_straight())

    def test_007(self):
        """get_five_of_a_kind_sum should return 0"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(0, roll.get_five_of_a_kind_sum())

        roll = ThrowRoll([1, 1, 1, 1, 4])
        self.assertEqual(0, roll.get_five_of_a_kind_sum())

    def test_008(self):
        """has_five_of_a_kind should return sum when there is 5 of any dice"""

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertEqual(5, roll.get_five_of_a_kind_sum())

        roll = ThrowRoll([2, 2, 2, 2, 2])
        self.assertEqual(10, roll.get_five_of_a_kind_sum())

        roll = ThrowRoll([5, 5, 5, 5, 5])
        self.assertEqual(25, roll.get_five_of_a_kind_sum())

    def test_009(self):
        """get_four_of_a_kind_sum should be 0 when there is NOT 4 of any dice"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(0, roll.get_four_of_a_kind_sum())

        roll = ThrowRoll([1, 1, 1, 2, 3])
        self.assertEqual(0, roll.get_four_of_a_kind_sum())

    def test_010(self):
        """get_four_of_a_kind_sum should be sum when there is 4 of any dice"""

        roll = ThrowRoll([1, 1, 1, 1, 3])
        self.assertEqual(4, roll.get_four_of_a_kind_sum())

        roll = ThrowRoll([4, 6, 6, 6, 6])
        self.assertEqual(6 * 4, roll.get_four_of_a_kind_sum())

        roll = ThrowRoll([3, 3, 5, 3, 3])
        self.assertEqual(3 * 4, roll.get_four_of_a_kind_sum())

    def test_011(self):
        """get_change_value should return sum of all dice"""

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertEqual(5, roll.get_change_value())

        roll = ThrowRoll([1, 1, 1, 6, 1])
        self.assertEqual(10, roll.get_change_value())

        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertEqual(15, roll.get_change_value())

    def test_012(self):
        """get_sum_of_all should return the sum of all of a single value"""

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertEqual(5, roll.get_sum_of_all(1))

        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertEqual(5, roll.get_sum_of_all(5))

        roll = ThrowRoll([1, 2, 3, 5, 5])
        self.assertEqual(10, roll.get_sum_of_all(5))

        roll = ThrowRoll([5, 2, 3, 5, 5])
        self.assertEqual(15, roll.get_sum_of_all(5))

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(0, roll.get_sum_of_all(5))
