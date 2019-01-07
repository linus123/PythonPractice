import queue
import sys
from bisect import bisect_left, bisect_right


class SortedCollection(object):
    '''Sequence sorted by a key function.
    SortedCollection() is much easier to work with than using bisect() directly.
    It supports key functions like those use in sorted(), min(), and max().
    The result of the key function call is saved so that keys can be searched
    efficiently.
    Instead of returning an insertion-point which can be hard to interpret, the
    five find-methods return a specific item in the sequence. They can scan for
    exact matches, the last item less-than-or-equal to a key, or the first item
    greater-than-or-equal to a key.
    Once found, an item's ordinal position can be located with the index() method.
    New items can be added with the insert() and insert_right() methods.
    Old items can be deleted with the remove() method.
    The usual sequence methods are provided to support indexing, slicing,
    length lookup, clearing, copying, forward and reverse iteration, contains
    checking, item counts, item removal, and a nice looking repr.
    Finding and indexing are O(log n) operations while iteration and insertion
    are O(n).  The initial sort is O(n log n).
    The key function is stored in the 'key' attibute for easy introspection or
    so that you can assign a new key function (triggering an automatic re-sort).
    In short, the class was designed to handle all of the common use cases for
    bisect but with a simpler API and support for key functions.
    >>> from pprint import pprint
    >>> from operator import itemgetter
    >>> s = SortedCollection(key=itemgetter(2))
    >>> for record in [
    ...         ('roger', 'young', 30),
    ...         ('angela', 'jones', 28),
    ...         ('bill', 'smith', 22),
    ...         ('david', 'thomas', 32)]:
    ...     s.insert(record)
    >>> pprint(list(s))         # show records sorted by age
    [('bill', 'smith', 22),
     ('angela', 'jones', 28),
     ('roger', 'young', 30),
     ('david', 'thomas', 32)]
    >>> s.find_le(29)           # find oldest person aged 29 or younger
    ('angela', 'jones', 28)
    >>> s.find_lt(28)           # find oldest person under 28
    ('bill', 'smith', 22)
    >>> s.find_gt(28)           # find youngest person over 28
    ('roger', 'young', 30)
    >>> r = s.find_ge(32)       # find youngest person aged 32 or older
    >>> s.index(r)              # get the index of their record
    3
    >>> s[3]                    # fetch the record at that index
    ('david', 'thomas', 32)
    >>> s.key = itemgetter(0)   # now sort by first name
    >>> pprint(list(s))
    [('angela', 'jones', 28),
     ('bill', 'smith', 22),
     ('david', 'thomas', 32),
     ('roger', 'young', 30)]
    '''

    def __init__(self, iterable=(), key=None):
        self._given_key = key
        key = (lambda x: x) if key is None else key
        decorated = sorted((key(item), item) for item in iterable)
        self._keys = [k for k, item in decorated]
        self._items = [item for k, item in decorated]
        self._key = key

    def _getkey(self):
        return self._key

    def _setkey(self, key):
        if key is not self._key:
            self.__init__(self._items, key=key)

    def _delkey(self):
        self._setkey(None)

    key = property(_getkey, _setkey, _delkey, 'key function')

    def clear(self):
        self.__init__([], self._key)

    def copy(self):
        return self.__class__(self, self._key)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, i):
        return self._items[i]

    def __iter__(self):
        return iter(self._items)

    def __reversed__(self):
        return reversed(self._items)

    def __repr__(self):
        return '%s(%r, key=%s)' % (
            self.__class__.__name__,
            self._items,
            getattr(self._given_key, '__name__', repr(self._given_key))
        )

    def __reduce__(self):
        return self.__class__, (self._items, self._given_key)

    def __contains__(self, item):
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return item in self._items[i:j]

    def index(self, item):
        'Find the position of an item.  Raise ValueError if not found.'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)

        j_ = self._items[i:j]

        return j_.index(item) + i

    def count(self, item):
        'Return number of occurrences of item'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return self._items[i:j].count(item)

    def insert(self, item):
        'Insert a new item.  If equal keys are found, add to the left'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        self._keys.insert(i, k)
        self._items.insert(i, item)

    def insert_right(self, item):
        'Insert a new item.  If equal keys are found, add to the right'
        k = self._key(item)
        i = bisect_right(self._keys, k)
        self._keys.insert(i, k)
        self._items.insert(i, item)

    def remove(self, item):
        'Remove first occurence of item.  Raise ValueError if not found'
        i = self.index(item)
        del self._keys[i]
        del self._items[i]

    def find(self, k):
        'Return first item with a key == k.  Raise ValueError if not found.'
        i = bisect_left(self._keys, k)
        if i != len(self) and self._keys[i] == k:
            return self._items[i]
        raise ValueError('No item found with key equal to: %r' % (k,))

    def find_with_index(self, k):
        'Return first item with a key == k.  Raise ValueError if not found.'
        i = bisect_left(self._keys, k)
        if i != len(self) and self._keys[i] == k:
            return self._items[i], i
        raise ValueError('No item found with key equal to: %r' % (k,))

    def find_le(self, k):
        'Return last item with a key <= k.  Raise ValueError if not found.'
        i = bisect_right(self._keys, k)
        if i:
            return self._items[i-1]
        raise ValueError('No item found with key at or below: %r' % (k,))

    def find_lt(self, k):
        'Return last item with a key < k.  Raise ValueError if not found.'
        i = bisect_left(self._keys, k)
        if i:
            return self._items[i-1]
        raise ValueError('No item found with key below: %r' % (k,))

    def find_ge(self, k):
        'Return first item with a key >= equal to k.  Raise ValueError if not found'
        i = bisect_left(self._keys, k)
        if i != len(self):
            return self._items[i]
        raise ValueError('No item found with key at or above: %r' % (k,))

    def find_gt(self, k):
        'Return first item with a key > k.  Raise ValueError if not found'
        i = bisect_right(self._keys, k)
        if i != len(self):
            return self._items[i]
        raise ValueError('No item found with key above: %r' % (k,))


