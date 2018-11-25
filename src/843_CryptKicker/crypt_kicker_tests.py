import unittest

from crypt_kicker import crypt_decrypt


class CryptKickerTests(unittest.TestCase):
    def test_should_return_empty_string_given_empty_string(self):
        dictionary = []

        result = crypt_decrypt("", dictionary)
        self.assertEqual("", result)

        result = crypt_decrypt(" ", dictionary)
        self.assertEqual("", result)

    def test_should_return_empty_string_given_empty_string_and_anything_in_dictionary(self):
        dictionary = ["some stuff"]

        result = crypt_decrypt("", dictionary)
        self.assertEqual("", result)

        result = crypt_decrypt("  ", dictionary)
        self.assertEqual("", result)

    def test_should_return_result_with_single_letter(self):
        dictionary = ["a"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("a", result)

        dictionary = ["c"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("c", result)

        dictionary = ["e"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("e", result)

    def test_should_return_possible_results_when_single_letter_word_has_more_than_one_solution(self):
        dictionary = ["a", "b"]
        result = crypt_decrypt("c", dictionary)
        self.assertEqual("a", result)

        dictionary = ["c", "d"]
        result = crypt_decrypt("a", dictionary)
        self.assertEqual("c", result)

    def test_should_return_solution_given_two_single_letter_dictionary_and_two_single_letter_encrypt(self):
        dictionary = ["a", "b"]

        result = crypt_decrypt("c d", dictionary)
        self.assertEqual("a b", result)

        result = crypt_decrypt("d c", dictionary)
        self.assertEqual("a b", result)

        result = crypt_decrypt("c d d", dictionary)
        self.assertEqual("a b b", result)

        result = crypt_decrypt("c c d", dictionary)
        self.assertEqual("a a b", result)

    def test_should_return_solution_give_two_single_letter_words_without_single_solution(self):
        dictionary = ["a"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

        dictionary = ["z"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

    def test_should_return_solution_given_two_single_letter_words(self):
        dictionary = ["a"]
        result = crypt_decrypt("c c", dictionary)
        self.assertEqual("a a", result)

    def test_should_return_solution_given_three_single_letter_words(self):
        dictionary = ["a"]
        result = crypt_decrypt("c c c", dictionary)
        self.assertEqual("a a a", result)

    def test_should_return_no_solution_when_two_letter_words_have_no_solution(self):
        dictionary = ["aa"]
        result = crypt_decrypt("bb cc", dictionary)
        self.assertEqual("** **", result)

    def test_should_return_no_solution_with_three_letters(self):
        dictionary = ["aab", "aac"]
        result = crypt_decrypt("xxy xxz", dictionary)
        self.assertEqual("aab acc", result)

    def test_should_return_no_solution_when_two_letter_words_have_no_solution_and_change_in_letters(self):
        dictionary = ["ab"]
        result = crypt_decrypt("bc cd", dictionary)
        self.assertEqual("** **", result)

        dictionary = ["ab"]
        result = crypt_decrypt("bc bd", dictionary)
        self.assertEqual("** **", result)

        dictionary = ["ab"]
        result = crypt_decrypt("cc dd", dictionary)
        self.assertEqual("** **", result)

    def test_should_return_solution_when_two_letter_words_have_single_solution(self):
        dictionary = ["aa"]
        result = crypt_decrypt("bb bb", dictionary)
        self.assertEqual("aa aa", result)

    def test_should_return_solution_when_two_letter_words_have_single_solution_with_different_letters(self):
        dictionary = ["ab"]
        result = crypt_decrypt("bc bc", dictionary)
        self.assertEqual("ab ab", result)

    def test_should_return_solution_one_of_multiple_solutions_with_two_letters(self):
        dictionary = ["ab", "cd"]
        result = crypt_decrypt("xy xy", dictionary)
        self.assertEqual("ab ab", result)

        dictionary = ["cd", "ab"]
        result = crypt_decrypt("xy xy", dictionary)
        self.assertEqual("cd cd", result)

    def test_should_return_solution_one_of_multiple_solutions_with_two_letters_when_first_item_should_be_rejected(self):
        dictionary = ["xx", "cd"]
        result = crypt_decrypt("xy", dictionary)
        self.assertEqual("cd cd", result)

    def test_would_work_with_singe_word_and_single_encrypt_word(self):
        dictionary = ["abc"]
        result = crypt_decrypt("xyx", dictionary)
        self.assertEqual("abc", result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()

