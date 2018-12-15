import copy


def crypt_decrypt(encrypted_line, solution_words):
    encrypted_words = convert_to_array(encrypted_line)

    if len(encrypted_words) == 0:
        return ""

    solution_words = clean_array(solution_words)

    word_map = WordMap(solution_words)

    for encrypted_word in encrypted_words:
        word_map.process_encrypted_word(encrypted_word)

    if has_no_solution(word_map):
        return get_no_solution(encrypted_line)
    # else MIGHT have a solution

    has_single_solution = word_map.has_single_solution()

    if not has_single_solution:
        has_guess_solution = False

        for guess_word_map in word_map.get_guesses():
            if has_no_solution(guess_word_map):
                continue

            has_single_solution = guess_word_map.has_single_solution()

            if has_single_solution:
                word_map = guess_word_map
                has_guess_solution = True
                break

        if not has_guess_solution:
            return get_no_solution(encrypted_line)

    return word_map.get_decrypted_line(encrypted_line)


def has_no_solution(word_map) -> bool:
    if not word_map.has_any_decode_words():
        return True

    has_solution = word_map.all_decode_words_have_at_least_one_item()

    if not has_solution:
        return True

    has_solution = word_map.remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option()

    if not has_solution:
        return True

    letter_maps = word_map.create_letter_map_array_for_all_single_solution_words()

    if letter_maps is None:
        return True

    word_map.remove_possible_words_that_do_not_match_letter_maps(letter_maps)

    has_solution = word_map.all_decode_words_have_at_least_one_item()

    if not has_solution:
        return True

    return False


def clean_array(word_dictionary):
    return [word.strip() for word in word_dictionary]


def convert_to_array(encrypted_line: str) -> list:
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


def get_no_solution(encrypted_line):
    char_array = []

    for letter in encrypted_line:
        if letter == " ":
            char_array.append(letter)
        else:
            char_array.append("*")

    return ''.join(char_array)


class WordMap:
    def __init__(self, solution_words, decode_words=None):
        self.solution_words = solution_words

        if decode_words is None:
            decode_words = {}
        self.decode_words = decode_words

    def get_decrypted_line(self, encrypted_line: str):

        letter_map = self.create_letter_map_array_for_all_single_solution_words()

        char_array = []

        for letter in encrypted_line:
            if letter == " ":
                char_array.append(letter)
            else:
                char_array.append(letter_map[letter])

        return ''.join(char_array)

    def process_encrypted_word(self, encrypted_word: str):
        if encrypted_word in self.decode_words:
            return

        encrypted_word_obj = EncryptedWordWithOptions(encrypted_word)

        for solution_word in self.solution_words:

            word_pair = WordPair(encrypted_word_obj.encrypted_word, solution_word)

            if word_pair.is_word_possible():
                encrypted_word_obj.add_solution_word(solution_word)

        self.decode_words[encrypted_word] = encrypted_word_obj

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

    def create_encrypted_letter_map(self, encrypted_word: str, solution_word: str) -> dict:
        encrypted_letter_dictionary = {}

        for encrypted_letter_index in range(len(encrypted_word)):
            encrypted_letter = encrypted_word[encrypted_letter_index]
            encrypted_letter_dictionary[encrypted_letter] = solution_word[encrypted_letter_index]

        return encrypted_letter_dictionary

    def get_guesses(self):

        decode_words_array = []

        curr_dict = {}

        for current_key, current_encrypted_word in self.decode_words.items():
            decode_words_array.append(current_encrypted_word)

        array_of_dicts = []

        self.create_all_single_word_combinations(decode_words_array, curr_dict, array_of_dicts)

        for blow in array_of_dicts:
            yield WordMap(self.solution_words, blow)

    @staticmethod
    def create_all_single_word_combinations(decode_words_array, curr_dict, array_of_dicts, level=0):
        if len(decode_words_array) == 0:
            return
        copy_with_sig_options = decode_words_array[0].copy_with_single_options()

        for single_option in copy_with_sig_options:
            curr_dict[single_option.encrypted_word] = single_option
            # print("level %i - single_option %s" % (level, single_option))
            sub_decode_words_array = decode_words_array[1:]
            # print("level %i - sub_decode_words_array length %i" % (level, len(sub_decode_words_array)))
            WordMap.create_all_single_word_combinations(sub_decode_words_array, curr_dict, array_of_dicts, level + 1)
            if len(decode_words_array) == 1:
                # print("level %i - adding to array_of_dicts" % level)
                array_of_dicts.append(copy.copy(curr_dict))


class EncryptedWordWithOptions:
    def __init__(self, encrypted_word: str):
        self.encrypted_word = encrypted_word
        self.solution_words = []

    def __repr__(self):
        return self.encrypted_word + "[" + ",".join(self.solution_words) + "]"

    def copy_with_single_options(self):
        result = []

        for solution_word in self.solution_words:
            opt = EncryptedWordWithOptions(self.encrypted_word)
            opt.add_solution_word(solution_word)
            result.append(opt)

        return result

    def add_solution_word(self, word):
        self.solution_words.append(word)

    def has_any_solution_words(self) -> bool:
        return len(self.solution_words) > 0

    def get_solution_word_count(self) -> int:
        return len(self.solution_words)

    def get_solution_words(self):
        return self.solution_words

    def remove_solution_word(self, item_to_remove) -> bool:
        try:
            self.solution_words.remove(item_to_remove)
        except ValueError:
            return False

        return True

    def get_first_solution_word(self) -> str:
        return self.solution_words[0]

    def remove_word_that_do_not_match_letter(self, encrypted_letter, solution_letter):

        for encrypted_letter_index in range(len(self.encrypted_word)):
            current_encrypted_letter = self.encrypted_word[encrypted_letter_index]

            new_solution_words = []

            if current_encrypted_letter == encrypted_letter:
                for solution_word in self.solution_words:
                    if solution_word[encrypted_letter_index] == solution_letter:
                        new_solution_words.append(solution_word)

                self.solution_words = new_solution_words


class WordPair:
    def __init__(self, encrypted_word: str, solution_word: str):
        self.solution_word = solution_word
        self.encrypted_word = encrypted_word

    def is_word_possible(self) -> bool:
        if not self.has_same_length():
            return False

        return self.is_letter_possible()

    def has_same_length(self) -> bool:
        return len(self.encrypted_word) == len(self.solution_word)

    def is_letter_possible(self) -> bool:
        letter_dic = {}
        solution_letter_count_dic = {}

        for i in range(len(self.encrypted_word)):
            solution_letter = self.solution_word[i]
            encrypted_letter = self.encrypted_word[i]

            if encrypted_letter in letter_dic:
                if solution_letter != letter_dic[encrypted_letter]:
                    return False
            elif solution_letter in solution_letter_count_dic:
                return False
            else:
                letter_dic[encrypted_letter] = solution_letter
                solution_letter_count_dic[solution_letter] = 1
        return True
