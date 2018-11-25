def crypt_decrypt(encrypted_line, solution_words):

    encrypted_words = convert_to_array(encrypted_line)

    if len(encrypted_words) == 0:
        return ""

    solution_words = clean_array(solution_words)

    word_map = WordMap(solution_words)

    for encrypted_word in encrypted_words:
        word_map.process_encrypted_word(encrypted_word)

    has_solution = word_map.has_solution()

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


class WordMap:
    def __init__(self, solution_words):
        self.solution_words = solution_words
        self.decode_words = {}

    def process_encrypted_word(self, encrypted_word):
        single_letter_options = []

        for solution_word in self.solution_words:
            single_letter_options.append(solution_word)
            self.decode_words[encrypted_word] = single_letter_options

    def has_solution(self):
        for key, letter_array in self.decode_words.items():
            if len(letter_array) == 1:
                still_as_solution = self.remove_letter_from_options(letter_array[0], self.decode_words, key)
                if not still_as_solution:
                    return False

        # for multiples .. pick one
        for key, letter_array in self.decode_words.items():
            if len(letter_array) > 1:
                # delete all items except first one
                del letter_array[1:]
                still_as_solution = self.remove_letter_from_options(letter_array[0], self.decode_words, key)
                if not still_as_solution:
                    return False

        return True

    def remove_letter_from_options(self, letter_to_remove, decode_letters, key_to_skip):
        for key, letter_array in decode_letters.items():
            if key != key_to_skip:
                letter_array.remove(letter_to_remove)
                if len(letter_array) == 0:
                    return False
        return True

    def get_word(self, encrypted_word):
        return self.decode_words[encrypted_word][0]


class LetterMap:
    def __init__(self, solution_words):
        self.solution_words = solution_words
        self.decode_letters = {}

    def process_encrypted_word(self, word):
        pass

