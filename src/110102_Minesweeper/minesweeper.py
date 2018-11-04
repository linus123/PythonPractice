import sys


def count_mines(height, width, field):

    def is_on_field(x, y):
        if x < 0:
            return False

        if y < 0:
            return False

        if x >= width:
            return False

        if y >= height:
            return False

        return True

    def create_result_field():
        y = 0

        new_field = []

        while y < height:
            new_field.append(list("0" * width))
            y += 1

        return new_field

    def is_mine(x, y):

        if is_on_field(x, y) and field[y][x] == "*":
            return True

        return False

    def count_surrounding_mines(x, y):
        mine_count = 0

        if is_mine(x - 1, y - 1):
            mine_count += 1

        if is_mine(x, y - 1):
            mine_count += 1

        if is_mine(x + 1, y - 1):
            mine_count += 1

        if is_mine(x - 1, y):
            mine_count += 1

        if is_mine(x + 1, y):
            mine_count += 1

        if is_mine(x - 1, y + 1):
            mine_count += 1

        if is_mine(x, y + 1):
            mine_count += 1

        if is_mine(x + 1, y + 1):
            mine_count += 1

        return mine_count

    def convert_to_array_of_strings(result_field):
        y = 0

        new_field = []

        while y < height:
            new_field.append("".join(result_field[y]))
            y += 1

        return new_field

    y = 0

    result_field = create_result_field()

    while y < height:

        x = 0

        while x < width:

            if is_mine(x, y):
                result_field[y][x] = "*"
            else:
                result_field[y][x] = str(count_surrounding_mines(x, y))

            x += 1

        y += 1

    return convert_to_array_of_strings(result_field)

####################################################


def read_from_standard_in():
    field_size_line = get_next_non_blank_line_from_standard_in()

    field_counter = 1

    while has_more_grids(field_size_line):

        split_result = field_size_line.split()

        number_of_rows = int(split_result[0])
        number_of_columns = int(split_result[1])

        field = read_field_from_standard_in(number_of_rows)

        result = count_mines(number_of_rows, number_of_columns, field)

        print("Field #{0}:".format(field_counter))

        print_result_grid(result)

        field_size_line = get_next_non_blank_line_from_standard_in()

        if has_more_grids(field_size_line):
            print()

        field_counter += 1


def print_result_grid(result):
    for result_line in result:
        print(result_line)


def read_field_from_standard_in(number_of_rows):
    field = []

    for line_counter in range(number_of_rows):
        field_line = sys.stdin.readline().rstrip()
        field.append(field_line)

    return field


def has_more_grids(line):
    return line != "0 0"


def get_next_non_blank_line_from_standard_in():
    line = sys.stdin.readline().rstrip()

    while line == "" :
        line = sys.stdin.readline().rstrip()

    return line


def main():
    read_from_standard_in()


if __name__ == '__main__':
    main()

