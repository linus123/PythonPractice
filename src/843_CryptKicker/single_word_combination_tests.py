import unittest

from crypt_kicker import EncryptedWordWithOptions, WordMap, SingleWord


class SingleWordComboTests(unittest.TestCase):
    def test_recurse_001(self):
        word_sw = SingleWord("foobar")

        decode_words_array = [EncryptedWordWithOptions(word_sw)]

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array))

        self.assertEqual(0, len(array_of_dicts))

    def test_recurse_002(self):
        word_sw = SingleWord("foobar")
        enc_word = EncryptedWordWithOptions(word_sw)

        enc_word.add_solution_word(SingleWord("bcculs"))
        decode_words_array = [enc_word]

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array))

        self.assertEqual(0, len(array_of_dicts))

    def test_recurse_003(self):
        word_sw = SingleWord("foobar")

        enc_word = EncryptedWordWithOptions(word_sw)
        enc_word.add_solution_word(SingleWord("bcculs"))
        enc_word.add_solution_word(SingleWord("qwwert"))
        decode_words_array = [enc_word]

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array))

        self.assertEqual(2, len(array_of_dicts))

        GuessDictionaryAssertBuilder(array_of_dicts[0], self)\
            .assert_word_with_options_matches(word_sw, ["bcculs"])

        GuessDictionaryAssertBuilder(array_of_dicts[1], self)\
            .assert_word_with_options_matches(word_sw, ["qwwert"])

    def test_recurse_004(self):
        word1_sw = SingleWord("a")

        enc_word01 = EncryptedWordWithOptions(word1_sw)
        enc_word01.add_solution_word(SingleWord("i"))

        word2_sw = SingleWord("foobar")

        enc_word02 = EncryptedWordWithOptions(word2_sw)
        enc_word02.add_solution_word(SingleWord("bcculs"))
        enc_word02.add_solution_word(SingleWord("qwwert"))
        decode_words_array = [enc_word01, enc_word02]

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array))

        self.assertEqual(2, len(array_of_dicts))

        GuessDictionaryAssertBuilder(array_of_dicts[0], self)\
            .assert_word_with_options_matches(word1_sw, ["i"])\
            .assert_word_with_options_matches(word2_sw, ["bcculs"])

        GuessDictionaryAssertBuilder(array_of_dicts[1], self)\
            .assert_word_with_options_matches(word1_sw, ["i"])\
            .assert_word_with_options_matches(word2_sw, ["qwwert"])

    def test_recurse_005(self):
        word1_sw = SingleWord("a")

        enc_word01 = EncryptedWordWithOptions(word1_sw)
        enc_word01.add_solution_word(SingleWord("i"))
        enc_word01.add_solution_word(SingleWord("j"))

        word2_sw = SingleWord("foobar")

        enc_word02 = EncryptedWordWithOptions(word2_sw)
        enc_word02.add_solution_word(SingleWord("bcculs"))
        enc_word02.add_solution_word(SingleWord("qwwert"))

        decode_words_array = [enc_word01, enc_word02]

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array))

        self.assertEqual(4, len(array_of_dicts))

        GuessDictionaryAssertBuilder(array_of_dicts[0], self)\
            .assert_word_with_options_matches(word1_sw, ["i"])\
            .assert_word_with_options_matches(word2_sw, ["bcculs", "qwwert"])

        GuessDictionaryAssertBuilder(array_of_dicts[1], self)\
            .assert_word_with_options_matches(word1_sw, ["j"])\
            .assert_word_with_options_matches(word2_sw, ["bcculs", "qwwert"])

        GuessDictionaryAssertBuilder(array_of_dicts[2], self)\
            .assert_word_with_options_matches(word1_sw, ["i", "j"])\
            .assert_word_with_options_matches(word2_sw, ["bcculs"])

        GuessDictionaryAssertBuilder(array_of_dicts[3], self)\
            .assert_word_with_options_matches(word1_sw, ["i", "j"])\
            .assert_word_with_options_matches(word2_sw, ["qwwert"])

    def test_recurse_005(self):
        word1_sw = SingleWord("a")

        enc_word01 = EncryptedWordWithOptions(word1_sw)
        enc_word01.add_solution_word(SingleWord("a"))
        enc_word01.add_solution_word(SingleWord("b"))
        enc_word01.add_solution_word(SingleWord("c"))

        word2_sw = SingleWord("foobar")

        enc_word02 = EncryptedWordWithOptions(word2_sw)
        enc_word02.add_solution_word(SingleWord("x"))
        enc_word02.add_solution_word(SingleWord("y"))
        enc_word02.add_solution_word(SingleWord("z"))

        decode_words_array = [enc_word01, enc_word02]

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array))

        self.assertEqual(6, len(array_of_dicts))

        GuessDictionaryAssertBuilder(array_of_dicts[0], self)\
            .assert_word_with_options_matches(word1_sw, ["a"])\
            .assert_word_with_options_matches(word2_sw, ["x", "y", "z"])

        GuessDictionaryAssertBuilder(array_of_dicts[1], self)\
            .assert_word_with_options_matches(word1_sw, ["b"])\
            .assert_word_with_options_matches(word2_sw, ["x", "y", "z"])

        GuessDictionaryAssertBuilder(array_of_dicts[2], self)\
            .assert_word_with_options_matches(word1_sw, ["c"])\
            .assert_word_with_options_matches(word2_sw, ["x", "y", "z"])

        GuessDictionaryAssertBuilder(array_of_dicts[3], self)\
            .assert_word_with_options_matches(word1_sw, ["a", "b", "c"])\
            .assert_word_with_options_matches(word2_sw, ["x"])

        GuessDictionaryAssertBuilder(array_of_dicts[4], self)\
            .assert_word_with_options_matches(word1_sw, ["a", "b", "c"])\
            .assert_word_with_options_matches(word2_sw, ["y"])

        GuessDictionaryAssertBuilder(array_of_dicts[5], self)\
            .assert_word_with_options_matches(word1_sw, ["a", "b", "c"])\
            .assert_word_with_options_matches(word2_sw, ["z"])

    def test_recurse_006(self):
        word1_sw = SingleWord("foo")

        enc_word01 = EncryptedWordWithOptions(word1_sw)
        enc_word01.add_solution_word(SingleWord("a"))
        enc_word01.add_solution_word(SingleWord("b"))

        word2_sw = SingleWord("baz")

        enc_word02 = EncryptedWordWithOptions(word2_sw)
        enc_word02.add_solution_word(SingleWord("x"))
        enc_word02.add_solution_word(SingleWord("y"))

        word3_sw = SingleWord("bar")

        enc_word03 = EncryptedWordWithOptions(word3_sw)
        enc_word03.add_solution_word(SingleWord("e"))
        enc_word03.add_solution_word(SingleWord("f"))

        decode_words_array = [enc_word01, enc_word02, enc_word03]

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array))

        self.assertEqual(6, len(array_of_dicts))

        GuessDictionaryAssertBuilder(array_of_dicts[0], self)\
            .assert_word_with_options_matches(word1_sw, ["a"])\
            .assert_word_with_options_matches(word2_sw, ["x", "y"])\
            .assert_word_with_options_matches(word3_sw, ["e", "f"])

        GuessDictionaryAssertBuilder(array_of_dicts[1], self)\
            .assert_word_with_options_matches(word1_sw, ["b"])\
            .assert_word_with_options_matches(word2_sw, ["x", "y"])\
            .assert_word_with_options_matches(word3_sw, ["e", "f"])

        GuessDictionaryAssertBuilder(array_of_dicts[2], self)\
            .assert_word_with_options_matches(word1_sw, ["a", "b"])\
            .assert_word_with_options_matches(word2_sw, ["x"])\
            .assert_word_with_options_matches(word3_sw, ["e", "f"])

        GuessDictionaryAssertBuilder(array_of_dicts[3], self)\
            .assert_word_with_options_matches(word1_sw, ["a", "b"])\
            .assert_word_with_options_matches(word2_sw, ["y"])\
            .assert_word_with_options_matches(word3_sw, ["e", "f"])

        GuessDictionaryAssertBuilder(array_of_dicts[4], self)\
            .assert_word_with_options_matches(word1_sw, ["a", "b"])\
            .assert_word_with_options_matches(word2_sw, ["x", "y"])\
            .assert_word_with_options_matches(word3_sw, ["e"])

        GuessDictionaryAssertBuilder(array_of_dicts[5], self)\
            .assert_word_with_options_matches(word1_sw, ["a", "b"])\
            .assert_word_with_options_matches(word2_sw, ["x", "y"])\
            .assert_word_with_options_matches(word3_sw, ["f"])

    def assert_word_with_options_matches(self, target: EncryptedWordWithOptions, single_word: SingleWord, solution_words: list):
        self.assertEqual(single_word.word, target.get_encrypted_word())

        self.assertEqual(len(solution_words), target.get_solution_word_count())

        for index in range(len(solution_words)):
            self.assertTrue(target.has_solution_word(solution_words[index]))


class GuessDictionaryAssertBuilder:

    def __init__(self, dictionary: dict, test_case: unittest.TestCase) -> None:
        self.dictionary = dictionary
        self.test_case = test_case

    def assert_word_with_options_matches(self, single_word: SingleWord, solution_words: list):
        target = self.dictionary[single_word.word]

        self.test_case.assertEqual(single_word.word, target.get_encrypted_word())

        self.test_case.assertEqual(len(solution_words), target.get_solution_word_count())

        for index in range(len(solution_words)):
            self.test_case.assertEqual(solution_words[index], target.get_solution_word_at_index(index))

        return self


