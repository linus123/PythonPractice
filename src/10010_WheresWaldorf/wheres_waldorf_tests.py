import unittest


class WaldorfGridTests(unittest.TestCase):
    def test_001(self):
        """get_char should return None when given location out of bounds"""
        grid = WaldorfGrid([""], 1, 0)

        result = grid.get_char(0, 0)

        self.assertEqual(None, result)

    def test_002(self):
        """get_char should return None when empty array"""
        grid = WaldorfGrid([], 1, 0)

        result = grid.get_char(0, 0)

        self.assertEqual(None, result)

    def test_003(self):
        """get_char should return none when position is out of bounds"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(1, 1)

        self.assertEqual(None, result)

    def test_004(self):
        """get_char should get character as location"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)

        self.assertEqual("a", result)


class WaldorfGrid:
    def __init__(self, grid: list, m: int, n: int) -> None:
        self.__grid = grid
        self.row_count = m
        self.column_count = n

    def __is_empty(self) -> bool:
        if self.column_count <= 0:
            return True

    def get_char(self, row_index: int, col_index: int) -> chr:
        if self.__is_empty():
            return None

        if row_index >= self.row_count:
            return None

        if col_index >= self.column_count:
            return None

        return self.__grid[row_index][col_index]
