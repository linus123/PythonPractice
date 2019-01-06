import unittest

from file_fragmentation import assemble_fragments, get_unique_combinations


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

    def test_005(self):
        """Should wor for just 2 values"""
        result = assemble_fragments([
            "01",
            "10",
        ])

        self.assertIn(result,["0110", "1001"])

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


