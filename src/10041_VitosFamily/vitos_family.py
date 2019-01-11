import math


def find_sum_of_distances(numbers: list):
    numbers.sort()

    average = calculate_average(numbers)

    min_distance = calculate_distances(numbers, average)

    right_dist = calculate_distances(numbers, average + 1)
    right_smaller = False

    if right_dist < min_distance:
        min_distance = right_dist
        right_smaller = True

    left_dist = calculate_distances(numbers, average - 1)
    left_smaller = False

    if left_dist < min_distance:
        min_distance = left_dist
        left_smaller = True

    if not right_smaller and not left_smaller:
        return min_distance

    if right_smaller:
        return chase_direction(average, min_distance, numbers, 1)

    if left_smaller:
        return chase_direction(average, min_distance, numbers, -1)

    return min_distance


def chase_direction(average, min_distance, numbers, direction):
    diff_counter = 2 * direction
    current_target = average + diff_counter
    current_dist = calculate_distances(numbers, current_target)
    while current_dist <= min_distance:
        min_distance = current_dist
        diff_counter += direction
        current_target = average + diff_counter
        current_dist = calculate_distances(numbers, current_target)
    return min_distance


def calculate_average(numbers):
    sum_for_ave = 0
    for number in numbers:
        sum_for_ave += number
    average = math.ceil(sum_for_ave / len(numbers))
    return average


def calculate_distances(numbers: list, target: int) -> int:
    sum_of_distances = 0

    for number in numbers:
        distance = abs(number - target)
        sum_of_distances += distance

    return sum_of_distances
