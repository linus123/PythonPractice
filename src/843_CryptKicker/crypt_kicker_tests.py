import unittest

from crypt_kicker import crypt_decrypt


class CryptKickerTests(unittest.TestCase):
    def test_001(self):
        """Should return the empty string given an empty string"""
        dictionary = []

        result = crypt_decrypt("", dictionary)
        self.assertEqual("", result)

        result = crypt_decrypt(" ", dictionary)
        self.assertEqual("", result)

    def test_002(self):
        """Should return the empty string given an empty string and anything in the decrypted words"""
        dictionary = ["some stuff"]

        result = crypt_decrypt("", dictionary)
        self.assertEqual("", result)

        result = crypt_decrypt("  ", dictionary)
        self.assertEqual("", result)

    def test_003(self):
        """Should return the expected result given a single letter for encrypted and decrypted words"""
        dictionary = ["a"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("a", result)

        dictionary = ["c"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("c", result)

        dictionary = ["e"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("e", result)

    def test_004(self):
        """Should return first possible result when single letter has more than one solution"""
        dictionary = ["a", "b"]
        result = crypt_decrypt("c", dictionary)
        self.assertEqual("a", result)

        dictionary = ["c", "d"]
        result = crypt_decrypt("a", dictionary)
        self.assertEqual("c", result)

    def test_005(self):
        """Should return expected solution given two single letter dictionary and two single letter encrypted words"""
        dictionary = ["a", "b"]

        result = crypt_decrypt("c d", dictionary)
        self.assertEqual("a b", result)

        result = crypt_decrypt("d c", dictionary)
        self.assertEqual("a b", result)

        result = crypt_decrypt("c d d", dictionary)
        self.assertEqual("a b b", result)

        result = crypt_decrypt("c c d", dictionary)
        self.assertEqual("a a b", result)

    def test_006(self):
        """Should return no solution given two single letter words without single solution"""
        dictionary = ["a"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

        dictionary = ["z"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

    def test_007(self):
        """Should return expected solution given two single letter words"""
        dictionary = ["a"]
        result = crypt_decrypt("c c", dictionary)
        self.assertEqual("a a", result)

    def test_008(self):
        """Should return expected solution given three single letter words"""
        dictionary = ["a"]
        result = crypt_decrypt("c c c", dictionary)
        self.assertEqual("a a a", result)

    def test_009(self):
        """Should not return solution given two letter words with no solution"""
        dictionary = ["aa"]
        result = crypt_decrypt("bb cc", dictionary)
        self.assertEqual("** **", result)

    def test_010(self):
        """Should return solution with three letters"""
        dictionary = ["aab", "aac"]
        result = crypt_decrypt("xxy xxz", dictionary)
        self.assertEqual("aab aac", result)

    def test_011(self):
        """Should not return solution when two letter words have no solution can a change in letters"""
        dictionary = ["ab"]
        result = crypt_decrypt("bc cd", dictionary)
        self.assertEqual("** **", result)

        dictionary = ["ab"]
        result = crypt_decrypt("bc bd", dictionary)
        self.assertEqual("** **", result)

        dictionary = ["ab"]
        result = crypt_decrypt("cc dd", dictionary)
        self.assertEqual("** **", result)

    def test_012(self):
        """Should return expected solution when two letter words have single solution for both words"""
        dictionary = ["aa"]
        result = crypt_decrypt("bb bb", dictionary)
        self.assertEqual("aa aa", result)

    def test_013(self):
        """Should return expected solution two letter words have single solution with different letters"""
        dictionary = ["ab"]
        result = crypt_decrypt("bc bc", dictionary)
        self.assertEqual("ab ab", result)

    def test_014(self):
        """Should return expected solution when duplication decrypted words are given"""
        dictionary = ["ab", "ab"]
        result = crypt_decrypt("xy", dictionary)
        self.assertEqual("ab", result)

    def test_015(self):
        """Should return one of multiple solutions with two letters"""
        dictionary = ["ab", "cd"]
        result = crypt_decrypt("xy xy", dictionary)
        self.assertEqual("ab ab", result)

        dictionary = ["cd", "ab"]
        result = crypt_decrypt("xy xy", dictionary)
        self.assertEqual("cd cd", result)

    def test_016(self):
        """Should not return solution when encrypted word length do not match decrypted word length"""
        dictionary = ["a"]
        result = crypt_decrypt("xy", dictionary)
        self.assertEqual("**", result)

        dictionary = ["ab"]
        result = crypt_decrypt("xyz", dictionary)
        self.assertEqual("***", result)

    def test_017(self):
        """Should not return solution when words are not letter possible"""
        dictionary = ["ab"]
        result = crypt_decrypt("xx", dictionary)
        self.assertEqual("**", result)

        dictionary = ["abc"]
        result = crypt_decrypt("xxy", dictionary)
        self.assertEqual("***", result)

    def test_018(self):
        """Should not return solution word is not letter possible with duplicate letters"""
        dictionary = ["aba"]
        result = crypt_decrypt("xyx", dictionary)
        self.assertEqual("aba", result)

    def test_019(self):
        """Should return solution when one of multiple solutions with two letters where first decrypted word is rejected"""
        dictionary = ["xx", "cd"]
        result = crypt_decrypt("xy", dictionary)
        self.assertEqual("cd", result)

    def test_020(self):
        """Should return solution with single encrypted word and single decrypted word"""
        dictionary = ["abc"]
        result = crypt_decrypt("xyz", dictionary)
        self.assertEqual("abc", result)

    def test_021(self):
        """Should return solution there are more that two solutions"""
        dictionary = ["ab", "bc", "de", "fg"]
        result = crypt_decrypt("hi hi", dictionary)
        self.assertEqual("ab ab", result)

    def test_022(self):
        """Should use single option as a way of clearing all other options that match by letter"""
        dictionary = ["bc", "ab", "bb"]
        result = crypt_decrypt("yy xy yz", dictionary)
        self.assertEqual("bb ab bc", result)

    def test_023(self):
        """Should find solution that ONLY is solved by letter maps"""
        dictionary = ["bc", "ab"]
        result = crypt_decrypt("xy yz", dictionary)
        self.assertEqual("ab bc", result)

    def test_024(self):
        """Should return solution by using letters that match across different words"""
        dictionary = ["ef", "ab", "bc"]
        result = crypt_decrypt("xy yz", dictionary)
        self.assertEqual("ab bc", result)

    def test_024(self):
        """Should leave spaces in solution intact"""
        dictionary = ["cd"]
        result = crypt_decrypt("ab  ab", dictionary)
        self.assertEqual("cd  cd", result)

    def test_024(self):
        """Should leave spaces in no solution intact"""
        dictionary = ["xx"]
        result = crypt_decrypt("ab    ab", dictionary)
        self.assertEqual("**    **", result)

    def test_sample_input_should_pass(self):
        """Should return expected solution from the directions samle"""
        dictionary = ["and", "dick", "jane", "puff", "spot", "yertle"]

        result = crypt_decrypt("bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn", dictionary)
        self.assertEqual("dick and jane and puff and spot and yertle", result)

        result = crypt_decrypt("xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd", dictionary)
        self.assertEqual("**** *** **** *** **** *** **** *** ******", result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()

