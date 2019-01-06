import copy
import queue
import sys


class DoubletWord:
    def __init__(self, word: str) -> None:
        self.word = word
        self.length = len(word)

        self.related_words = []

    def add_related_word_index(self, index: int):
        self.related_words.append(index)

    def has_any_related_words(self) -> bool:
        return len(self.related_words) > 0

    def __str__(self) -> str:
        return self.word

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

    def __init__(self, words) -> None:

        self.doublet_words = []

        for w in words:
            self.__add_word(w)

    def __add_word(self, sword):
        new_word = DoubletWord(sword)

        for saved_word_index in range(len(self.doublet_words)):
            saved_word = self.doublet_words[saved_word_index]
            if not has_more_than_one_difference_same_length_match(new_word, saved_word):
                new_word.add_related_word_index(saved_word_index)
                saved_word.add_related_word_index(len(self.doublet_words))

        self.doublet_words.append(new_word)

    def find_shortest_path(self, start_word_raw: str, end_word_raw: str):
        start_word_index = -1

        for word_under_eval_index in range(len(self.doublet_words)):
            if start_word_raw == self.doublet_words[word_under_eval_index].word:
                start_word_index = word_under_eval_index
                break

        if start_word_index < 0:
            return []

        visited_dict = {start_word_index: -1}

        next_item_q = queue.Queue()
        next_item_q.put(start_word_index)

        found = False
        word_under_eval_index = -1

        while not found:

            if next_item_q.empty():
                break

            parent_word_index = next_item_q.get()
            parent_word = self.doublet_words[parent_word_index]

            if not parent_word.has_any_related_words():
                continue

            for word_under_eval_index in parent_word.related_words:
                if word_under_eval_index == parent_word_index:
                    continue

                if word_under_eval_index in visited_dict:
                    continue

                word_under_eval = self.doublet_words[word_under_eval_index]

                visited_dict[word_under_eval_index] = parent_word_index

                if word_under_eval.word == end_word_raw:
                    found = True
                    break

                next_item_q.put(word_under_eval_index)

        if found:
            path = []

            current = word_under_eval_index

            while current != -1:
                path.append(self.doublet_words[current].word)
                current = visited_dict[current]

            path.reverse()

            return path
        else:
            return None

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

def run_from_standard_in():

    line = sys.stdin.readline().strip()
    words = []
    while line != "":
        words.append(line)
        line = sys.stdin.readline().strip()

    dpf = DoubletPathFinder(words)

    line = sys.stdin.readline().strip()
    while line != "":
        line_s = line.split(" ")

        result = dpf.find_shortest_path(line_s[0], line_s[1])

        if result is None:
            print("No solution.")
        else:
            for wd in result:
                print(wd)

        line = sys.stdin.readline().strip()

        if line != "":
            print("")



def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()