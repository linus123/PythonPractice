import copy
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

        self.name = ""

    def __repr__(self) -> str:
        return "%s - %s" % (self.name, str(self.dice_values))

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
            score_dic[Category.LONG_STRAIGHT] = 35
        else:
            score_dic[Category.LONG_STRAIGHT] = 0

        if self.__is_short_straight():
            score_dic[Category.SHORT_STRAIGHT] = 25
        else:
            score_dic[Category.SHORT_STRAIGHT] = 0

        if self.__has_x_of_the_same_value(5):
            score_dic[Category.FIVE_OF_A_KIND] = 50
        else:
            score_dic[Category.FIVE_OF_A_KIND] = 0

        score_dic[Category.FOUR_OF_A_KIND] = self.__get_x_of_a_kind_sum(4)
        score_dic[Category.THREE_OF_A_KIND] = self.__get_x_of_a_kind_sum(3)

        chance_sum = 0
        sums = [0, 0, 0, 0, 0, 0]
        for v in self.dice_values:
            chance_sum += v

            for i in range(7):
                if v == i:
                    sums[i - 1] += i

        score_dic[Category.CHANCE] = chance_sum
        score_dic[Category.SIXES] = sums[5]
        score_dic[Category.FIVES] = sums[4]
        score_dic[Category.FOURS] = sums[3]
        score_dic[Category.THREES] = sums[2]
        score_dic[Category.TWOS] = sums[1]
        score_dic[Category.ONES] = sums[0]

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

    def __has_x_of_the_same_value(self, x: int) -> bool:
        for key, value in self.count_dic.items():
            if value == x:
                return True

        return False

    def __get_x_of_a_kind_sum(self, x: int) -> int:
        for key, value in self.count_dic.items():
            if value >= x:
                return x * key

        return 0

    # **

    def get_score(self, cat: Category) -> int:
        return self.score_dic[cat]


class ScoreSequence:

    def __init__(self):
        self.__sequence_dic = {}

    def set_category(self, cat: Category, roll: ThrowRoll):
        self.__sequence_dic[cat] = roll

    def create_copy(self):
        ss = ScoreSequence()
        ss.__sequence_dic = copy.copy(self.__sequence_dic)
        return ss

    def get_score(self) -> int:
        grand_total = 0

        for key, roll in self.__sequence_dic.items():
            grand_total += roll.get_score(key)

        if self.__should_add_bonus():
            grand_total += 35

        return grand_total

    def __should_add_bonus(self):
        bonus_categories = [Category.ONES,
                            Category.TWOS,
                            Category.THREES,
                            Category.FOURS,
                            Category.FIVES,
                            Category.SIXES]

        total = 0

        for c in bonus_categories:
            total += self.__sequence_dic[c].get_score(c)

        return total >= 63


class ScoreSequenceFactory:
    def __init__(self) -> None:
        self.rolls = []

    def add_roll(self, values: list, name: str):
        roll = ThrowRoll(values)
        if name is not None:
            roll.name = name
        self.rolls.append(roll)

    def is_complete(self) -> bool:
        return len(self.rolls) >= 13

    def get_all_combinations(self):
        cat_array = []

        for cat in Category:
            cat_array.append(cat)

        ss = ScoreSequence()

        opts = self.__recurse(cat_array, self.rolls, ss)

        for o in opts:
            yield o

    def __recurse(self, categories, rolls, current_ss):

        if len(categories) == 0:
            yield current_ss.create_copy()

        for roll_index in range(len(rolls)):
            roll = rolls[roll_index]
            current_ss.set_category(categories[0], roll)

            less_rolls1 = rolls[0:roll_index]
            less_rolls2 = rolls[roll_index + 1:]

            less_rolls = less_rolls1 + less_rolls2

            foo = self.__recurse(categories[1:], less_rolls, current_ss)

            for f in foo:
                yield f


class YahtzeeScorer:
    def __init__(self) -> None:
        self.rolls = []

    def add_roll(self, values: list):
        self.rolls.append(ThrowRoll(values))

    def is_complete(self) -> bool:
        return len(self.rolls) >= 13

    def get_game_score(self) -> str:
        score_array = ["0"] * 15

        score_array[0] = str(self.rolls[0].get_score(Category.ONES))
        score_array[1] = str(self.rolls[1].get_score(Category.TWOS))
        score_array[2] = str(self.rolls[2].get_score(Category.THREES))
        score_array[3] = str(self.rolls[3].get_score(Category.FOURS))
        score_array[4] = str(self.rolls[4].get_score(Category.FIVES))
        score_array[5] = str(self.rolls[5].get_score(Category.SIXES))
        score_array[6] = str(self.rolls[6].get_score(Category.CHANCE))
        score_array[7] = str(self.rolls[7].get_score(Category.THREE_OF_A_KIND))
        score_array[8] = str(self.rolls[8].get_score(Category.FOUR_OF_A_KIND))
        score_array[9] = str(self.rolls[9].get_score(Category.FIVE_OF_A_KIND))
        score_array[10] = str(self.rolls[10].get_score(Category.SHORT_STRAIGHT))
        score_array[11] = str(self.rolls[11].get_score(Category.LONG_STRAIGHT))
        score_array[12] = str(self.rolls[12].get_score(Category.FULL_HOUSE))
        score_array[13] = str(0)

        grand_total = self.rolls[0].get_score(Category.ONES) \
                      + self.rolls[1].get_score(Category.TWOS) \
                      + self.rolls[2].get_score(Category.THREES) \
                      + self.rolls[3].get_score(Category.FOURS) \
                      + self.rolls[4].get_score(Category.FIVES) \
                      + self.rolls[5].get_score(Category.SIXES) \
                      + self.rolls[6].get_score(Category.CHANCE) \
                      + self.rolls[7].get_score(Category.THREE_OF_A_KIND) \
                      + self.rolls[8].get_score(Category.FOUR_OF_A_KIND) \
                      + self.rolls[9].get_score(Category.FIVE_OF_A_KIND) \
                      + self.rolls[10].get_score(Category.SHORT_STRAIGHT) \
                      + self.rolls[11].get_score(Category.LONG_STRAIGHT) \
                      + self.rolls[12].get_score(Category.FULL_HOUSE) \
                      + 0

        score_array[14] = str(grand_total)

        return " ".join(score_array)
