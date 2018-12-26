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

        if 3 in self.count_dic \
                and 4 in self.count_dic \
                and 5 in self.count_dic \
                and 6 in self.count_dic:
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

    def __get_score_as_string(self, cat: Category):
        if cat in self.__sequence_dic:
            return str(self.__sequence_dic[cat].get_score(cat))
        else:
            return "0"

    def get_formatted_score(self):

        score_array = []

        score_array.append(self.__get_score_as_string(Category.ONES))
        score_array.append(self.__get_score_as_string(Category.TWOS))
        score_array.append(self.__get_score_as_string(Category.THREES))
        score_array.append(self.__get_score_as_string(Category.THREES))
        score_array.append(self.__get_score_as_string(Category.FOURS))
        score_array.append(self.__get_score_as_string(Category.FIVES))
        score_array.append(self.__get_score_as_string(Category.SIXES))
        score_array.append(self.__get_score_as_string(Category.CHANCE))
        score_array.append(self.__get_score_as_string(Category.THREE_OF_A_KIND))
        score_array.append(self.__get_score_as_string(Category.FOUR_OF_A_KIND))
        score_array.append(self.__get_score_as_string(Category.FIVE_OF_A_KIND))
        score_array.append(self.__get_score_as_string(Category.SHORT_STRAIGHT))
        score_array.append(self.__get_score_as_string(Category.LONG_STRAIGHT))
        score_array.append(self.__get_score_as_string(Category.FULL_HOUSE))

        if self.__should_add_bonus():
            score_array.append("35")
        else:
            score_array.append("0")

        score_array.append(str(self.get_score()))

        return " ".join(score_array)


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
        cat_array = [Category.ONES,
                     Category.TWOS,
                     Category.THREES,
                     Category.FOURS,
                     Category.FIVES,
                     Category.SIXES,
                     Category.CHANCE,
                     Category.THREE_OF_A_KIND,
                     Category.FOUR_OF_A_KIND]

        ss = ScoreSequence()
        target_rolls = copy.copy(self.rolls)

        # **

        smallest_five_of_a_kind_roll_index, smallest_five_of_a_kind_roll = self.__get_smallest_roll(
            target_rolls,
            Category.FIVE_OF_A_KIND
        )

        if smallest_five_of_a_kind_roll is not None:
            ss.set_category(Category.FIVE_OF_A_KIND, smallest_five_of_a_kind_roll)
            del target_rolls[smallest_five_of_a_kind_roll_index]

        # **

        smallest_full_house_roll_index, smallest_full_house_roll = self.__get_smallest_roll(
            target_rolls,
            Category.FULL_HOUSE
        )

        if smallest_five_of_a_kind_roll is not None:
            ss.set_category(Category.FULL_HOUSE, smallest_full_house_roll)
            del target_rolls[smallest_full_house_roll_index]

        # **

        smallest_long_straight_roll_index, smallest_long_straight_roll = self.__get_smallest_roll(
            target_rolls,
            Category.LONG_STRAIGHT
        )

        if smallest_long_straight_roll is not None:
            ss.set_category(Category.LONG_STRAIGHT, smallest_long_straight_roll)
            del target_rolls[smallest_long_straight_roll_index]

        # **

        smallest_short_straight_roll_index, smallest_short_straight_roll = self.__get_smallest_roll(
            target_rolls,
            Category.SHORT_STRAIGHT
        )

        if smallest_short_straight_roll is not None:
            ss.set_category(Category.SHORT_STRAIGHT, smallest_short_straight_roll)
            del target_rolls[smallest_short_straight_roll_index]

        # **

        sequences = self.__recurse(cat_array, target_rolls, ss)

        for s in sequences:
            yield s

    def __recurse(self, categories, rolls, current_ss):

        if len(categories) == 0:
            yield current_ss.create_copy()
            return

        for roll_index in range(len(rolls)):
            roll = rolls[roll_index]
            current_ss.set_category(categories[0], roll)

            less_rolls1 = rolls[0:roll_index]
            less_rolls2 = rolls[roll_index + 1:]

            less_rolls = less_rolls1 + less_rolls2

            sub_categories = categories[1:]

            recurse_results = self.__recurse(sub_categories, less_rolls, current_ss)

            for ss in recurse_results:
                if ss is not None:
                    yield ss

    def __get_smallest_roll(self, rolls, category):
        smallest_roll = None
        smallest_index = -1
        for roll_index in range(len(rolls)):
            current_five_score = rolls[roll_index].get_score(category)
            if current_five_score > 0:
                if smallest_roll is None:
                    smallest_roll = rolls[roll_index]
                    smallest_index = roll_index
                else:
                    if current_five_score < smallest_roll.get_score(category):
                        smallest_roll = rolls[roll_index]
                        smallest_index = roll_index

        return smallest_index, smallest_roll


class YahtzeeScorer:
    def __init__(self) -> None:
        self.factory = ScoreSequenceFactory()

    def add_roll(self, values: list, name=None):
        self.factory.add_roll(values, name)

    def is_complete(self) -> bool:
        return self.factory.is_complete()

    def get_max_game_score(self, max_count) -> str:

        max_score_sequence = None

        combos = self.factory.get_all_combinations()

        count = 0

        for combo in combos:

            if count == 0:
                max_score_sequence = combo
            else:
                if combo.get_score() > max_score_sequence.get_score():
                    max_score_sequence = combo

            if count > max_count:
                break
            count += 1

        return max_score_sequence.get_formatted_score()
