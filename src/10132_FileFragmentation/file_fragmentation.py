import math
import sys


def assemble_fragments(fragments: list):

    if len(fragments) == 1:
        return fragments[0]

    by_count_dict = {}

    max_len = 0
    min_len = 500

    for index in range(len(fragments)):

        fragment = fragments[index]
        frag_len = len(fragment)

        if frag_len in by_count_dict:
            by_count_dict[frag_len].append(fragment)
        else:
            by_count_dict[frag_len] = [fragment]

        if max_len < frag_len:
            max_len = frag_len

        if min_len > frag_len:
            min_len = frag_len

    half_count = math.ceil((max_len - min_len + 1) / 2.0)

    inter_set = None

    for half_index in range(0, half_count):

        key1 = min_len + half_index
        key2 = max_len - half_index

        if key1 not in by_count_dict:
            continue

        left_list = by_count_dict[key1]

        if key2 not in by_count_dict:
            continue

        right_list = by_count_dict[key2]

        outer_set = get_all_combinations(left_list, right_list)

        if inter_set is None:
            inter_set = outer_set
        else:
            inter_set = inter_set.intersection(outer_set)

    return next(iter(inter_set))


def get_all_combinations(lst1: list, lst2: list) -> set:
    set1 = get_unique_combinations(lst1, lst2)
    set2 = get_unique_combinations(lst2, lst1)

    return set1.union(set2)


def get_unique_combinations(lst1: list, lst2: list) -> set:

    unique_items = set()

    for item1 in lst1:
        for item2 in lst2:
            unique_items.add(item1 + item2)

    return unique_items


def run_from_standard_in():

    first_line = sys.stdin.readline()
    number_of_test_cases = int(first_line.strip())
    blank_line = sys.stdin.readline()

    for test_case_counter in range(number_of_test_cases):
        fragments = []

        line = sys.stdin.readline().strip()
        while line != "":
            fragments.append(line)
            line = sys.stdin.readline().strip()

        solution = assemble_fragments(fragments)

        print(solution)

        if test_case_counter < number_of_test_cases - 1:
            print("")


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()
