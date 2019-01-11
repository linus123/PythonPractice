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

        people = [35, 56, 72, 18, 26, 63, 26, 47, 18, 81, 69, 60, 84, 90, 90, 74, 33, 40, 45, 4, 36, 10, 38, 61, 84, 6,
                  41, 100, 57, 100, 91, 43, 7, 62, 60, 32, 76, 37, 30, 46]

        result = get_min_time_to_cross(people)

        self.assertEqual([4, 6], result.crossings[0])
        self.assertEqual([4], result.crossings[1])
        self.assertEqual([100, 100], result.crossings[2])
        self.assertEqual([6], result.crossings[3])
        self.assertEqual([4, 6], result.crossings[4])
        self.assertEqual([4], result.crossings[5])
        self.assertEqual([90, 91], result.crossings[6])
        self.assertEqual([6], result.crossings[7])
        self.assertEqual([4, 6], result.crossings[8])
        self.assertEqual([4], result.crossings[9])
        self.assertEqual([84, 90], result.crossings[10])
        self.assertEqual([6], result.crossings[11])
        self.assertEqual([4, 6], result.crossings[12])
        self.assertEqual([4], result.crossings[13])
        self.assertEqual([81, 84], result.crossings[14])
        self.assertEqual([6], result.crossings[15])
        self.assertEqual([4, 6], result.crossings[16])
        self.assertEqual([4], result.crossings[17])
        self.assertEqual([74, 76], result.crossings[18])
        self.assertEqual([6], result.crossings[19])
        self.assertEqual([4, 6], result.crossings[20])
        self.assertEqual([4], result.crossings[21])
        self.assertEqual([69, 72], result.crossings[22])
        self.assertEqual([6], result.crossings[23])
        self.assertEqual([4, 6], result.crossings[24])
        self.assertEqual([4], result.crossings[25])
        self.assertEqual([62, 63], result.crossings[26])
        self.assertEqual([6], result.crossings[27])
        self.assertEqual([4, 6], result.crossings[28])
        self.assertEqual([4], result.crossings[29])
        self.assertEqual([60, 61], result.crossings[30])
        self.assertEqual([6], result.crossings[31])
        self.assertEqual([4, 6], result.crossings[32])
        self.assertEqual([4], result.crossings[33])
        self.assertEqual([57, 60], result.crossings[34])
        self.assertEqual([6], result.crossings[35])
        self.assertEqual([4, 6], result.crossings[36])
        self.assertEqual([4], result.crossings[37])
        self.assertEqual([47, 56], result.crossings[38])
        self.assertEqual([6], result.crossings[39])
        self.assertEqual([4, 6], result.crossings[40])
        self.assertEqual([4], result.crossings[41])
        self.assertEqual([45, 46], result.crossings[42])
        self.assertEqual([6], result.crossings[43])
        self.assertEqual([4, 6], result.crossings[44])
        self.assertEqual([4], result.crossings[45])
        self.assertEqual([41, 43], result.crossings[46])
        self.assertEqual([6], result.crossings[47])
        self.assertEqual([4, 6], result.crossings[48])
        self.assertEqual([4], result.crossings[49])
        self.assertEqual([38, 40], result.crossings[50])
        self.assertEqual([6], result.crossings[51])
        self.assertEqual([4, 6], result.crossings[52])
        self.assertEqual([4], result.crossings[53])
        self.assertEqual([36, 37], result.crossings[54])
        self.assertEqual([6], result.crossings[55])
        self.assertEqual([4, 6], result.crossings[56])
        self.assertEqual([4], result.crossings[57])
        self.assertEqual([33, 35], result.crossings[58])
        self.assertEqual([6], result.crossings[59])
        self.assertEqual([4, 6], result.crossings[60])
        self.assertEqual([4], result.crossings[61])
        self.assertEqual([30, 32], result.crossings[62])
        self.assertEqual([6], result.crossings[63])
        self.assertEqual([4, 6], result.crossings[64])
        self.assertEqual([4], result.crossings[65])
        self.assertEqual([26, 26], result.crossings[66])
        self.assertEqual([6], result.crossings[67])
        self.assertEqual([4, 6], result.crossings[68])
        self.assertEqual([4], result.crossings[69])
        self.assertEqual([18, 18], result.crossings[70])
        self.assertEqual([6], result.crossings[71])
        self.assertEqual([4, 7], result.crossings[72])
        self.assertEqual([4], result.crossings[73])
        self.assertEqual([4, 10], result.crossings[74])
        self.assertEqual([4], result.crossings[75])
        self.assertEqual([4, 6], result.crossings[76])

        self.assertEqual(1349, result.total_number_of_seconds)

    def test_005(self):
        """Edge case 1"""
        people = [1, 3, 4, 5]

        result = get_min_time_to_cross(people)

        self.assertEqual(14, result.total_number_of_seconds)
        self.assertEqual(5, len(result.crossings))

        self.assertEqual([1, 4], result.crossings[0])
        self.assertEqual([1], result.crossings[1])
        self.assertEqual([1, 5], result.crossings[2])
        self.assertEqual([1], result.crossings[3])
        self.assertEqual([1, 3], result.crossings[4])

        # self.assertEqual([1, 3], result.crossings[0])
        # self.assertEqual([1], result.crossings[1])
        # self.assertEqual([4, 5], result.crossings[2])
        # self.assertEqual([3], result.crossings[3])
        # self.assertEqual([1, 3], result.crossings[4])

    def test_006(self):
        """Edge cases 2"""

        people = [1, 2, 4, 5]

        result = get_min_time_to_cross(people)

        self.assertEqual(12, result.total_number_of_seconds)
        self.assertEqual(5, len(result.crossings))
        self.assertEqual([1, 2], result.crossings[0])
        self.assertEqual([1], result.crossings[1])
        self.assertEqual([4, 5], result.crossings[2])
        self.assertEqual([2], result.crossings[3])
        self.assertEqual([1, 2], result.crossings[4])
