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

    def test_should_return_solution_give_two_single_letter_words_without_single_solution(self):
        dictionary = ["a"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

        dictionary = ["z"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

    def test_should_return_solution_give_two_single_letter_words(self):
        dictionary = ["a"]
        result = crypt_decrypt("c c", dictionary)
        self.assertEqual("a a", result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()

