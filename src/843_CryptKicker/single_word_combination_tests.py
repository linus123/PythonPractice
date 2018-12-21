import unittest

from crypt_kicker import EncryptedWordWithOptions, WordMap, SingleWord


class SingleWordComboTests(unittest.TestCase):
    def test_recurse_001(self):
        word_sw = SingleWord("foobar")

        decode_words_array = [EncryptedWordWithOptions(word_sw)]
        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(0, len(array_of_dicts))

    def test_recurse_002(self):
        word_sw = SingleWord("foobar")
        enc_word = EncryptedWordWithOptions(word_sw)

        enc_word.add_solution_word(SingleWord("bcculs"))
        decode_words_array = [enc_word]
        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(1, len(array_of_dicts))

        GuessDictionaryAssertBuilder(array_of_dicts[0], self)\
            .assert_word_with_options_matches(word_sw, ["bcculs"])

    def test_recurse_003(self):
        word_sw = SingleWord("foobar")

        enc_word = EncryptedWordWithOptions(word_sw)
        enc_word.add_solution_word(SingleWord("bcculs"))
        enc_word.add_solution_word(SingleWord("qwwert"))
        decode_words_array = [enc_word]
        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

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

        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

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

        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(8, len(array_of_dicts))

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

        GuessDictionaryAssertBuilder(array_of_dicts[4], self)\
            .assert_word_with_options_matches(word1_sw, ["i"])\
            .assert_word_with_options_matches(word2_sw, ["bcculs"])

        GuessDictionaryAssertBuilder(array_of_dicts[5], self)\
            .assert_word_with_options_matches(word1_sw, ["i"])\
            .assert_word_with_options_matches(word2_sw, ["qwwert"])

        GuessDictionaryAssertBuilder(array_of_dicts[6], self)\
            .assert_word_with_options_matches(word1_sw, ["j"])\
            .assert_word_with_options_matches(word2_sw, ["bcculs"])

        GuessDictionaryAssertBuilder(array_of_dicts[7], self)\
            .assert_word_with_options_matches(word1_sw, ["j"])\
            .assert_word_with_options_matches(word2_sw, ["qwwert"])

    def assert_word_with_options_matches(self, target: EncryptedWordWithOptions, single_word: SingleWord, solution_words: list):
        self.assertEqual(single_word.word, target.get_encrypted_word())

        self.assertEqual(len(solution_words), target.get_solution_word_count())

        for index in range(len(solution_words)):
            self.assertEqual(solution_words[index], target.get_solution_word_at_index(index))


class GuessDictionaryAssertBuilder:

    def __init__(self, dictionary: dict, test_case: unittest.TestCase) -> None:
        self.dictionary = dictionary
        self.test_case = test_case

    def assert_word_with_options_matches(self, single_word: SingleWord, solution_words: list):
        target = self.dictionary[single_word]

        self.test_case.assertEqual(single_word.word, target.get_encrypted_word())

        self.test_case.assertEqual(len(solution_words), target.get_solution_word_count())

        for index in range(len(solution_words)):
            self.test_case.assertEqual(solution_words[index], target.get_solution_word_at_index(index))

        return self


