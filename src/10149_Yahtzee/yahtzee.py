from enum import Enum


class Category(Enum):
    ONES = 1,
    TWOS = 2,
    THREES = 3,
    FOURS = 4,
    FIVES = 5,
    SIXES = 6,
    CHANCE = 7,
    THREE_OF_A_KIND = 8,
    FOUR_OF_A_KIND = 9,
    FIVE_OF_A_KIND = 10,
    SHORT_STRAIGHT = 11,
    LONG_STRAIGHT = 12,
    FULL_HOUSE = 13


class ThrowRoll:
    def __init__(self, dice_values: list) -> None:

        if len(dice_values) != 5:
            raise ValueError("Array must have 5 values")

        dice_values.sort()

        self.dice_values = dice_values

        self.count_dic = self.__create_count_dic()
        self.score_dic = self.__create_score_dic()

    def __create_count_dic(self):
        value_dic = {}
        for dic_value in self.dice_values:
            if dic_value in value_dic:
                value_dic[dic_value] += 1
            else:
                value_dic[dic_value] = 1
        return value_dic

    def __create_score_dic(self):
        has_two_of_any_kind = False
        has_three_of_any_kind = False

        score_dic = {}

        is_full_house = self.__is_full_house(has_three_of_any_kind, has_two_of_any_kind)

        if is_full_house:
            score_dic[Category.FULL_HOUSE] = 40
        else:
            score_dic[Category.FULL_HOUSE] = 0

        if self.__is_long_straight():
            score_dic[Category.LONG_STRAIGHT] = 30
        else:
            score_dic[Category.LONG_STRAIGHT] = 0

        if self.__is_short_straight():
            score_dic[Category.SHORT_STRAIGHT] = 25
        else:
            score_dic[Category.SHORT_STRAIGHT] = 0

        return score_dic

    def __is_full_house(self, has_three_of_any_kind, has_two_of_any_kind):
        for key, value in self.count_dic.items():
            if value == 2:
                has_two_of_any_kind = True

            if value == 3:
                has_three_of_any_kind = True

        return has_two_of_any_kind and has_three_of_any_kind

    def __is_long_straight(self) -> bool:
        index = 1

        while index < 5:

            if self.dice_values[index] - (self.dice_values[0] + index) != 0:
                return False

            index += 1

        return True

    def __is_short_straight(self) -> bool:
        if 1 in self.count_dic \
                and 2 in self.count_dic \
                and 3 in self.count_dic \
                and 4 in self.count_dic:
            return True

        if 2 in self.count_dic \
                and 3 in self.count_dic \
                and 4 in self.count_dic \
                and 5 in self.count_dic:
            return True

        return False

    # **

    def get_score(self, cat: Category) -> int:
        return self.score_dic[cat]

    def is_short_straight(self) -> bool:
        return self.score_dic[Category.SHORT_STRAIGHT] > 0

    def has_x_of_the_same_value(self, x: int) -> bool:
        for key, value in self.count_dic.items():
            if value == x:
                return True

        return False

    def get_x_of_a_kind_sum(self, x: int) -> int:
        for key, value in self.count_dic.items():
            if value == x:
                return value * key

        return 0

    def get_five_of_a_kind_sum(self) -> int:
        return self.get_x_of_a_kind_sum(5)

    def get_four_of_a_kind_sum(self) -> int:
        return self.get_x_of_a_kind_sum(4)

    def get_three_of_a_kind_sum(self) -> int:
        return self.get_x_of_a_kind_sum(3)

    def get_change_value(self) -> int:
        s = 0
        for dice_value in self.dice_values:
            s += dice_value

        return s

    def get_sum_of_all(self, v) -> int:
        if v in self.count_dic:
            return self.count_dic[v] * v

        return 0
