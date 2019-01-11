import math
import unittest


class VitosFamilyTests(unittest.TestCase):
    def test_001(self):
        """Should return the correct answer given the first sample problem"""

        numbers = [2, 4]
        result = find_sum_of_distances(numbers)
        self.assertEqual(2, result)

    def test_002(self):
        """Should return the correct answer for the scond sample program"""

        numbers = [2, 4, 6]
        result = find_sum_of_distances(numbers)
        self.assertEqual(4, result)


def find_sum_of_distances(numbers: list):
    numbers.sort()

    sum_for_ave = 0

    for number in numbers:
        sum_for_ave += number

    average = math.ceil(sum_for_ave / len(numbers))

    min_distance = calculate_distances(numbers, average)

    right_dis = calculate_distances(numbers, average + 1)

    if right_dis < min_distance:
        min_distance = right_dis

    left_dis = calculate_distances(numbers, average - 1)

    if left_dis < min_distance:
        min_distance = left_dis

    return min_distance


def calculate_distances(numbers: list, target: int) -> int:
    sum_of_distances = 0

    for number in numbers:
        distance = abs(number - target)
        sum_of_distances += distance

    return sum_of_distances
