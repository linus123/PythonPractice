import unittest

from yahtzee import ThrowRoll, Category, YahtzeeScorer, ScoreSequence


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
        self.assertEqual(0, roll.get_score(Category.LONG_STRAIGHT))

        roll = ThrowRoll([1, 2, 3, 4, 4])
        self.assertEqual(0, roll.get_score(Category.LONG_STRAIGHT))

        roll = ThrowRoll([1, 1, 2, 3, 4])
        self.assertEqual(0, roll.get_score(Category.LONG_STRAIGHT))

    def test_004(self):
        """is_long_straight should return true when is sequence"""

        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertEqual(30, roll.get_score(Category.LONG_STRAIGHT))

        roll = ThrowRoll([2, 3, 4, 5, 6])
        self.assertEqual(30, roll.get_score(Category.LONG_STRAIGHT))

        roll = ThrowRoll([1, 5, 2, 4, 3])
        self.assertEqual(30, roll.get_score(Category.LONG_STRAIGHT))

        roll = ThrowRoll([6, 5, 4, 3, 2])
        self.assertEqual(30, roll.get_score(Category.LONG_STRAIGHT))

    def test_005(self):
        """is_short_straight should return false when there is no 4 sequence"""

        roll = ThrowRoll([1, 2, 3, 2, 2])
        self.assertEqual(0, roll.get_score(Category.SHORT_STRAIGHT))

        roll = ThrowRoll([2, 1, 1, 2, 3])
        self.assertEqual(0, roll.get_score(Category.SHORT_STRAIGHT))

    def test_006(self):
        """is_short_straight should return true when roll has sequence of 4"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(25, roll.get_score(Category.SHORT_STRAIGHT))

        roll = ThrowRoll([6, 1, 2, 3, 4])
        self.assertEqual(25, roll.get_score(Category.SHORT_STRAIGHT))

        roll = ThrowRoll([1, 3, 4, 2, 1])
        self.assertEqual(25, roll.get_score(Category.SHORT_STRAIGHT))

    def test_007(self):
        """get_five_of_a_kind_sum should return 0"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(0, roll.get_score(Category.FIVE_OF_A_KIND))

        roll = ThrowRoll([1, 1, 1, 1, 4])
        self.assertEqual(0, roll.get_score(Category.FIVE_OF_A_KIND))

    def test_008(self):
        """has_five_of_a_kind should return sum when there is 5 of any dice"""

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertEqual(50, roll.get_score(Category.FIVE_OF_A_KIND))

        roll = ThrowRoll([2, 2, 2, 2, 2])
        self.assertEqual(50, roll.get_score(Category.FIVE_OF_A_KIND))

        roll = ThrowRoll([5, 5, 5, 5, 5])
        self.assertEqual(50, roll.get_score(Category.FIVE_OF_A_KIND))

    def test_009(self):
        """get_four_of_a_kind_sum should be 0 when there is NOT 4 of any dice"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(0, roll.get_score(Category.FOUR_OF_A_KIND))

        roll = ThrowRoll([1, 1, 1, 2, 3])
        self.assertEqual(0, roll.get_score(Category.FOUR_OF_A_KIND))

    def test_010(self):
        """get_four_of_a_kind_sum should be sum when there is 4 of any dice"""

        roll = ThrowRoll([1, 1, 1, 1, 3])
        self.assertEqual(4, roll.get_score(Category.FOUR_OF_A_KIND))

        roll = ThrowRoll([4, 6, 6, 6, 6])
        self.assertEqual(6 * 4, roll.get_score(Category.FOUR_OF_A_KIND))

        roll = ThrowRoll([3, 3, 5, 3, 3])
        self.assertEqual(3 * 4, roll.get_score(Category.FOUR_OF_A_KIND))

    def test_011(self):
        """get_three_of_a_kind_sum should be 0 when there is NOT 4 of any dice"""

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(0, roll.get_score(Category.THREE_OF_A_KIND))

        roll = ThrowRoll([1, 6, 1, 2, 3])
        self.assertEqual(0, roll.get_score(Category.THREE_OF_A_KIND))

    def test_012(self):
        """get_three_of_a_kind_sum should be sum when there is 4 of any dice"""

        roll = ThrowRoll([1, 1, 1, 1, 3])
        self.assertEqual(3, roll.get_score(Category.THREE_OF_A_KIND))

        roll = ThrowRoll([4, 6, 6, 6, 6])
        self.assertEqual(6 * 3, roll.get_score(Category.THREE_OF_A_KIND))

        roll = ThrowRoll([3, 6, 5, 3, 3])
        self.assertEqual(3 * 3, roll.get_score(Category.THREE_OF_A_KIND))

    def test_013(self):
        """CHANCE should return sum of all dice"""

        roll = ThrowRoll([1, 1, 1, 1, 1])
        self.assertEqual(5, roll.get_score(Category.CHANCE))

        roll = ThrowRoll([1, 1, 1, 6, 1])
        self.assertEqual(10, roll.get_score(Category.CHANCE))

        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertEqual(15, roll.get_score(Category.CHANCE))

    def test_014(self):
        """get_sum_of_all should return the sum of all of a single value"""

        roll = ThrowRoll([1, 1, 1, 1, 6])
        self.assertEqual(0, roll.get_score(Category.TWOS))
        self.assertEqual(4, roll.get_score(Category.ONES))
        self.assertEqual(6, roll.get_score(Category.SIXES))

        roll = ThrowRoll([1, 2, 3, 4, 5])
        self.assertEqual(1, roll.get_score(Category.ONES))
        self.assertEqual(2, roll.get_score(Category.TWOS))
        self.assertEqual(3, roll.get_score(Category.THREES))
        self.assertEqual(4, roll.get_score(Category.FOURS))
        self.assertEqual(5, roll.get_score(Category.FIVES))

        roll = ThrowRoll([1, 2, 3, 5, 5])
        self.assertEqual(10, roll.get_score(Category.FIVES))

        roll = ThrowRoll([5, 2, 3, 5, 5])
        self.assertEqual(15, roll.get_score(Category.FIVES))

        roll = ThrowRoll([1, 2, 3, 4, 1])
        self.assertEqual(0, roll.get_score(Category.FIVES))


class ScoreSequenceTests(unittest.TestCase):
    def test_000(self):
        """get_score should return total score without bonus"""
        ss = ScoreSequence()

        same_roll = ThrowRoll([1, 2, 3, 4, 5])

        ss.set_category(Category.ONES, same_roll)
        ss.set_category(Category.TWOS, same_roll)
        ss.set_category(Category.THREES, same_roll)
        ss.set_category(Category.FOURS, same_roll)
        ss.set_category(Category.FIVES, same_roll)
        ss.set_category(Category.SIXES, same_roll)
        ss.set_category(Category.CHANCE, same_roll)
        ss.set_category(Category.THREE_OF_A_KIND, same_roll)
        ss.set_category(Category.FOUR_OF_A_KIND, same_roll)
        ss.set_category(Category.FIVE_OF_A_KIND, same_roll)
        ss.set_category(Category.SHORT_STRAIGHT, same_roll)
        ss.set_category(Category.LONG_STRAIGHT, same_roll)
        ss.set_category(Category.FULL_HOUSE, same_roll)

        score = ss.get_score()

        self.assertEqual(90, score)


class YahtzeeScorerTest(unittest.TestCase):
    def test_000(self):
        """"""
        s = YahtzeeScorer()
        s.add_roll([1, 2, 3, 4, 5])
        self.assertFalse(s.is_complete())
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        s.add_roll([1, 2, 3, 4, 5])
        self.assertTrue(s.is_complete())

        self.assertEqual("1 2 3 4 5 0 15 0 0 0 25 35 0 0 90", s.get_game_score())