class DoubletWord:
    def __ne__(self, o: object) -> bool:
        return self.word.__ne__(object.word)

    def __eq__(self, o: object) -> bool:
        return self.word.__eq__(object.word)

    def __init__(self, word: str) -> None:
        self.word = word
        self.length = len(word)

        self.related_words = set()

        self.related_words_populated = False

    def add_related_word_index(self, index: int):
        self.related_words.add(index)

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


def get_word(sw: DoubletWord):
    return sw.word


class DoubletPathFinder:

    def __init__(self, words: list) -> None:

        self.doublet_words = []

        sc = SortedCollection(key=get_word)

        for sword in words:
            sc.insert(DoubletWord(sword))

        self.doublet_words = sc

        # touch_count = 0
        #
        # for word_index in range(len(self.doublet_words)):
        #     word = self.doublet_words[word_index]
        #
        #     word_combos = get_word_combinations(word.word)
        #
        #     for combo_word in word_combos:
        #
        #         find_word = None
        #         find_word_index = -1
        #
        #         touch_count += 1
        #
        #         try:
        #             find_word, find_word_index = self.doublet_words.find_with_index(combo_word)
        #         except ValueError:
        #             pass
        #
        #         if find_word is not None and find_word_index > 0:
        #             word.add_related_word_index(find_word_index)
        #             find_word.add_related_word_index(word_index)
        #
        # print(touch_count)

    def populate_related_words(self, word_index):
        word = self.doublet_words[word_index]

        word_combos = get_word_combinations(word.word)

        for combo_word in word_combos:

            find_word = None
            find_word_index = -1

            try:
                find_word, find_word_index = self.doublet_words.find_with_index(combo_word)
            except ValueError:
                pass

            if find_word is not None and find_word_index > 0:
                word.add_related_word_index(find_word_index)
                # find_word.add_related_word_index(word_index)

        word.related_words_populated = True


    def find_shortest_path(self, start_word_raw: str, end_word_raw: str):
        start_word_index = -1

        try:
            start_word, start_word_index = self.doublet_words.find_with_index(start_word_raw)
        except ValueError:
            pass

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

            if not parent_word.related_words_populated:
                self.populate_related_words(parent_word_index)

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


def get_word_combinations(word: str):

    for index in range(len(word)):
        for c in range(ord('a'), ord('z')+1):
            if chr(c) != word[index]:
                yield word[:index] + chr(c) + word[index + 1:]


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()