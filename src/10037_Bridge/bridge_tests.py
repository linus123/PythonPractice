import unittest

from bridge import get_min_time_to_cross


class BridgeTests(unittest.TestCase):
    def test_001(self):
        """ShouldR return the value of the of the given time given a single person"""

        people = [1]
        result = get_min_time_to_cross(people)

        self.assertEqual(1, result.total_number_of_seconds)
        self.assertEqual(1, len(result.crossings))
        self.assertEqual([1], result.crossings[0])

    def test_002(self):
        """Should return the time of the large person give two people"""

        people = [1, 2]
        result = get_min_time_to_cross(people)

        self.assertEqual(2, result.total_number_of_seconds)
        self.assertEqual(1, len(result.crossings))
        self.assertEqual([1, 2], result.crossings[0])

        people = [1, 10]
        result = get_min_time_to_cross(people)

        self.assertEqual(10, result.total_number_of_seconds)
        self.assertEqual(1, len(result.crossings))
        self.assertEqual([1, 10], result.crossings[0])

    def test_003(self):
        """Should return expected values given sample test problem"""

        people = [1, 2, 5, 10]
        result = get_min_time_to_cross(people)

        self.assertEqual(17, result.total_number_of_seconds)
        self.assertEqual(5, len(result.crossings))
        self.assertEqual([1, 2], result.crossings[0])
        self.assertEqual([1], result.crossings[1])
        self.assertEqual([5, 10], result.crossings[2])
        self.assertEqual([2], result.crossings[3])
        self.assertEqual([1, 2], result.crossings[4])

    def test_004(self):
        """Udebug 1"""

        people = [1, 3, 5]
        result = get_min_time_to_cross(people)

        self.assertEqual(9, result.total_number_of_seconds)
        self.assertEqual(3, len(result.crossings))
        self.assertEqual([1, 3], result.crossings[0])
        self.assertEqual([1], result.crossings[1])
        self.assertEqual([1, 5], result.crossings[2])
