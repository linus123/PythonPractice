from enum import Enum


class Direction(Enum):
    NORTH = 1,
    SOUTH = 2,
    EAST = 3,
    WEST = 4,
    NORTH_WEST = 5,
    NORTH_EAST = 6,
    SOUTH_WEST = 7,
    SOUTH_EAST = 8


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

    def get_projection(self, row_index: int, col_index: int, length: int, direction: Direction):

        if direction == Direction.EAST:
            if col_index + length > self.column_count:
                return None

            return self.__grid[row_index][col_index: col_index + length]

        if direction == Direction.WEST:
            if col_index - length + 1 < 0:
                return None

            raw_string = self.__grid[row_index][col_index - length + 1: col_index + 1]

            return raw_string[::-1]

    def get_projection_north(self, row_index: int, col_index: int, length: int):
        return None