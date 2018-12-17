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

        target_enc_word = array_of_dicts[0][foobar_sw]
        self.assertEqual("foobar", target_enc_word.get_encrypted_word())
        self.assertEqual(1, target_enc_word.get_solution_word_count())
        self.assertEqual("bcculs", target_enc_word.get_solution_word_at_index(0))

    def test_recurse_003(self):
        foobar_sw = SingleWord("foobar")

        enc_word = EncryptedWordWithOptions(foobar_sw)
        enc_word.add_solution_word(SingleWord("bcculs"))
        enc_word.add_solution_word(SingleWord("qwwert"))
        decode_words_array = [enc_word]
        curr_dict = {}

        array_of_dicts = list(WordMap.create_all_single_word_combinations(decode_words_array, curr_dict))

        self.assertEqual(2, len(array_of_dicts))

        target_enc_word = array_of_dicts[0][foobar_sw]
        self.assertEqual("foobar", target_enc_word.get_encrypted_word())
        self.assertEqual(1, target_enc_word.get_solution_word_count())
        self.assertEqual("bcculs", target_enc_word.get_solution_word_at_index(0))

        target_enc_word = array_of_dicts[1][foobar_sw]
        self.assertEqual("foobar", target_enc_word.get_encrypted_word())
        self.assertEqual(1, target_enc_word.get_solution_word_count())
        self.assertEqual("qwwert", target_enc_word.get_solution_word_at_index(0))

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

        target_enc_word = array_of_dicts[0][a_sw]
        self.assertEqual("a", target_enc_word.get_encrypted_word())
        self.assertEqual(1, target_enc_word.get_solution_word_count())
        self.assertEqual("i", target_enc_word.get_solution_word_at_index(0))

        target_enc_word = array_of_dicts[0][foobar_sw]
        self.assertEqual("foobar", target_enc_word.get_encrypted_word())
        self.assertEqual(1, target_enc_word.get_solution_word_count())
        self.assertEqual("bcculs", target_enc_word.get_solution_word_at_index(0))

        target_enc_word = array_of_dicts[1][a_sw]
        self.assertEqual("a", target_enc_word.get_encrypted_word())
        self.assertEqual(1, target_enc_word.get_solution_word_count())
        self.assertEqual("i", target_enc_word.get_solution_word_at_index(0))

        target_enc_word = array_of_dicts[1][foobar_sw]
        self.assertEqual("foobar", target_enc_word.get_encrypted_word())
        self.assertEqual(1, target_enc_word.get_solution_word_count())
        self.assertEqual("qwwert", target_enc_word.get_solution_word_at_index(0))
