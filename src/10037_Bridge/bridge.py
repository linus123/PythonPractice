import sys
from bisect import bisect_left, bisect_right
from enum import Enum


class MoveTypes(Enum):
    FASTER = 1,
    SLOWER = 2,


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


class CrossResult:
    def __init__(self) -> None:
        self.total_number_of_seconds = 0
        self.crossings = []

    def add_crossing(self, person1: int, person2=None):
        if person2 is None:
            self.total_number_of_seconds += person1
            self.crossings.append([person1])
        else:
            self.total_number_of_seconds += max(person1, person2)
            self.crossings.append([person1, person2])


def get_min_time_to_cross(people: list) -> CrossResult:

    if len(people) == 1:
        cr = CrossResult()
        cr.add_crossing(people[0])
        return cr

    people_to_cross = SortedCollection()

    for person in people:
        people_to_cross.insert(person)

    crossed_people = SortedCollection()

    cross_type = MoveTypes.FASTER

    cr = CrossResult()

    while len(crossed_people) < len(people):

        if should_do_fast_first(people_to_cross):
            fastest_person = people_to_cross[0]
            second_slowest = people_to_cross[-2]

            cr.add_crossing(fastest_person, second_slowest)

            people_to_cross.remove(fastest_person)
            people_to_cross.remove(second_slowest)

            crossed_people.insert(fastest_person)
            crossed_people.insert(second_slowest)

            # **

            fastest_person = crossed_people[0]

            cr.add_crossing(fastest_person)

            crossed_people.remove(fastest_person)
            people_to_cross.insert(fastest_person)

            # **

            fastest_person = people_to_cross[0]
            slowest = people_to_cross[-1]

            cr.add_crossing(fastest_person, slowest)

            people_to_cross.remove(fastest_person)
            people_to_cross.remove(slowest)

            crossed_people.insert(fastest_person)
            crossed_people.insert(slowest)

            # **

            fastest_person = crossed_people[0]

            cr.add_crossing(fastest_person)

            crossed_people.remove(fastest_person)
            people_to_cross.insert(fastest_person)

            continue

        if cross_type == MoveTypes.FASTER:

            fastest_person = people_to_cross[0]
            next_fastest_person = people_to_cross[1]

            cr.add_crossing(fastest_person, next_fastest_person)

            people_to_cross.remove(fastest_person)
            people_to_cross.remove(next_fastest_person)

            crossed_people.insert(fastest_person)
            crossed_people.insert(next_fastest_person)

            cross_type = MoveTypes.SLOWER

            if len(people_to_cross) == 0:
                break

            fastest_person = crossed_people[0]

            cr.add_crossing(fastest_person)

            crossed_people.remove(fastest_person)
            people_to_cross.insert(fastest_person)

        elif cross_type == MoveTypes.SLOWER:

            slowest_person = people_to_cross[-1]
            next_slowest_person = people_to_cross[-2]

            cr.add_crossing(next_slowest_person, slowest_person)

            people_to_cross.remove(slowest_person)
            people_to_cross.remove(next_slowest_person)

            crossed_people.insert(slowest_person)
            crossed_people.insert(next_slowest_person)

            cross_type = MoveTypes.FASTER

            if len(people_to_cross) == 0:
                break

            fastest_person = crossed_people[0]

            cr.add_crossing(fastest_person)

            crossed_people.remove(fastest_person)
            people_to_cross.insert(fastest_person)

    return cr


def should_do_fast_first(people_to_cross: list) -> bool:
    if len(people_to_cross) < 4:
        return False

    fast_first_time = people_to_cross[-2] + people_to_cross[0] + people_to_cross[-1] + people_to_cross[0]

    slow_only = people_to_cross[1] + people_to_cross[0] + people_to_cross[-1] + people_to_cross[1]

    return fast_first_time < slow_only


def run_from_standard_in():

    first_line = sys.stdin.readline()
    number_of_test_cases = int(first_line.strip())

    blank_line = sys.stdin.readline()

    for test_case_counter in range(number_of_test_cases):

        current_line = sys.stdin.readline().strip()
        people_count = int(current_line)

        people = []

        for pc in range(people_count):
            current_line = sys.stdin.readline().strip()
            people.append(int(current_line))

        result = get_min_time_to_cross(people)

        print(result.total_number_of_seconds)

        for cross in result.crossings:
            print(" ".join(str(x) for x in cross))

        if test_case_counter != number_of_test_cases:
            print("")
            blank_line = sys.stdin.readline()


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()