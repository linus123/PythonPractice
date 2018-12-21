import copy
import sys
from typing import List


def crypt_decrypt(encrypted_line, solution_words):

    print("Start")

    encrypted_words = convert_to_array(encrypted_line)

    if len(encrypted_words) == 0:
        return ""

    solution_words = clean_array(solution_words)

    word_map = WordMap(solution_words)

    for encrypted_word in encrypted_words:
        word_map.process_encrypted_word(encrypted_word)

    word_map.prune_options()

    if word_map.has_no_solution:
        return get_no_solution(encrypted_line)
    # else MIGHT have a solution

    has_single_solution = word_map.has_single_solution()

    if not has_single_solution:
        has_guess_solution = False

        for guess_word_map in word_map.get_guesses():

            print("Process Guess")

            guess_word_map.prune_options()

            if guess_word_map.has_no_solution:
                continue

            has_single_solution = guess_word_map.has_single_solution()

            if has_single_solution:
                print("Found Single Solution")
                word_map = guess_word_map
                has_guess_solution = True
                break

        if not has_guess_solution:
            return get_no_solution(encrypted_line)

    return word_map.get_decrypted_line(encrypted_line)


class SingleWord:
    def __init__(self, word: str):
        self.word = word
        self.word_length = len(word)

        self.unique_letter_word = self.create_unique_letter_word(word)
        self.unique_letter_word_length = len(self.create_unique_letter_word(word))

    @staticmethod
    def create_unique_letter_word(word) -> str:

        letter_dict = {}

        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1

        return "".join(letter_dict.keys())

    def __repr__(self) -> str:
        return "word: '%s' unique_letter_word: '%s' unique_letter_word_length: '%i'" % (
            self.word,
            self.unique_letter_word,
            self.unique_letter_word_length)

    def __str__(self) -> str:
        return "word: '%s' unique_letter_word: '%s' unique_letter_word_length: '%i'" % (
            self.word,
            self.unique_letter_word,
            self.unique_letter_word_length)

    def is_word_possible(self, word):
        if self.word_length != word.word_length:
            return False

        if self.unique_letter_word_length != word.unique_letter_word_length:
            return False

        return True


def clean_array(word_dictionary):
    return [SingleWord(word.strip()) for word in word_dictionary]


def convert_to_array(encrypted_line: str) -> List[SingleWord]:
    encrypted_line = encrypted_line.strip()

    if encrypted_line == "":
        return []

    split_line = encrypted_line.split(' ')

    encrypted_words = []

    for word in split_line:
        word = word.strip()

        if word != "":
            encrypted_words.append(SingleWord(word))

    return encrypted_words


def get_no_solution(encrypted_line):
    char_array = []

    for letter in encrypted_line:
        if letter == " ":
            char_array.append(letter)
        else:
            char_array.append("*")

    return ''.join(char_array)


