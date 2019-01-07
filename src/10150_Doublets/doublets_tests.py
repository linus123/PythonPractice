import unittest

from doublets import *


class DoubletsTests(unittest.TestCase):
    def test_001(self):
        """sample should work"""

        words = [
            "booster",
            "rooster",
            "roaster",
            "coasted",
            "roasted",
            "coastal",
            "postal"
        ]

        dpf = DoubletPathFinder(words)

        result = dpf.find_shortest_path(
            "booster",
            "roasted"
        )

        expected = [
            "booster",
            "rooster",
            "roaster",
            "roasted"
        ]

        self.assert_match(expected, result)

    def test_002(self):
        """Should pass short test"""

        words = [
            "aa",
            "ab",
            "ac",
            "bb"
        ]

        dpf = DoubletPathFinder(words)

        result = dpf.find_shortest_path(
            "ac",
            "bb"
        )

        expected = [
            "ac",
            "ab",
            "bb"
        ]

        self.assert_match(expected, result)

    def assert_match(self, expected, result):
        self.assertIsNotNone(result)

        match = all([a == b for a, b in zip(result, expected)])

        self.assertTrue(match, "%s does not match %s" % (result, expected))

    def test_300(self):
        """get_word_combinations should return every combination for single letter"""

        result = list(get_word_combinations("a"))

        self.assert_match(
            ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
             "w", "x", "y", "z"], result)

    def test_301(self):
        """get_word_combinations should return every word combination for two letters"""

        result = list(get_word_combinations("aa"))

        self.assertIn("ab", result)
        self.assertIn("ac", result)
        self.assertIn("ba", result)
        self.assertNotIn("a", result)
        self.assertNotIn("bb", result)

    def test_302(self):
        """get_word_combinations should return every word combination for two letters"""

        result = list(get_word_combinations("abc"))

        self.assertIn("abf", result)
        self.assertIn("fbc", result)
        self.assertIn("afc", result)
        self.assertNotIn("bc", result)
        self.assertNotIn("ac", result)
        self.assertNotIn("bc", result)
        self.assertNotIn("bbb", result)
