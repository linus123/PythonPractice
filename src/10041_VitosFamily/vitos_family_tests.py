import unittest

from vitos_family import find_sum_of_distances


class VitosFamilyTests(unittest.TestCase):
    def test_001(self):
        """Should return the correct answer given the first sample problem"""

        numbers = [2, 4]
        result = find_sum_of_distances(numbers)
        self.assertEqual(2, result)

    def test_002(self):
        """Should return the correct answer for the scond sample program"""

        numbers = [2, 4, 6]
        result = find_sum_of_distances(numbers)
        self.assertEqual(4, result)

    def test_003(self):
        """Should return expected value given udbug problem 1"""

        numbers = [7, 8, 2, 3, 6, 1]
        result = find_sum_of_distances(numbers)
        self.assertEqual(15, result)

    def test_004(self):
        """Should return correct value for udebug problem 2"""

        numbers = [1, 1, 1, 1, 1000, 1000]
        result = find_sum_of_distances(numbers)
        self.assertEqual(1998, result)

    def test_005(self):
        """Should return correct value for udebug problem 3"""

        numbers = [7, 8, 2, 3, 6, 1]
        result = find_sum_of_distances(numbers)
        self.assertEqual(15, result)

    def test_006(self):
        """Should return correct value for udebug problem 3"""

        numbers = [1, 2, 4, 5]
        result = find_sum_of_distances(numbers)
        self.assertEqual(6, result)



