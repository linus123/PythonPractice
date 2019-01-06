
class DoubletWord:
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


def has_more_than_one_difference_primitive(sword1: str, sword2: str):

    return has_more_than_one_difference(
        DoubletWord(sword1),
        DoubletWord(sword2)
    )


def has_more_than_one_difference(word1: DoubletWord, word2: DoubletWord):

    if abs(word1.length - word2.length) > 1:
        return True

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

