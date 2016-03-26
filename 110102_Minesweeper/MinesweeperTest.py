import unittest
from Minesweeper import count_mines

class MinesweeperTests(unittest.TestCase):
    def test_should_work(self):
        field = []

        field[0] = "*..."
        field[1] = "...."
        field[2] = ".*.."
        field[3] = "...."

        count_mines(3, 5, field)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

