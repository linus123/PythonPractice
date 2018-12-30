import copy


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


class SolutionMap:
    def __init__(self) -> None:
        self.__encrypted_word_dict = {}
        self.__taken_solution_word_dict = {}
        self.__letter_map_dict = {}
        self.__taken_solution_letter_dict = {}

    def print_state(self):
        print(self.__encrypted_word_dict)

    def try_to_set_word(self, enc_word: SingleWord, sol_word: SingleWord) -> bool:
        if not enc_word.is_word_possible(sol_word):
            return False

        if self.__violates_letter_map(enc_word, sol_word):
            return False

        self.__encrypted_word_dict[enc_word.word] = sol_word
        self.__taken_solution_word_dict[sol_word.word] = 1
        self.__update_letter_map(enc_word, sol_word)
        return True

    def __update_letter_map(self, enc_word: SingleWord, sol_word: SingleWord):
        for letter_index in range(enc_word.unique_letter_word_length):
            enc_letter = enc_word.unique_letter_word[letter_index]
            sol_letter = sol_word.unique_letter_word[letter_index]

            self.__letter_map_dict[enc_letter] = sol_letter
            self.__taken_solution_letter_dict[sol_letter] = 1

    def __violates_letter_map(self, enc_word: SingleWord, sol_word: SingleWord):
        for letter_index in range(enc_word.unique_letter_word_length):
            enc_letter = enc_word.unique_letter_word[letter_index]
            sol_letter = sol_word.unique_letter_word[letter_index]

            if enc_letter in self.__letter_map_dict:
                if self.__letter_map_dict[enc_letter] != sol_letter:
                    return True
            else:
                if sol_letter in self.__taken_solution_letter_dict:
                    return True

        return False

    def has_mapped_solution_word(self, sol_word):
        return sol_word.word in self.__taken_solution_word_dict

    def get_decrypted_line(self, encrypted_words: list):

        word_array = []

        for word in encrypted_words:
            word_array.append(self.__encrypted_word_dict[word].word)

        return ' '.join(word_array)

    def has_solution_for_encrypted_word(self, enc_word):
        return enc_word.word in self.__encrypted_word_dict

    def get_solution_for_encrypted_word(self, enc_word):
        return self.__encrypted_word_dict[enc_word]

    def create_copy(self):
        c = SolutionMap()
        c.__encrypted_word_dict = copy.copy(self.__encrypted_word_dict)
        c.__taken_solution_word_dict = copy.copy(self.__taken_solution_word_dict)
        c.__letter_map_dict = copy.copy(self.__letter_map_dict)
        c.__taken_solution_letter_dict = copy.copy(self.__taken_solution_letter_dict)

        return c


class LengthKeyedDict:

    def __init__(self, words) -> None:

        largest_word_length = 0

        word_dict = {}
        word_lengths = set()

        for word in words:
            word_len = len(word)
            word_lengths.add(word_len)

            if word_len in word_dict:
                word_dict[word_len].add(word)
            else:
                word_dict[word_len] = {word}

        sw_word_dict = {}

        for key in word_dict.keys():
            sw_word_dict[key] = []
            for word in word_dict[key]:
                sw_word_dict[key].append(SingleWord(word))

            sw_word_dict[key].sort(key=lambda sw: sw.word)

        self.__dict = sw_word_dict
        self.largest_word_length = largest_word_length
        self.word_lengths = sorted(list(word_lengths), reverse=True)

    def has_words_of_length(self, word_len) -> bool:
        return word_len in self.__dict

    def get_words(self, word_len) -> list:
        return self.__dict[word_len]
