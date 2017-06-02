import unittest
from ThreeNPlus1 import three_n_plus_one
from ThreeNPlus1 import maxThreeNPlus1
from ThreeNPlus1 import threeNPlus1CountOnly

class ThreeNPLus1Tests(unittest.TestCase):

    def test_shouldReturnExpectedValues(self):
        result = three_n_plus_one(22)
        self.assertEqual(result[0], 22)
        self.assertEqual(result[1], 11)
        self.assertEqual(result[2], 34)

    def test_shouldReturnExpectedLength(self):
        result = three_n_plus_one(17)
        self.assertEqual(len(result), 13)

        result = three_n_plus_one(18)
        self.assertEqual(len(result), 21)

        result = three_n_plus_one(19)
        self.assertEqual(len(result), 21)

        result = three_n_plus_one(20)
        self.assertEqual(len(result), 8)

        result = three_n_plus_one(21)
        self.assertEqual(len(result), 8)

        result = three_n_plus_one(22)
        self.assertEqual(len(result), 16)

    def test_shouldFindMaxCountGivenRange(self):
        result = maxThreeNPlus1(17, 22)
        self.assertEqual(result, 21)

        result = maxThreeNPlus1(1, 10)
        self.assertEqual(result, 20)

        result = maxThreeNPlus1(100, 200)
        self.assertEqual(result, 125)

    def test_not_working(self):
        result = three_n_plus_one(956739)
        self.assertEqual(len(result), 352)

        result = threeNPlus1CountOnly(956739)
        self.assertEqual(result, 352)

        result = maxThreeNPlus1(956739, 956006)
        self.assertEqual(result, 352)


def main():
    unittest.main()

if __name__ == '__main__':
    main()

