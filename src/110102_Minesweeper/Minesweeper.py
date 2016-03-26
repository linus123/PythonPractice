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

# def main():
#     threeNPLus1FromStdIn()
#
# if __name__ == '__main__':
#     main()

