def crypt_decrypt(encrypted_line, solution_words):

    encrypted_words = convert_to_array(encrypted_line)

    if len(encrypted_words) == 0:
        return ""

    solution_words = clean_array(solution_words)

    word_map = WordMap(solution_words)

    for encrypted_word in encrypted_words:
        word_map.process_encrypted_word(encrypted_word)

    has_solution = word_map.calculate_solution()

    if not has_solution:
        return get_no_solution(encrypted_words)

    s = ""

    for encrypted_word in encrypted_words:
        s += str(word_map.get_word(encrypted_word)) + " "

    return s.strip()


def clean_array(word_dictionary):
    return [word.strip() for word in word_dictionary]


def convert_to_array(encrypted_line):
    encrypted_line = encrypted_line.strip()

    if encrypted_line == "":
        return []

    encrypted_words = encrypted_line.split(' ')
    encrypted_words = [word.strip() for word in encrypted_words]
    return encrypted_words


def get_no_solution(encrypted_words):
    s = ""

    for _ in encrypted_words:
        s += ('*' * len(_)) + " "

    return s.strip()


def is_already_mapped(letter, decode_letters):
    for key, letter_array in decode_letters.items():
        if letter in letter_array:
            return True
    return False


class EncryptedWordWithOptions:
    def __init__(self, encrypted_word: str):
        self.encrypted_word = encrypted_word
        self.solution_words = []

    def add_solution_word(self, word):
        self.solution_words.append(word)

    def has_any_solution_words(self) -> bool:
        return len(self.solution_words) > 0

    def get_solution_word_count(self) -> int:
        return len(self.solution_words)

    def delete_all_solution_words_except_first(self):
        del self.solution_words[1:]

    def safe_array_remove(self, item_to_remove):
        try:
            self.solution_words.remove(item_to_remove)
        except ValueError:
            return False

        return True

    def get_first_solution_word(self) -> str:
        return self.solution_words[0]


class WordMap:
    def __init__(self, solution_words):
        self.solution_words = solution_words
        self.decode_words = {}

    def process_encrypted_word(self, encrypted_word: str):
        if encrypted_word in self.decode_words:
            return

        encrypted_word_obj = EncryptedWordWithOptions(encrypted_word)

        for solution_word in self.solution_words:

            word_pair = WordPair(encrypted_word_obj.encrypted_word, solution_word)

            if word_pair.is_word_possible():
                encrypted_word_obj.add_solution_word(solution_word)

        self.decode_words[encrypted_word] = encrypted_word_obj

    def calculate_solution(self) -> bool:
        if len(self.decode_words) <= 0:
            return False

        has_solution = self.all_decode_words_have_at_least_one_item()

        if not has_solution:
            return False

        has_solution = self.remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option()

        if not has_solution:
            return False

        has_solution = self.choose_single_option_when_word_has_multiples()

        if not has_solution:
            return False

        return True

    def all_decode_words_have_at_least_one_item(self):
        for key, encrypted_word in self.decode_words.items():
            if not encrypted_word.has_any_solution_words():
                return False

        return True

    def remove_all_decode_words_from_all_other_items_where_word_only_has_single_decode_option(self):
        for key, decode_word_array in self.decode_words.items():
            if decode_word_array.get_solution_word_count() == 1:
                has_solution = self.remove_word_from_decode_words(decode_word_array.get_first_solution_word(), key)
                if not has_solution:
                    return False

        return True

    def choose_single_option_when_word_has_multiples(self):
        for key, encrypted_word in self.decode_words.items():

            if encrypted_word.get_solution_word_count() > 1:
                encrypted_word.delete_all_solution_words_except_first()

                first_solution_word = encrypted_word.get_first_solution_word()

                has_solution = self.remove_word_from_decode_words(first_solution_word, key)

                if not has_solution:
                    return False

        return True

    def remove_word_from_decode_words(self, word_to_remove: str, key_to_skip: str):
        for key, encrypted_word in self.decode_words.items():
            if key != key_to_skip:
                encrypted_word.safe_array_remove(word_to_remove)
                if encrypted_word.get_solution_word_count() == 0:
                    return False
        return True

    def get_word(self, encrypted_word: str) -> str:
        return self.decode_words[encrypted_word].get_first_solution_word()


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

