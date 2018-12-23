import enum


class Card:
    def __init__(self, value: int, suite: int) -> None:
        self.value = value
        self.suite = suite

    def get_card_name(self):
        value_for_name = self.value + 2

        return "%i of Clubs" % value_for_name


