import unittest

from Minesweeper import count_mines


class MinesweeperTests(unittest.TestCase):
    def test_should_return_expected_count1(self):
        field = ["*...", "....", ".*..", "...."]

        field_with_counts = count_mines(4, 4, field)

        self.assertEquals(field_with_counts[0], "*100")
        self.assertEquals(field_with_counts[1], "2210")
        self.assertEquals(field_with_counts[2], "1*10")
        self.assertEquals(field_with_counts[3], "1110")

    def test_should_return_expected_count2(self):
        field = ["**...", ".....", ".*..."]

        field_with_counts = count_mines(3, 5, field)

        self.assertEquals(field_with_counts[0], "**100")
        self.assertEquals(field_with_counts[1], "33200")
        self.assertEquals(field_with_counts[2], "1*100")

def main():
    unittest.main()


if __name__ == '__main__':
    main()

