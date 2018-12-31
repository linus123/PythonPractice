import sys
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

    def is_valid(self) -> bool:
        if self.column_count <= 0:
            return False

        if self.__grid[0].strip() == "":
            return False

        return True

    def get_char(self, row_index: int, col_index: int) -> chr:
        if not self.is_valid():
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

        if direction == Direction.SOUTH:
            if row_index + length > self.row_count:
                return None

            char_array = []

            for row_count in range(row_index, row_index + length):
                char_array.append(self.__grid[row_count][col_index])

            return "".join(char_array)

        if direction == Direction.NORTH:
            if row_index - length + 1 < 0:
                return None

            char_array = []

            for row_count in range(row_index, row_index - length, -1):
                char_array.append(self.__grid[row_count][col_index])

            return "".join(char_array)

        if direction == Direction.SOUTH_EAST:
            if row_index + length > self.row_count:
                return None

            if col_index + length > self.column_count:
                return None

            char_array = []

            for len_count in range(length):
                char_array.append(self.__grid[row_index + len_count][col_index + len_count])

            return "".join(char_array)

        if direction == Direction.NORTH_WEST:
            if row_index - length + 1 < 0:
                return None

            if col_index - length + 1 < 0:
                return None

            char_array = []

            for len_count in range(length):
                char_array.append(self.__grid[row_index - len_count][col_index - len_count])

            return "".join(char_array)

        if direction == Direction.NORTH_EAST:
            if row_index - length + 1 < 0:
                return None

            if col_index + length > self.column_count:
                return None

            char_array = []

            for len_count in range(length):
                char_array.append(self.__grid[row_index - len_count][col_index + len_count])

            return "".join(char_array)

        if direction == Direction.SOUTH_WEST:
            if row_index + length > self.row_count:
                return None

            if col_index - length + 1 < 0:
                return None

            char_array = []

            for len_count in range(length):
                char_array.append(self.__grid[row_index + len_count][col_index - len_count])

            return "".join(char_array)

        raise ValueError("Invalid Direction")


def find_waldorf(grid: WaldorfGrid, words: list):

    if not grid.is_valid():
        return []

    if len(words) <= 0:
        return []

    word_dic = {}

    for word in words:
        first_letter = word[0]

        if first_letter in word_dic:
            word_dic[first_letter].append(word)
        else:
            word_dic[first_letter] = [word]

    found_words = {}

    for row_index in range(grid.row_count):
        for col_index in range(grid.column_count):
            letter = grid.get_char(row_index, col_index)

            if letter in word_dic:
                for word in word_dic[letter]:

                    if word in found_words:
                        continue

                    for dir in Direction:
                        proj = grid.get_projection(row_index, col_index, len(word), dir)
                        if proj == word:
                            found_words[word] = (row_index + 1, col_index + 1)

    for word in words:
        yield found_words[word]


def run_from_standard_in():

    first_line = sys.stdin.readline()
    number_of_test_cases = int(first_line.strip())

    for test_case_counter in range(number_of_test_cases):
        blank_line = sys.stdin.readline()

        grid_dim_line = sys.stdin.readline().strip()
        grid_dim_ar = grid_dim_line.split(" ")

        row_count = int(grid_dim_ar[0])
        col_count = int(grid_dim_ar[1])

        grid_array = []

        for row_counter in range(row_count):
            grid_array.append(sys.stdin.readline().strip().lower())

        grid = WaldorfGrid(grid_array, row_count, col_count)

        word_count_line = sys.stdin.readline()
        number_of_words = int(word_count_line.strip())

        word_array = []

        for word_counter in range(number_of_words):
            word_array.append(sys.stdin.readline().strip().lower())

        word_locations = find_waldorf(grid, word_array)

        for loc in word_locations:
            print("%i %i" % loc)

        if test_case_counter < number_of_test_cases - 1:
            print("")

def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()