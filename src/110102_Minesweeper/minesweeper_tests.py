import unittest


class MinesweeperTests(unittest.TestCase):
    def test_should_return_expected_count1(self):
        from minesweeper import count_mines
        field = ["*...", "....", ".*..", "...."]

        field_with_counts = count_mines(4, 4, field)

        self.assertEqual(field_with_counts[0], "*100")
        self.assertEqual(field_with_counts[1], "2210")
        self.assertEqual(field_with_counts[2], "1*10")
        self.assertEqual(field_with_counts[3], "1110")

    def test_should_return_expected_count2(self):
        from minesweeper import count_mines
        field = ["**...", ".....", ".*..."]

        field_with_counts = count_mines(3, 5, field)

        self.assertEqual(field_with_counts[0], "**100")
        self.assertEqual(field_with_counts[1], "33200")
        self.assertEqual(field_with_counts[2], "1*100")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
