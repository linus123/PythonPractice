import unittest

from crypt_kicker import crypt_decrypt, SingleWord


class CryptKickerHarnessTests(unittest.TestCase):
    def test_foobar(self):
        letter_key = self.create_letter_key_via_offset()

        # expected_result = "neque porro quisquam est qui dolorem ipsum quia dolor sit amet consectetur adipisci velit"

        dictionary = ["neque",
                    "porro",
                    "quisquam",
                    "est",
                    "qui",
                    "dolorem",
                    "ipsum",
                    "quia",
                    "dolor",
                    "sit",
                    "amet",
                    "consectetur",
                    "velit"]

        expected_result = "neque porro quisquam"
        enc_line = self.encrypt_line(expected_result, letter_key)
        result = crypt_decrypt(enc_line, dictionary)
        self.assertEqual(expected_result, result)

        expected_result = "neque porro quisquam est qui dolorem ipsum quia dolor sit amet consectetur"
        enc_line = self.encrypt_line(expected_result, letter_key)
        result = crypt_decrypt(enc_line, dictionary)
        self.assertEqual(expected_result, result)

    def encrypt_line(self, expected_result, letter_key):
        foo_arr = []
        for letter in expected_result:
            if letter == " ":
                foo_arr.append(" ")
            else:
                foo_arr.append(letter_key[letter])
        enc_line = "".join(foo_arr)
        return enc_line

    def create_letter_key_via_offset(self):
        offset = 10
        letter_key = {}
        for count in range(26):
            key = chr(ord('a') + count)

            if count >= 26 - offset:
                enc_letter = chr(ord('a') + count + offset - 26)
            else:
                enc_letter = chr(ord('a') + count + offset)

            letter_key[key] = enc_letter
        return letter_key
