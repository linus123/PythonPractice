import sys
from typing import List

from crypt_helpers import *

"""
KeyArray will hold the replacement table.

- Start with an empty KeyArray, this is version 0
- Match longest encrypted word to longest dictionary word and add to KeyArray (if there are two longest, pick any),
    this is version 1.
- Decrypt some letters of the next longest encrypted word.
- Check if the decrypted letters match the letter in the same position in any dictionary word of the same length.
- If none matches, go back to version 0 and try another word.
- If some letters match, add the rest of the letters to KeyArray, this is version 2.
- Decrypt some letters of the next longest encrypted word.
- Check if the decrypted letters match the letter in the same position in any dictionary word.
- If none matches, go back to version 1 and try another word
- If some letters match, add the rest of the letters to KeyArray, this is version 3.
- Repeat until all words are decrypted.

If at version 0 none of the longest words creates a partial decrypt in shorter words,
    very probably there is no solution.
"""

def crypt_decrypt(encrypted_line, solution_words):

    if encrypted_line.strip() == "":
        return None

    encrypted_words = convert_to_array_of_strings(encrypted_line)
    encrypted_words_dict = LengthKeyedDict(encrypted_words)

    if len(encrypted_words) == 0:
        return get_no_solution(encrypted_words)

    solution_words = clean_array(solution_words)
    solution_words_dict = LengthKeyedDict(solution_words)

    word_lengths = encrypted_words_dict.word_lengths

    solution_map = SolutionMap()

    solution_maps = create_solution_maps(
        word_lengths,
        solution_map,
        encrypted_words_dict,
        solution_words_dict
    )

    for solution_map in solution_maps:
        return solution_map.get_decrypted_line(encrypted_words)

    return get_no_solution(encrypted_words)


def create_solution_maps(
        word_lengths: list,
        solution_map: SolutionMap,
        encrypted_words_dict: LengthKeyedDict,
        solution_words_dict: LengthKeyedDict):

    if len(word_lengths) <= 0:
        return solution_map

    current_len = word_lengths[0]

    current_enc_word_list = encrypted_words_dict.get_words(current_len)

    if not solution_words_dict.has_words_of_length(current_len):
        return

    current_sol_word_list = solution_words_dict.get_words(current_len)

    for enc_word_index in range(len(current_enc_word_list)):
        solution_maps = create_solution_maps_for_single_word_length(
            enc_word_index,
            solution_map.create_copy(),
            copy.copy(current_enc_word_list),
            copy.copy(current_sol_word_list))

        for solution_map in solution_maps:
            yield solution_map

def create_solution_maps_for_single_word_length(
        enc_word_index: int,
        solution_map: SolutionMap,
        current_enc_word_list: list,
        current_sol_word_list: list):

    if len(current_enc_word_list) <= 0:
        yield solution_map
        return

    if len(current_sol_word_list) <= 0:
        return

    target_encrypted_word = current_enc_word_list[enc_word_index]

    sol_word_index = -1

    for sol_word_index in range(len(current_sol_word_list)):
        sol_word = current_sol_word_list[sol_word_index]
        # Do we need this?
        if solution_map.has_mapped_solution_word(sol_word):
            continue

        has_found_solution_word = solution_map.try_to_set_word(target_encrypted_word, sol_word)

        if has_found_solution_word:
            break

    if not solution_map.has_solution_for_encrypted_word(target_encrypted_word):
        return
    else:
        new_enc_word_list = current_enc_word_list[:enc_word_index] + current_enc_word_list[enc_word_index+1:]
        new_sol_word_list = current_sol_word_list[:sol_word_index] + current_sol_word_list[sol_word_index+1:]

        if len(new_enc_word_list) <= 0:
            yield solution_map

        for new_enc_word_index in range(len(new_enc_word_list)):
            r = create_solution_maps_for_single_word_length(new_enc_word_index, solution_map.create_copy(), new_enc_word_list, new_sol_word_list)

            for s in r:
                if s is not None:
                    yield s


def remove_duplicates_and_convert(encrypted_words: list):
    lst = list(set(encrypted_words))

    final = []

    for itm in lst:
        final.append(SingleWord(itm))

    return final


def create_sorted_list_with_largest_word_first(encrypted_words):
    return sorted(encrypted_words, key=lambda w: w.word_length, reverse=True)


def get_no_solution(encrypted_words: list):
    word_array = []

    for word in encrypted_words:
        word_array.append("*" * len(word))

    return ' '.join(word_array)

def convert_to_array_of_strings(encrypted_line: str) -> list:
    encrypted_line = encrypted_line.strip()

    if encrypted_line == "":
        return []

    split_line = encrypted_line.split(' ')

    encrypted_words = []

    for word in split_line:
        word = word.strip()

        if word != "":
            encrypted_words.append(word)

    return encrypted_words


def clean_array(word_dictionary):
    return [word.strip() for word in word_dictionary]


# *******************************************

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
        for key, encrypted_word in sorted(self.decode_words.items()):
            for en_letter, sol_letter in letter_maps.items():
                removed = encrypted_word.remove_word_that_do_not_match_letter(en_letter, sol_letter)
                if removed:
                    return True

        return False

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

        for key, decode_word_array in sorted(self.decode_words.items(), key=lambda kv: len(kv[0]), reverse=True):
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
        self.solution_words = {}

        self.opt_dic = {}

        for letter in encrypted_word.unique_letter_word:
            self.opt_dic[letter] = 1

    def has_letter_in_encrypted_word(self, letter):
        return letter in self.opt_dic

    # Needed by print
    def get_solution_words(self):
        for key, decode_word_array in self.solution_words.items():
            yield key

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

        for key, solution_word in self.solution_words.items():
            opt = EncryptedWordWithOptions(self.encrypted_word)
            opt.add_solution_word(solution_word)
            result.append(opt)

        return result

    def add_solution_word(self, word: SingleWord):
        self.solution_words[word.word] = word

    def has_any_solution_words(self) -> bool:
        return len(self.solution_words) > 0

    def get_solution_word_count(self) -> int:
        return len(self.solution_words)

    def has_solution_word(self, word: str):
        return word in self.solution_words

    def remove_solution_word(self, item_to_remove: SingleWord) -> bool:
        if self.has_solution_word(item_to_remove.word):
            del self.solution_words[item_to_remove.word]
            return True

        return False

    def get_first_solution_word(self) -> SingleWord:
        # return self.solution_words[0]
        return next(iter(self.solution_words.values()))

    def remove_word_that_do_not_match_letter(self, encrypted_letter, solution_letter):

        items_were_removed = False

        if not self.has_letter_in_encrypted_word(encrypted_letter):
            return False

        for encrypted_letter_index in range(len(self.encrypted_word.unique_letter_word)):
            current_encrypted_letter = self.encrypted_word.unique_letter_word[encrypted_letter_index]

            if current_encrypted_letter == encrypted_letter:

                new_solution_words = {}

                for key, solution_word in self.solution_words.items():
                    if solution_word.unique_letter_word[encrypted_letter_index] == solution_letter:
                        new_solution_words[solution_word.word] = solution_word

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
