import copy
import sys
from typing import List


def crypt_decrypt(encrypted_line, solution_words):

    if encrypted_line.strip() == "":
        return None

    encrypted_words = convert_to_array(encrypted_line)

    if len(encrypted_words) == 0:
        return get_no_solution(encrypted_words)

    solution_words = clean_array(solution_words)

    word_map = WordMap(solution_words)

    for encrypted_word in encrypted_words:
        word_map.process_encrypted_word(encrypted_word)

    word_map.prune_options()

    if word_map.has_no_solution:
        return get_no_solution(encrypted_words)
    # else MIGHT have a solution

    has_single_solution = word_map.has_single_solution()

    if not has_single_solution:
        solution = recurse_guesses(word_map)

        if solution is None:
            return get_no_solution(encrypted_words)

        word_map = solution

    return word_map.get_decrypted_line(encrypted_words)


def recurse_guesses(current_guess):
    # print("Starting Recursing Guesses")
    for guess_word_map in current_guess.get_guesses():

        # print("Process Guess has_no_solution" + str(guess_word_map.has_no_solution))

        guess_word_map.prune_options()

        if guess_word_map.has_no_solution:
            # print("Not a solution")
            continue

        has_single_solution = guess_word_map.has_single_solution()

        if has_single_solution:
            # print("Found Single Solution")
            return guess_word_map
        else:
            # print("did NOT Found Single Solution")
            pass

        rg = recurse_guesses(guess_word_map)

        if rg is not None:
            return rg

    return None


class SingleWord:
    def __init__(self, word: str):
        self.word = word
        self.word_length = len(word)

        self.unique_letter_word = self.create_unique_letter_word(word)
        self.unique_letter_word_length = len(self.create_unique_letter_word(word))

    def get_no_solution_string(self):
        return "*" * len(self.word)

    @staticmethod
    def create_unique_letter_word(word) -> str:

        letter_dict = {}
        letter_array = []

        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
                letter_array.append(letter)

        return "".join(letter_array)

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

        dic1 = {}
        dic2 = {}

        for letter_index in range(len(self.word)):

            letter1 = self.word[letter_index]
            letter2 = word.word[letter_index]

            if letter1 in dic1:
                if dic1[letter1] != letter2:
                    return False
            else:
                dic1[letter1] = letter2

            if letter2 in dic2:
                if dic2[letter2] != letter1:
                    return False
            else:
                dic2[letter2] = letter1

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


def get_no_solution(encrypted_words: list):
    word_array = []

    for word in encrypted_words:
        word_array.append(word.get_no_solution_string())

    return ' '.join(word_array)


