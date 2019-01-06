import copy


class DoubletWord:
    def __str__(self) -> str:
        return self.word

    def __init__(self, word: str) -> None:
        self.word = word
        self.length = len(word)

    def __repr__(self) -> str:
        return self.word

    def __getitem__(self, item):
        return self.word[item]

    def has_letter(self, index: int):
        if index < 0:
            return False

        if index >= len(self.word):
            return False

        return True

    def get_letter_or_blank(self, index: int):
        if index < 0:
            return ""

        if index >= len(self.word):
            return ""

        return self.word[index]

class DoubletPathFinder:

    def __init__(self, words: list) -> None:

        doublet_words = []

        for word in words:
            doublet_words.append(DoubletWord(word))

        self.doublet_words = doublet_words

    def find_shortest_path(self, start_word_raw: str, end_word_raw: str):
        start_word_index = -1

        for index in range(len(self.doublet_words)):
            if start_word_raw == self.doublet_words[index].word:
                start_word_index = index
                break

        if start_word_index < 0:
            return []

        new_words = self.doublet_words[:start_word_index] + self.doublet_words[start_word_index + 1:]

        word_path = [self.doublet_words[start_word_index].word]

        path = self.__recurse(
            new_words,
            self.doublet_words[start_word_index],
            DoubletWord(end_word_raw),
            word_path
        )

        return path

    def __recurse(
            self,
            words,
            current_word: DoubletWord,
            end_word: DoubletWord,
            word_path: list):

        recurse_items = []

        for word_index in range(len(words)):
            word = words[word_index]
            if not has_more_than_one_difference(current_word, word):

                if end_word.word == word.word:
                    word_path.append(word.word)
                    return word_path
                else:
                    new_word_path = copy.copy(word_path)
                    new_word_path.append(word.word)

                    new_words = words[:word_index] + words[word_index + 1:]

                    recurse_items.append((new_words, word, end_word, new_word_path))

        for itm in recurse_items:
            inner_path = self.__recurse(
                itm[0],
                itm[1],
                itm[2],
                itm[3]
            )

            if inner_path is not None:
                return inner_path

        return None


def find_doublets(start_word: str, end_word: str, words: list):
    return []


def has_more_than_one_difference_primitive(sword1: str, sword2: str):
    return has_more_than_one_difference(
        DoubletWord(sword1),
        DoubletWord(sword2)
    )


def has_more_than_one_difference_same_length_match(
        word1: DoubletWord,
        word2: DoubletWord
):
    letter_index = 0
    diff_count = 0

    while letter_index < word1.length:

        if diff_count > 1:
            break

        if word1[letter_index] != word2[letter_index]:
            diff_count += 1

        letter_index += 1

    return diff_count > 1


def has_more_than_one_difference(
        word1: DoubletWord,
        word2: DoubletWord
):
    if abs(word1.length - word2.length) > 1:
        return True

    if word1.length == word2.length:
        return has_more_than_one_difference_same_length_match(word1, word2)

    letter_index = 0
    word1_index = 0
    word2_index = 0
    diff_count = 0

    word_scan_is_done = False

    while not word_scan_is_done:

        if diff_count > 1:
            word_scan_is_done = True
            continue

        if not word1.has_letter(word1_index) and not word2.has_letter(word2_index):
            word_scan_is_done = True
            continue

        if not word1.has_letter(word1_index) and word2.has_letter(word2_index):
            diff_count += 1
            word_scan_is_done = True
            continue

        if word1.has_letter(word1_index) and not word2.has_letter(word2_index):
            diff_count += 1
            word_scan_is_done = True
            continue

        if word1[word1_index] != word2[word2_index]:
            diff_count += 1

            # word1 look ahead
            if word1.get_letter_or_blank(word1_index + 1) == word2[word2_index]:
                word2_index -= 1

            # word2 look ahead
            if word1[word1_index] == word2.get_letter_or_blank(word2_index + 1):
                word1_index -= 1

        word1_index += 1
        word2_index += 1
        letter_index += 1

    return diff_count > 1
