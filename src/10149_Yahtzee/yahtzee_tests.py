import unittest

from yahtzee import ThrowRoll


class ThrowRollTest(unittest.TestCase):
    def test_001(self):
        """is_full_house should return false when non full house"""
        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertFalse(roll.is_full_house())

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertFalse(roll.is_full_house())

        roll = ThrowRoll([2, 2, 3, 4, 4])
        self.assertFalse(roll.is_full_house())

    def test_002(self):
        """is_full_houlse should return true given values in predictable order"""

        roll = ThrowRoll([1, 1, 2, 2, 2])
        self.assertTrue(roll.is_full_house())

        roll = ThrowRoll([2, 2, 3, 3, 3])
        self.assertTrue(roll.is_full_house())

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
        """has_five_of_a_kind should be false when not 5 of any dice"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertFalse(roll.has_five_of_a_kind())

        roll = ThrowRoll([1, 1, 1, 1, 4])
        self.assertFalse(roll.has_five_of_a_kind())

    def test_008(self):
        """has_five_of_a_kind should be true when there is 5 of any dice"""

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertTrue(roll.has_five_of_a_kind())

        roll = ThrowRoll([2, 2, 2, 2, 2])
        self.assertTrue(roll.has_five_of_a_kind())

    def test_009(self):
        """has_four_of_a_kind should be false when there is NOT 4 of any dice"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertFalse(roll.has_four_of_a_kind())

        roll = ThrowRoll([1, 1, 1, 2, 3])
        self.assertFalse(roll.has_four_of_a_kind())

    def test_010(self):
        """has_four_of_a_kind should be true when there is 4 of any dice"""

        roll = ThrowRoll([1, 1, 1, 1, 3])
        self.assertTrue(roll.has_four_of_a_kind())

        roll = ThrowRoll([4, 6, 6, 6, 6])
        self.assertTrue(roll.has_four_of_a_kind())

        roll = ThrowRoll([3, 3, 5, 3, 3])
        self.assertTrue(roll.has_four_of_a_kind())

    def test_011(self):
        """get_change_value should return sum of all dice"""

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertEqual(5, roll.get_change_value())

        roll = ThrowRoll([1, 1, 1, 6, 1])
        self.assertEqual(10, roll.get_change_value())

        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertEqual(15, roll.get_change_value())
