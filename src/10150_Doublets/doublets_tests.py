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
