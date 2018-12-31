import unittest

from wheres_waldorf import WaldorfGrid, Direction, find_waldorf


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

    # **

    def test_020(self):
        """get_projection north west should return none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.NORTH_WEST)
        self.assertEqual(None, projection)

    def test_021(self):
        """get_projection north west should value given valid length"""
        grid = WaldorfGrid(["bc", "ea"], 2, 2)

        result = grid.get_char(1, 1)
        self.assertEqual("a", result)

        projection = grid.get_projection(1, 1, 1, Direction.NORTH_WEST)
        self.assertEqual("a", projection)

        projection = grid.get_projection(1, 1, 2, Direction.NORTH_WEST)
        self.assertEqual("ab", projection)

    def test_022(self):
        """get_projection north west should value given longer valid length"""
        grid = WaldorfGrid(["cxy", "xby", "xya"], 3, 3)

        result = grid.get_char(2, 2)
        self.assertEqual("a", result)

        projection = grid.get_projection(2, 2, 3, Direction.NORTH_WEST)
        self.assertEqual("abc", projection)

    # **

    def test_023(self):
        """get_projection north east should return none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.NORTH_EAST)
        self.assertEqual(None, projection)

    def test_024(self):
        """get_projection north east should value given valid length"""
        grid = WaldorfGrid([
            "yb",
            "ax"], 2, 2)

        result = grid.get_char(1, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(1, 0, 1, Direction.NORTH_EAST)
        self.assertEqual("a", projection)

        projection = grid.get_projection(1, 0, 2, Direction.NORTH_EAST)
        self.assertEqual("ab", projection)

    def test_025(self):
        """get_projection north east should value given longer valid length"""
        grid = WaldorfGrid([
            "yxc",
            "xby",
            "axy"], 3, 3)

        result = grid.get_char(2, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(2, 0, 3, Direction.NORTH_EAST)
        self.assertEqual("abc", projection)

    # **

    def test_026(self):
        """get_projection south west should return none given long length"""
        grid = WaldorfGrid(["a"], 1, 1)

        result = grid.get_char(0, 0)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 0, 2, Direction.SOUTH_WEST)
        self.assertEqual(None, projection)

    def test_027(self):
        """get_projection south west should value given valid length"""
        grid = WaldorfGrid([
            "ya",
            "bx"], 2, 2)

        result = grid.get_char(0, 1)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 1, 1, Direction.SOUTH_WEST)
        self.assertEqual("a", projection)

        projection = grid.get_projection(0, 1, 2, Direction.SOUTH_WEST)
        self.assertEqual("ab", projection)

    def test_028(self):
        """get_projection south west should value given longer valid length"""
        grid = WaldorfGrid([
            "yxa",
            "xby",
            "cxy"], 3, 3)

        result = grid.get_char(0, 2)
        self.assertEqual("a", result)

        projection = grid.get_projection(0, 2, 3, Direction.SOUTH_WEST)
        self.assertEqual("abc", projection)

    def test_029(self):
        """find_waldorf should return empty array given invalid grid"""
        grid = WaldorfGrid([""], 1, 0)
        result = list(find_waldorf(grid, []))
        self.assertEqual(0, len(result))

    def test_030(self):
        """find_waldorf should return empty array no words"""
        grid = WaldorfGrid(["a"], 1, 1)
        result = list(find_waldorf(grid, []))
        self.assertEqual(0, len(result))

    def test_031(self):
        """Should find words given sample test"""
        ar = ["abcDEFGhigg".lower(),
              "hEbkWalDork".lower(),
              "FtyAwaldORm".lower(),
              "FtsimrLqsrc".lower(),
              "byoArBeDeyv".lower(),
              "Klcbqwikomk".lower(),
              "strEBGadhrb".lower(),
              "yUiqlxcnBjf".lower()
              ]

        grid = WaldorfGrid(ar, 8, 11)

        words = ["Waldorf".lower(),
                 "Bambi".lower(),
                 "Betty".lower(),
                 "Dagbert".lower()
                 ]

        result = list(find_waldorf(grid, words))

        self.assertEqual(4, len(result))

        self.assertEqual(2, result[0][0])
        self.assertEqual(5, result[0][1])

        self.assertEqual(2, result[1][0])
        self.assertEqual(3, result[1][1])

        self.assertEqual(1, result[2][0])
        self.assertEqual(2, result[2][1])

        self.assertEqual(7, result[3][0])
        self.assertEqual(8, result[3][1])
