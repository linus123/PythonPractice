import math
import sys


def find_sum_of_distances(numbers: list):
    numbers.sort()

    median_index = math.floor(len(numbers) / 2)

    left_median_dist = calculate_distances(numbers, numbers[median_index])

    return left_median_dist


def calculate_distances(numbers: list, target: int) -> int:
    sum_of_distances = 0

    for number in numbers:
        distance = abs(number - target)
        sum_of_distances += distance

    return sum_of_distances


def run_from_standard_in():

    first_line = sys.stdin.readline()
    number_of_test_cases = int(first_line.strip())

    for test_case_counter in range(number_of_test_cases):

        current_line = sys.stdin.readline().strip()
        line_split = current_line.split(" ")

        number_count = int(line_split[0])

        numbers = []

        for i in range(number_count):
            numbers.append(int(line_split[i + 1]))

        min_dist = find_sum_of_distances(numbers)

        print(min_dist)

def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()