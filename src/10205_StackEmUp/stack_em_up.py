import enum


class Card:
    def __init__(self, value: int, suite: int) -> None:
        self.value = value
        self.suite = suite

    def get_card_name(self):
        value_for_name = str(self.value + 2)

        if self.value == 9:
            value_for_name = "Jack"

        return "%s of Clubs" % value_for_name

    def get_id(self):
        return self.value + 1


