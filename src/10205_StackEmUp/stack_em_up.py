import enum


class Card:
    def __init__(self, value: int, suite: int) -> None:
        self.value = value
        self.suite = suite

    def get_card_name(self):
        value_for_name = str(self.value + 2)

        if self.value == 9:
            value_for_name = "Jack"

        if self.value == 10:
            value_for_name = "Queen"

        if self.value == 11:
            value_for_name = "King"

        if self.value == 12:
            value_for_name = "Ace"

        return "%s of Clubs" % value_for_name

    def get_id(self):
        return self.value + 1


