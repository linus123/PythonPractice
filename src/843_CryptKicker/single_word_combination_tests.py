import unittest

from crypt_kicker import EncryptedWordWithOptions, WordMap, SingleWord


class SingleWordComboTests(unittest.TestCase):
    def test_recurse_001(self):
        foobar_sw = SingleWord("foobar")

        decode_words_array = [EncryptedWordWithOptions(foobar_sw)]
        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(0, len(array_of_dicts))

    def test_recurse_002(self):
        foobar_sw = SingleWord("foobar")
        enc_word = EncryptedWordWithOptions(foobar_sw)

        enc_word.add_solution_word(SingleWord("bcculs"))
        decode_words_array = [enc_word]
        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(1, len(array_of_dicts))

        self.assert_word_with_options_matches(
            array_of_dicts[0][foobar_sw],
            foobar_sw,
            ["bcculs"]
        )


    def test_recurse_003(self):
        foobar_sw = SingleWord("foobar")

        enc_word = EncryptedWordWithOptions(foobar_sw)
        enc_word.add_solution_word(SingleWord("bcculs"))
        enc_word.add_solution_word(SingleWord("qwwert"))
        decode_words_array = [enc_word]
        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(2, len(array_of_dicts))

        self.assert_word_with_options_matches(
            array_of_dicts[0][foobar_sw],
            foobar_sw,
            ["bcculs"]
        )

        self.assert_word_with_options_matches(
            array_of_dicts[1][foobar_sw],
            foobar_sw,
            ["qwwert"]
        )

    def test_recurse_004(self):
        a_sw = SingleWord("a")
        foobar_sw = SingleWord("foobar")

        enc_word01 = EncryptedWordWithOptions(a_sw)
        enc_word01.add_solution_word(SingleWord("i"))

        enc_word02 = EncryptedWordWithOptions(foobar_sw)
        enc_word02.add_solution_word(SingleWord("bcculs"))
        enc_word02.add_solution_word(SingleWord("qwwert"))
        decode_words_array = [enc_word01, enc_word02]

        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(2, len(array_of_dicts))

        self.assert_word_with_options_matches(
            array_of_dicts[0][a_sw],
            a_sw,
            ["i"]
        )

        self.assert_word_with_options_matches(
            array_of_dicts[0][foobar_sw],
            foobar_sw,
            ["bcculs"]
        )

        self.assert_word_with_options_matches(
            array_of_dicts[1][a_sw],
            a_sw,
            ["i"]
        )

        self.assert_word_with_options_matches(
            array_of_dicts[1][foobar_sw],
            foobar_sw,
            ["qwwert"]
        )

    def assert_word_with_options_matches(self, target: EncryptedWordWithOptions, single_word: SingleWord, solution_words: list):
        self.assertEqual(single_word.word, target.get_encrypted_word())

        self.assertEqual(len(solution_words), target.get_solution_word_count())

        for index in range(len(solution_words)):
            self.assertEqual(solution_words[index], target.get_solution_word_at_index(index))
