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

    def test_200(self):
        """has_more_than_one_difference should be zero for the exact same word"""

        word1 = "sum"
        result = has_more_than_one_difference_primitive(word1, word1)
        self.assertFalse(result)

    def test_201(self):
        """has_more_than_one_difference should return false given a single letter difference with 3 letter word"""

        result = has_more_than_one_difference_primitive("sum", "fum")
        self.assertFalse(result)

        result = has_more_than_one_difference_primitive("sum", "som")
        self.assertFalse(result)

        result = has_more_than_one_difference_primitive("sum", "sud")
        self.assertFalse(result)

    def test_202(self):
        """has_more_than_one_difference should return true given words with wildly different lengths"""

        result = has_more_than_one_difference_primitive("sum", "foobar")
        self.assertTrue(result)

        result = has_more_than_one_difference_primitive("sum", "a")
        self.assertTrue(result)

        result = has_more_than_one_difference_primitive("sum", "subsc")
        self.assertTrue(result)

    def test_203(self):
        """has_more_than_one_difference should return true given 3 letter word with only letter differences"""

        result = has_more_than_one_difference_primitive("sum", "soo")
        self.assertTrue(result)

        result = has_more_than_one_difference_primitive("sum", "fom")
        self.assertTrue(result)

    def test_204(self):
        """has_more_than_one_difference should return false if only one letter is missing at the end"""

        result = has_more_than_one_difference_primitive("sum", "sumo")
        self.assertFalse(result)

        result = has_more_than_one_difference_primitive("sumo", "sum")
        self.assertFalse(result)

    def test_205(self):
        """has_more_than_one_difference should return false when only a single letter is missing from a word"""

        result = has_more_than_one_difference_primitive("foobar", "fobar")
        self.assertFalse(result)

        result = has_more_than_one_difference_primitive("fobar", "foobar")
        self.assertFalse(result)

        result = has_more_than_one_difference_primitive("fo", "f")
        self.assertFalse(result)

        result = has_more_than_one_difference_primitive("f", "fo")
        self.assertFalse(result)

    def test_206(self):
        """has_more_than_one_difference should return true when one letter is different and one letter is missing"""

        result = has_more_than_one_difference_primitive("foobar", "fobara")
        self.assertTrue(result)

        result = has_more_than_one_difference_primitive("fobara", "foobar")
        self.assertTrue(result)

        result = has_more_than_one_difference_primitive("xoobar", "foobara")
        self.assertTrue(result)

        result = has_more_than_one_difference_primitive("foobara", "xoobar")
        self.assertTrue(result)

    def test_207(self):
        """has_more_than_one_difference should return true when missing two letters"""

        result = has_more_than_one_difference_primitive("foobar", "foobaroo")
        self.assertTrue(result)

        result = has_more_than_one_difference_primitive("foobaroo", "foobar")
        self.assertTrue(result)

    def test_208(self):
        """has_more_than_one_difference should work with two letter"""

        result = has_more_than_one_difference_primitive("ac", "ab")
        self.assertFalse(result)

        result = has_more_than_one_difference_primitive("ab", "bb")
        self.assertFalse(result)

    def test_209(self):
        """foobar"""

        result = has_more_than_one_difference_primitive("abacus", "aback")
        self.assertTrue(result)