class WordMap:
    def __init__(self, solution_words: List[SingleWord], decode_words=None):
        self.solution_words = solution_words

        if decode_words is None:
            decode_words = {}
        else:
            for key, encrypted_word in sorted(decode_words.items()):
                if encrypted_word.get_solution_word_count() <= 0:
                    raise ValueError('Empty solution words')

        self.decode_words = decode_words

        self.has_no_solution = False

    def print_state(self):
        pass
        # print("***")
        # for key, item in sorted(self.decode_words.items()):
        #     print("encrypted word '%s'" % key)
        #     for sol_word in item.get_solution_words():
        #         print("\t%s" % sol_word.word)
        #
        # print("has_no_solution " + str(self.has_no_solution))

    def get_decrypted_line(self, encrypted_words):

        word_array = []

        for word in encrypted_words:
            word_array.append(self.decode_words[word.word].get_first_solution_word().word)

        return ' '.join(word_array)

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
        for key, encrypted_word in sorted(self.decode_words.items()):
            if encrypted_word.get_solution_word_count() > 1:
                return False
        return True

    def remove_possible_words_that_do_not_match_letter_maps(self, letter_maps: dict):
        items_were_removed = False

        for key, encrypted_word in sorted(self.decode_words.items()):
            for en_letter, sol_letter in letter_maps.items():
                removed = encrypted_word.remove_word_that_do_not_match_letter(en_letter, sol_letter)
                if removed:
                    items_were_removed = True

        return items_were_removed

    def create_letter_map_array_for_all_single_solution_words(self):
        letter_maps_dic_enc = {}
        letter_maps_dic_sol = {}

        # print("calling create_letter_map_array_for_all_single_solution_words")

        for key, current_encrypted_word in sorted(self.decode_words.items()):
            if current_encrypted_word.get_solution_word_count() == 1:
                first_solution_word = current_encrypted_word.get_first_solution_word()

                letter_map_for_current_enc_word = self.create_encrypted_letter_map(
                    current_encrypted_word.encrypted_word,
                    first_solution_word)

                # print("letter_map_for_current_enc_word: %s" % letter_map_for_current_enc_word)

                for current_key, current_sol_letter in letter_map_for_current_enc_word.items():
                    # print("eval current_key: %s current_sol_letter: %s" % (current_key, current_sol_letter))

                    if current_key in letter_maps_dic_enc:
                        if letter_maps_dic_enc[current_key] != current_sol_letter:
                            # print("1 - %s is not %s" % (letter_maps_dic_enc[current_key], current_sol_letter))
                            return None
                    if current_sol_letter in letter_maps_dic_sol:
                        if letter_maps_dic_sol[current_sol_letter] != current_key:
                            # print("2 - %s is not %s" % (letter_maps_dic_sol[current_sol_letter], current_key))
                            return None
                    else:
                        letter_maps_dic_enc[current_key] = current_sol_letter
                        letter_maps_dic_sol[current_sol_letter] = current_key

                        # print("letter_maps_dic_enc: %s" % letter_maps_dic_enc)
                        # print("letter_maps_dic_sol: %s" % letter_maps_dic_sol)

        return letter_maps_dic_enc

    def all_decode_words_have_at_least_one_item(self) -> bool:
        for key, encrypted_word in sorted(self.decode_words.items()):
            if not encrypted_word.has_any_solution_words():
                return False

        return True

    def remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option(self) -> (bool, bool):
        word_was_removed = False

        for key, decode_word_array in sorted(self.decode_words.items()):
            if decode_word_array.get_solution_word_count() == 1:

                has_solution, removed = self.remove_word_from_other_decode_words(
                    decode_word_array.get_first_solution_word(),
                    key)

                if removed:
                    word_was_removed = True

                if not has_solution:
                    return False, False

        return True, word_was_removed

    def remove_word_from_other_decode_words(self, word_to_remove: str, key_to_skip: str):
        word_was_removed = False

        for key, encrypted_word in sorted(self.decode_words.items()):
            if key != key_to_skip:
                word_was_removed = encrypted_word.remove_solution_word(word_to_remove)

                if not encrypted_word.has_any_solution_words():
                    return False, False
        return True, word_was_removed

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

        for current_key, current_encrypted_word in self.decode_words.items():
            decode_words_array.append(current_encrypted_word)

        decode_words_array.sort(key=lambda x: x.get_encrypted_word_length(), reverse=True)

        array_of_dicts = self.create_all_single_word_combinations(decode_words_array)

        for d in array_of_dicts:
            yield WordMap(self.solution_words, d)

    @staticmethod
    def create_all_single_word_combinations(decode_words_array):
        if len(decode_words_array) == 0:
            return

        for outer_index in range(len(decode_words_array)):
            if decode_words_array[outer_index].get_number_of_solution_words() <= 1:
                continue

            single_options = decode_words_array[outer_index].copy_with_single_options()

            for single_option in single_options:
                d = {}
                for inner_index in range(len(decode_words_array)):
                    current_enc_word = decode_words_array[inner_index]
                    if inner_index == outer_index:
                        d[current_enc_word.encrypted_word.word] = single_option
                    else:
                        current_enc_word = decode_words_array[inner_index]
                        d[current_enc_word.encrypted_word.word] = current_enc_word.create_copy()
                yield d

    def prune_options(self):
        words_were_removed_by_single = True
        words_were_removed_by_map = True

        # print("Begin Prune")
        self.print_state()

        while words_were_removed_by_single or words_were_removed_by_map:

            if not self.has_any_decode_words():
                # print("Cut 1")
                self.has_no_solution = True
                return

            has_solution = self.all_decode_words_have_at_least_one_item()

            if not has_solution:
                # print("Cut 2")
                self.has_no_solution = True
                return

            has_solution, words_were_removed_by_single = self\
                .remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option()

            # print("remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option | has_solution: %r words_were_removed_by_single: %r" % (has_solution, words_were_removed_by_single))
            self.print_state()

            if not has_solution:
                # print("Cut 3")
                self.has_no_solution = True
                return

            letter_maps = self.create_letter_map_array_for_all_single_solution_words()

            if letter_maps is None:
                # print("Cut 4")
                self.has_no_solution = True
                return
            else:
                # print("letter_map: " + str(letter_maps))
                pass

            words_were_removed_by_map = self.remove_possible_words_that_do_not_match_letter_maps(letter_maps)

            # print("remove_possible_words_that_do_not_match_letter_maps | words_were_removed_by_map: %r" % words_were_removed_by_map)
            self.print_state()

            has_solution = self.all_decode_words_have_at_least_one_item()

            if not has_solution:
                # print("Cut 5")
                self.has_no_solution = True
                return

        self.solution_words.sort(key=get_unique_letter_word_length)


def get_unique_letter_word_length(word: SingleWord):
    return word.unique_letter_word_length


class EncryptedWordWithOptions:
    def __init__(self, encrypted_word: SingleWord):
        self.encrypted_word = encrypted_word
        self.solution_words = []

    # Needed by print
    def get_solution_words(self):
        return self.solution_words

    def get_encrypted_word(self):
        return self.encrypted_word.word

    def get_encrypted_word_length(self):
        return len(self.encrypted_word.word)

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

        items_were_removed = False

        for encrypted_letter_index in range(len(self.encrypted_word.unique_letter_word)):
            current_encrypted_letter = self.encrypted_word.unique_letter_word[encrypted_letter_index]

            if current_encrypted_letter == encrypted_letter:

                new_solution_words = []

                for solution_word in self.solution_words:
                    if solution_word.unique_letter_word[encrypted_letter_index] == solution_letter:
                        new_solution_words.append(solution_word)

                items_were_removed = len(new_solution_words) != len(self.solution_words)
                self.solution_words = new_solution_words

        return items_were_removed


def run_from_standard_in():

    line_counter = 0

    dictionary_word_count = 0
    dictionary_words = []

    for line in sys.stdin:

        clean_line = line.strip().lower()

        if clean_line == "":
            continue

        if line_counter == 0:
            dictionary_word_count = int(clean_line)
        elif line_counter <= dictionary_word_count:
            dictionary_words.append(clean_line)
        else:
            result = crypt_decrypt(clean_line, dictionary_words)
            if result is not None:
                print(result)

        line_counter += 1


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()
