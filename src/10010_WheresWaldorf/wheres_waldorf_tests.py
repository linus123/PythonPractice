import unittest

from wheres_waldorf import WaldorfGrid, Direction


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
        """get_projection east should return none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.EAST)
        self.assertEqual(None, projection)

    def test_006(self):
        """get_projection east should return string given valid length"""
        grid = WaldorfGrid(["ab"], 1, 2)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 1, Direction.EAST)
        self.assertEqual("a", projection)

        projection = grid.get_projection(0, 0, 2, Direction.EAST)
        self.assertEqual("ab", projection)

    def test_007(self):
        """get_projection east should return string given longer valid length"""
        grid = WaldorfGrid(["abcdefg"], 1, 7)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 3, Direction.EAST)
        self.assertEqual("abc", projection)

    def test_008(self):
        """get_projection west should none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.WEST)
        self.assertEqual(None, projection)

    def test_009(self):
        """get_projection west should return string given valid length"""
        grid = WaldorfGrid(["ab"], 1, 2)

        result = grid.get_char(0, 1)
        self.assertEqual("b", result)

        projection = grid.get_projection(0, 1, 1, Direction.WEST)
        self.assertEqual("b", projection)

        projection = grid.get_projection(0, 1, 2, Direction.WEST)
        self.assertEqual("ba", projection)

    def test_010(self):
        """get_projection west should return string given longer valid length"""
        grid = WaldorfGrid(["abcdefg"], 1, 7)

        result = grid.get_char(0, 4)
        self.assertEqual("e", result)

        projection = grid.get_projection(0, 4, 3, Direction.WEST)
        self.assertEqual("edc", projection)

    def test_011(self):
        """get_projection north should none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.NORTH)
        self.assertEqual(None, projection)

    def test_012(self):
        """get_projection north should value given valid length"""
        grid = WaldorfGrid(["b", "a"], 2, 1)

        result = grid.get_char(1, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(1, 0, 2, Direction.NORTH)
        self.assertEqual("ab", projection)

    def test_013(self):
        """get_projection north should value given longer valid length"""
        grid = WaldorfGrid(["d", "c", "b", "a"], 4, 1)

        result = grid.get_char(3, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(3, 0, 3, Direction.NORTH)
        self.assertEqual("abc", projection)

    def test_014(self):
        """get_projection south should none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.SOUTH)
        self.assertEqual(None, projection)

    def test_015(self):
        """get_projection south should value given valid length"""
        grid = WaldorfGrid(["a", "b"], 2, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 1, Direction.SOUTH)
        self.assertEqual("a", projection)

        projection = grid.get_projection(0, 0, 2, Direction.SOUTH)
        self.assertEqual("ab", projection)

    def test_016(self):
        """get_projection south should value given longer valid length"""
        grid = WaldorfGrid(["a", "b", "c", "d"], 4, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 3, Direction.SOUTH)
        self.assertEqual("abc", projection)

    # **

    def test_017(self):
        """get_projection south east should return none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.SOUTH_EAST)
        self.assertEqual(None, projection)

    def test_018(self):
        """get_projection south east should value given valid length"""
        grid = WaldorfGrid(["ac", "eb"], 2, 2)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 1, Direction.SOUTH_EAST)
        self.assertEqual("a", projection)

        projection = grid.get_projection(0, 0, 2, Direction.SOUTH_EAST)
        self.assertEqual("ab", projection)

    def test_019(self):
        """get_projection south should value given longer valid length"""
        grid = WaldorfGrid(["axy", "xby", "xyc"], 3, 3)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 3, Direction.SOUTH_EAST)
        self.assertEqual("abc", projection)

