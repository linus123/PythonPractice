import sys


class Card:
    def __init__(self, value: int, suite: int) -> None:
        if value > 12:
            raise ValueError("Value cannot be greater than 13")

        if suite > 3:
            raise ValueError("Suite cannot be greater than 3")

        self.value = value
        self.suite = suite

    def get_card_name(self):
        value_for_name = self.get_value_name()

        suite_for_name = self.get_suite_name()

        return "%s of %s" % (value_for_name, suite_for_name)

    def get_suite_name(self):
        suite_for_name = "Clubs"

        if self.suite == 1:
            suite_for_name = "Diamonds"
        if self.suite == 2:
            suite_for_name = "Hearts"
        if self.suite == 3:
            suite_for_name = "Spades"

        return suite_for_name

    def get_value_name(self):
        value_for_name = str(self.value + 2)

        if self.value == 9:
            value_for_name = "Jack"
        if self.value == 10:
            value_for_name = "Queen"
        if self.value == 11:
            value_for_name = "King"
        if self.value == 12:
            value_for_name = "Ace"

        return value_for_name

    def get_id(self):
        return self.value + 1 + self.suite * 13


class Game:
    def __init__(self) -> None:
        self.deck = Game.create_deck()
        self.shuffle = []

    @staticmethod
    def create_deck() -> list:
        deck = []

        for suite_count in range(4):
            for value_count in range(13):
                deck.append(Card(value_count, suite_count))

        return deck

    def add_shuffle(self, shuffle: list):
        self.shuffle.append(shuffle)

    def apply_shuffle(self, shuffle_num):
        target_shuffle = self.shuffle[shuffle_num - 1]

        new_deck = [0] * 52

        for deck_index in range(52):
            target_deck_index = target_shuffle[deck_index] - 1
            new_deck[deck_index] = self.deck[target_deck_index]

        self.deck = new_deck

    def get_current_deck(self):
        for card in self.deck:
            yield card.get_card_name()


def run_from_standard_in():

    first_line = sys.stdin.readline()
    number_of_test_cases = int(first_line.strip())
    blank_line = sys.stdin.readline()

    for test_case_counter in range(number_of_test_cases):
        shuffle_type_count_line = sys.stdin.readline()
        shuffle_type_count = int(shuffle_type_count_line.strip())

        current_game = Game()

        for shuffle_type_index in range(shuffle_type_count):
            numbers_line = sys.stdin.readline().strip()
            numbers_list = numbers_line.split(" ")
            shuffle_number_array = []
            for number_string in numbers_list:
                shuffle_number_array.append(int(number_string))
            current_game.add_shuffle(shuffle_number_array)

        for line in sys.stdin:
            clean_line = line.strip()
            if clean_line == "":
                break
            current_game.apply_shuffle(int(clean_line))

        cards = current_game.get_current_deck()

        if test_case_counter == 0:
            is_first = False
        else:
            print("")

        for card in cards:
            print(card)


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()