class WordMap:
    def __init__(self, solution_words: List[SingleWord], decode_words=None):
        self.solution_words = solution_words

        if decode_words is None:
            decode_words = {}
        self.decode_words = decode_words

        self.has_no_solution = False

    def get_decrypted_line(self, encrypted_line: str):

        letter_map = self.create_letter_map_array_for_all_single_solution_words()

        char_array = []

        for letter in encrypted_line:
            if letter == " ":
                char_array.append(letter)
            else:
                char_array.append(letter_map[letter])

        return ''.join(char_array)

    def process_encrypted_word(self, encrypted_word: SingleWord):
        if encrypted_word.word in self.decode_words:
            return

        encrypted_word_obj = EncryptedWordWithOptions(encrypted_word)

        for solution_word in self.solution_words:

            possible = encrypted_word_obj.is_encrypted_word_possible_with(solution_word)

            if possible:
                encrypted_word_obj.add_solution_word(solution_word)

        self.decode_words[encrypted_word.word] = encrypted_word_obj

    def has_single_solution(self):
        for key, encrypted_word in self.decode_words.items():
            if encrypted_word.get_solution_word_count() > 1:
                return False
        return True

    def remove_possible_words_that_do_not_match_letter_maps(self, letter_maps: dict):
        for key, encrypted_word in self.decode_words.items():
            if encrypted_word.get_solution_word_count() > 1:
                for en_letter, sol_letter in letter_maps.items():
                    encrypted_word.remove_word_that_do_not_match_letter(en_letter, sol_letter)

    def create_letter_map_array_for_all_single_solution_words(self):
        letter_maps_dic_enc = {}
        letter_maps_dic_sol = {}

        # print("calling create_letter_map_array_for_all_single_solution_words")

        for key, current_encrypted_word in self.decode_words.items():
            if current_encrypted_word.get_solution_word_count() == 1:
                first_solution_word = current_encrypted_word.get_first_solution_word()

                letter_map_for_current_enc_word = self.create_encrypted_letter_map(
                    current_encrypted_word.encrypted_word,
                    first_solution_word)

                for current_key, current_sol_letter in letter_map_for_current_enc_word.items():
                    if current_key in letter_maps_dic_enc:
                        if letter_maps_dic_enc[current_key] != current_sol_letter:
                            return None
                    if current_sol_letter in letter_maps_dic_sol:
                        if letter_maps_dic_sol[current_sol_letter] != current_key:
                            return None
                    else:
                        letter_maps_dic_enc[current_key] = current_sol_letter
                        letter_maps_dic_sol[current_sol_letter] = current_key

        return letter_maps_dic_enc

    def all_decode_words_have_at_least_one_item(self) -> bool:
        for key, encrypted_word in self.decode_words.items():
            if not encrypted_word.has_any_solution_words():
                return False

        return True

    def remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option(self) -> bool:
        for key, decode_word_array in self.decode_words.items():
            if decode_word_array.get_solution_word_count() == 1:

                has_solution = self.remove_word_from_other_decode_words(
                    decode_word_array.get_first_solution_word(),
                    key)

                if not has_solution:
                    return False

        return True

    def remove_word_from_other_decode_words(self, word_to_remove: str, key_to_skip: str):
        for key, encrypted_word in self.decode_words.items():
            if key != key_to_skip:
                encrypted_word.remove_solution_word(word_to_remove)

                if not encrypted_word.has_any_solution_words():
                    return False
        return True

    def has_any_decode_words(self) -> bool:
        return len(self.decode_words) > 0

    def create_encrypted_letter_map(self, encrypted_word: SingleWord, solution_word: SingleWord) -> dict:
        encrypted_letter_dictionary = {}

        for encrypted_letter_index in range(len(encrypted_word.unique_letter_word)):
            encrypted_letter = encrypted_word.unique_letter_word[encrypted_letter_index]
            encrypted_letter_dictionary[encrypted_letter] = solution_word.unique_letter_word[encrypted_letter_index]

        return encrypted_letter_dictionary

    def get_guesses(self):

        decode_words_array = []

        curr_dict = {}

        for current_key, current_encrypted_word in self.decode_words.items():
            decode_words_array.append(current_encrypted_word)

        array_of_dicts = self.create_all_single_word_combinations(decode_words_array, curr_dict)

        for blow in array_of_dicts:
            yield WordMap(self.solution_words, blow)

    @staticmethod
    def create_all_single_word_combinations(decode_words_array):
        if len(decode_words_array) == 0:
            return

        for outer_index in range(len(decode_words_array)):
            if decode_words_array[outer_index].get_number_of_solution_words() <= 1:
                continue

            single_options = decode_words_array[outer_index].copy_with_single_options()

            for single_option in single_options:
                foo_dict = {}
                for inner_index in range(len(decode_words_array)):
                    current_enc_word = decode_words_array[inner_index]
                    if inner_index == outer_index:
                        foo_dict[current_enc_word.encrypted_word] = single_option
                    else:
                        current_enc_word = decode_words_array[inner_index]
                        foo_dict[current_enc_word.encrypted_word] = current_enc_word.create_copy()
                yield foo_dict

    def prune_options(self):
        if not self.has_any_decode_words():
            self.has_no_solution = True
            return

        has_solution = self.all_decode_words_have_at_least_one_item()

        if not has_solution:
            self.has_no_solution = True
            return

        has_solution = self.remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option()

        if not has_solution:
            self.has_no_solution = True
            return

        letter_maps = self.create_letter_map_array_for_all_single_solution_words()

        if letter_maps is None:
            self.has_no_solution = True
            return

        self.remove_possible_words_that_do_not_match_letter_maps(letter_maps)

        has_solution = self.all_decode_words_have_at_least_one_item()

        if not has_solution:
            self.has_no_solution = True
            return

        self.solution_words.sort(key=get_unique_letter_word_length)


def get_unique_letter_word_length(word: SingleWord):
    return word.unique_letter_word_length


class EncryptedWordWithOptions:
    def __init__(self, encrypted_word: SingleWord):
        self.encrypted_word = encrypted_word
        self.solution_words = []

    def get_encrypted_word(self):
        return self.encrypted_word.word

    def create_copy(self):
        ew = EncryptedWordWithOptions(self.encrypted_word)
        ew.solution_words = copy.copy(self.solution_words)
        return ew

    def __repr__(self):
        return str(self.encrypted_word) + "[" + ",".join(self.solution_words) + "]"

    def is_encrypted_word_possible_with(self, word: SingleWord):
        return self.encrypted_word.is_word_possible(word)

    def get_number_of_solution_words(self):
        return len(self.solution_words)

    def copy_with_single_options(self):
        result = []

        for solution_word in self.solution_words:
            opt = EncryptedWordWithOptions(self.encrypted_word)
            opt.add_solution_word(solution_word)
            result.append(opt)

        return result

    def add_solution_word(self, word: SingleWord):
        self.solution_words.append(word)

    def has_any_solution_words(self) -> bool:
        return len(self.solution_words) > 0

    def get_solution_word_count(self) -> int:
        return len(self.solution_words)

    def get_solution_words(self):
        return self.solution_words

    def get_solution_word_at_index(self, index: int):
        return self.solution_words[index].word

    def remove_solution_word(self, item_to_remove: SingleWord) -> bool:
        for index in range(len(self.solution_words)):
            if self.solution_words[index] == item_to_remove:
                del self.solution_words[index]
                return True

        return False

    def get_first_solution_word(self) -> SingleWord:
        return self.solution_words[0]

    def remove_word_that_do_not_match_letter(self, encrypted_letter, solution_letter):

        for encrypted_letter_index in range(len(self.encrypted_word.unique_letter_word)):
            current_encrypted_letter = self.encrypted_word.unique_letter_word[encrypted_letter_index]

            new_solution_words = []

            if current_encrypted_letter == encrypted_letter:
                for solution_word in self.solution_words:
                    if solution_word.unique_letter_word[encrypted_letter_index] == solution_letter:
                        new_solution_words.append(solution_word)

                self.solution_words = new_solution_words


def run_from_standard_in():

    line_counter = 0

    dictionary_word_count = 0
    dictionary_words = []

    for line in sys.stdin:

        clean_line = line.strip()

        if line_counter == 0:
            dictionary_word_count = int(clean_line)
        elif line_counter <= dictionary_word_count:
            dictionary_words.append(clean_line)
        else:
            result = crypt_decrypt(clean_line, dictionary_words)
            print(result)

        line_counter += 1


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()
