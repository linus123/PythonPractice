import copy
from enum import Enum
from queue import Queue


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
        return "%s - %s - Three of a K: %i Four of K: %i" % (self.name, str(self.dice_values), self.get_score(Category.THREE_OF_A_KIND), self.get_score(Category.FOUR_OF_A_KIND))

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

        has_four_of_a_kind = self.__get_x_of_a_kind(4)
        has_three_of_a_kind = self.__get_x_of_a_kind(3)

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

        if has_four_of_a_kind:
            score_dic[Category.FOUR_OF_A_KIND] = chance_sum
        else:
            score_dic[Category.FOUR_OF_A_KIND] = 0

        if has_three_of_a_kind:
            score_dic[Category.THREE_OF_A_KIND] = chance_sum
        else:
            score_dic[Category.THREE_OF_A_KIND] = 0

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

    def __get_x_of_a_kind(self, x: int) -> bool:
        for key, value in self.count_dic.items():
            if value >= x:
                return True

        return False

    # **

    def get_score(self, cat: Category) -> int:
        return self.score_dic[cat]

    def get_unique_number(self):
        return self.dice_values[0] \
            + self.dice_values[1] * 10 \
            + self.dice_values[2] * 100 \
            + self.dice_values[3] * 1000 \
            + self.dice_values[4] * 10000


class ScoreSequence:

    def __init__(self):
        self.__sequence_dic = {}

    def set_would_duplicate(self, roll: ThrowRoll) -> bool:
        for key, item in self.__sequence_dic.items():
            if item == roll:
                return True

        return False

    def set_category(self, cat: Category, roll: ThrowRoll):
        if self.set_would_duplicate(roll):
            raise ValueError("set_category would duplicate")

        self.__sequence_dic[cat] = roll

    def print_state(self):
        pass
        # print("***")
        # for cat in Category:
        #     if cat in self.__sequence_dic:
        #         print("%s || %r" % (cat, self.__sequence_dic[cat]))
        #     else:
        #         print("%s || None" % cat)

    def create_copy(self):
        ss = ScoreSequence()
        ss.__sequence_dic = copy.copy(self.__sequence_dic)
        return ss

    def get_total_score(self) -> int:
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
            if c in self.__sequence_dic:
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

        score_array.append(str(self.get_total_score()))

        return " ".join(score_array)


class ScoreSequenceFactory:
    def __init__(self) -> None:
        self.__rolls = []

    def add_roll(self, values: list, name: str):
        roll = ThrowRoll(values)
        if name is not None:
            roll.name = name
        self.__rolls.append(roll)

    def is_complete(self) -> bool:
        return len(self.__rolls) >= 13

    def __get_index_of_first_long_straight(self, rolls):

        for roll_index in range(len(rolls)):
            roll = rolls[roll_index]
            if roll.get_score(Category.LONG_STRAIGHT) > 0:
                return roll_index

        return -1

    def get_all_combinations(self):

        valid_cat_seq_dic = {}
        current_rolls = copy.copy(self.__rolls)

        ls_index = self.__get_index_of_first_long_straight(current_rolls)

        if ls_index >= 0:
            valid_cat_seq_dic[Category.LONG_STRAIGHT] = [current_rolls[ls_index]]
            del current_rolls[ls_index]

        categories_by_volatility = [Category.FIVE_OF_A_KIND,
                      Category.FULL_HOUSE,
                      Category.LONG_STRAIGHT,
                      Category.SHORT_STRAIGHT,
                      Category.FIVE_OF_A_KIND,
                      Category.FOUR_OF_A_KIND,
                      Category.THREE_OF_A_KIND,
                      Category.SIXES,
                      Category.FIVES,
                      Category.FOURS,
                      Category.THREES,
                      Category.TWOS,
                      Category.ONES,
                      Category.CHANCE
                      ]

        for cat in categories_by_volatility:
            if cat == Category.LONG_STRAIGHT:
                continue

            valid_cat_seq_dic[cat] = []

            for roll in current_rolls:

                if roll.get_score(cat) > 0:
                    valid_cat_seq_dic[cat].append(roll)

        valid_cat_seq_dic[Category.FULL_HOUSE].sort(key=lambda r: r.get_score(Category.CHANCE))
        valid_cat_seq_dic[Category.SHORT_STRAIGHT].sort(key=lambda r: r.get_score(Category.CHANCE))
        valid_cat_seq_dic[Category.FIVE_OF_A_KIND].sort(key=lambda r: r.get_score(Category.CHANCE))
        valid_cat_seq_dic[Category.FOUR_OF_A_KIND].sort(key=lambda r: r.get_score(Category.CHANCE))
        valid_cat_seq_dic[Category.THREE_OF_A_KIND].sort(key=lambda r: r.get_score(Category.CHANCE))

        valid_cat_seq_dic[Category.CHANCE].sort(key=lambda r: r.get_score(Category.CHANCE))

        valid_cat_seq_dic[Category.ONES].sort(key=lambda r: r.get_score(Category.ONES), reverse=True)
        valid_cat_seq_dic[Category.TWOS].sort(key=lambda r: r.get_score(Category.TWOS), reverse=True)
        valid_cat_seq_dic[Category.THREES].sort(key=lambda r: r.get_score(Category.THREES), reverse=True)
        valid_cat_seq_dic[Category.FOURS].sort(key=lambda r: r.get_score(Category.FOURS), reverse=True)
        valid_cat_seq_dic[Category.FIVES].sort(key=lambda r: r.get_score(Category.FIVES), reverse=True)
        valid_cat_seq_dic[Category.SIXES].sort(key=lambda r: r.get_score(Category.SIXES), reverse=True)

        ss = ScoreSequence()

        sequences = self.recurse(categories_by_volatility, valid_cat_seq_dic, ss)

        for s in sequences:
            yield s

    @staticmethod
    def recurse(categories_by_volatility, valid_cat_seq_dic, current_ss):

        if len(categories_by_volatility) <= 0:
            yield current_ss
            return

        cat = categories_by_volatility[0]
        if len(valid_cat_seq_dic[cat]) > 0:
            for roll in valid_cat_seq_dic[cat]:
                if not current_ss.set_would_duplicate(roll):
                    current_ss.set_category(cat, roll)
                    current_ss.print_state()
                    sequences = ScoreSequenceFactory.recurse(categories_by_volatility[1:], valid_cat_seq_dic, current_ss.create_copy())

                    for s in sequences:
                            yield s
        else:
            sequences = ScoreSequenceFactory.recurse(categories_by_volatility[1:], valid_cat_seq_dic, current_ss.create_copy())

            for s in sequences:
                yield s


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
                if combo.get_total_score() > max_score_sequence.get_total_score():
                    max_score_sequence = combo

            if count > max_count:
                break
            count += 1

        # print("Number of combos %i" % count)

        return max_score_sequence.get_formatted_score()
