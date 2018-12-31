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

    def test_005(self):
        """get_projection_left_to_right should return none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection_left_to_right(0, 0, 2)
        self.assertEqual(None, projection)

    def test_006(self):
        """get_projection_left_to_right should return string given valid length"""
        grid = WaldorfGrid(["ab"], 1, 2)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection_left_to_right(0, 0, 2)
        self.assertEqual("ab", projection)

    def test_007(self):
        """get_projection_left_to_right should return string given longer valid length"""
        grid = WaldorfGrid(["abcdefg"], 1, 7)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection_left_to_right(0, 0, 3)
        self.assertEqual("abc", projection)

    def test_008(self):
        """get_projection_right_to_left should none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection_right_to_left(0, 0, 2)
        self.assertEqual(None, projection)

    def test_009(self):
        """get_projection_right_to_left should return string given valid length"""
        grid = WaldorfGrid(["ab"], 1, 2)

        result = grid.get_char(0, 1)
        self.assertEqual("b", result)

        projection = grid.get_projection_right_to_left(0, 1, 2)
        self.assertEqual("ba", projection)

    def test_010(self):
        """get_projection_right_to_left should return string given longer valid length"""
        grid = WaldorfGrid(["abcdefg"], 1, 7)

        result = grid.get_char(0, 4)
        self.assertEqual("e", result)

        projection = grid.get_projection_right_to_left(0, 4, 3)
        self.assertEqual("edc", projection)


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

    def get_projection_left_to_right(self, row_index: int, col_index: int, length: int):

        if col_index + length > self.column_count:
            return None

        return self.__grid[row_index][col_index: col_index + length]

    def get_projection_right_to_left(self, row_index: int, col_index: int, length: int):

        if col_index - length + 1 < 0:
            return None

        raw_string = self.__grid[row_index][col_index - length + 1: col_index + 1]

        return raw_string[::-1]

