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
        if self.suite == 4:
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


