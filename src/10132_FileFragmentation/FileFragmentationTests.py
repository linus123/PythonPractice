import math
import unittest


class FileFragmentationTests(unittest.TestCase):
    def test_001(self):
        """Should work with just 1 fragment"""

        result = assemble_fragments(["1"])
        self.assertEqual("1", result)

        result = assemble_fragments(["01"])
        self.assertEqual("01", result)

    def test_002(self):
        """Should work with 2 fragments"""

        result = assemble_fragments(["10", "01"])
        self.assertIn(result, ["1001", "0110"])

    def test_003(self):
        """Should work with a even number of lengths"""

        result = assemble_fragments([
            "11",
            "0",
            "11111",
            "0111",
        ])

        self.assertEqual("011111", result)

    def test_004(self):
        """Should work with the sample in the document"""
        result = assemble_fragments([
            "011",
            "0111",
            "01110",
            "111",
            "0111",
            "10111"
        ])

        self.assertEqual("01110111", result)

    def test_100(self):
        """get_unique_combinations should return every combination"""

        results = get_unique_combinations(
            ["11", "01"],
            ["1", "0"])

        self.assertEqual(4, len(results))

        self.assertIn("111", results)
        self.assertIn("110", results)
        self.assertIn("011", results)
        self.assertIn("010", results)

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

    for foo in range(0, half_count):

        key1 = min_len + foo
        key2 = max_len - foo

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
