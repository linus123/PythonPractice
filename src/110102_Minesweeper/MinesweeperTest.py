import unittest
from Minesweeper import count_mines

class MinesweeperTests(unittest.TestCase):
    def test_should_work(self):
        field = []

        field.append("*...")
        field.append("....")
        field.append(".*..")
        field.append("....")

        count_mines(3, 5, field)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

