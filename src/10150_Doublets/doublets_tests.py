import unittest

from doublets import has_more_than_one_difference


class DoubletsTests(unittest.TestCase):
    def test_200(self):
        """has_more_than_one_difference should be zero for the exact same word"""

        word1 = "sum"
        result = has_more_than_one_difference(word1, word1)
        self.assertFalse(result)

    def test_201(self):
        """has_more_than_one_difference should return false given a single letter difference with 3 letter word"""

        result = has_more_than_one_difference("sum", "fum")
        self.assertFalse(result)

        result = has_more_than_one_difference("sum", "som")
        self.assertFalse(result)

        result = has_more_than_one_difference("sum", "sud")
        self.assertFalse(result)

    def test_202(self):
        """has_more_than_one_difference should return true given words with wildly different lengths"""

        result = has_more_than_one_difference("sum", "foobar")
        self.assertTrue(result)

        result = has_more_than_one_difference("sum", "a")
        self.assertTrue(result)

        result = has_more_than_one_difference("sum", "subsc")
        self.assertTrue(result)

    def test_203(self):
        """has_more_than_one_difference should return true given 3 letter word with only letter differences"""

        result = has_more_than_one_difference("sum", "soo")
        self.assertTrue(result)

        result = has_more_than_one_difference("sum", "fom")
        self.assertTrue(result)

    def test_204(self):
        """has_more_than_one_difference should return false if only one letter is missing at the end"""

        result = has_more_than_one_difference("sum", "sumo")
        self.assertFalse(result)

        result = has_more_than_one_difference("sumo", "sum")
        self.assertFalse(result)

    def test_205(self):
        """has_more_than_one_difference should return false when only a single letter is missing from a word"""

        result = has_more_than_one_difference("foobar", "fobar")
        self.assertFalse(result)

        result = has_more_than_one_difference("fobar", "foobar")
        self.assertFalse(result)

        result = has_more_than_one_difference("fo", "f")
        self.assertFalse(result)

        result = has_more_than_one_difference("f", "fo")
        self.assertFalse(result)

    def test_206(self):
        """foobar should return true when one letter is different and one letter is missing"""

        result = has_more_than_one_difference("foobar", "fobara")
        self.assertTrue(result)

        result = has_more_than_one_difference("fobara", "foobar")
        self.assertTrue(result)

        result = has_more_than_one_difference("xoobar", "foobara")
        self.assertTrue(result)

        result = has_more_than_one_difference("foobara", "xoobar")
        self.assertTrue(result)

    def test_207(self):
        """Should return true when missing two letters"""

        result = has_more_than_one_difference("foobar", "foobaroo")
        self.assertTrue(result)

        result = has_more_than_one_difference("foobaroo", "foobar")
        self.assertTrue(result)
