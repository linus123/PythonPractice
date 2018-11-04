import sys


def is_jolly_jumper(values):
    values_len = len(values)

    if values_len <= 0:
        raise ValueError("values must have at least one value")

    if values_len == 1:
        return True

    differences = {}

    for current_index in range(values_len - 1):
        next_index = current_index + 1

        current_difference = get_abs_diff(
            values[current_index],
            values[next_index])

        differences[current_difference] = 1

    if is_difference_values_len_minus_one(differences, values_len):
        return False

    if has_successive_elements(differences, values_len):
        return True

    return False


def has_successive_elements(differences, values_len):
    for count in range(values_len - 1):
        if (count + 1) not in differences:
            return False

    return True


def is_difference_values_len_minus_one(diff_dic, values_len):
    return len(diff_dic) != (values_len - 1)


def get_abs_diff(current_value, next_value):
    return abs(current_value - next_value)


def run_from_standard_in():

    for values_string in sys.stdin:
        split_values = values_string.strip().split(' ')

        values = [int(i) for i in split_values[1:]]

        if is_jolly_jumper(values):
            print("Jolly")
        else:
            print("Not jolly")


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()
