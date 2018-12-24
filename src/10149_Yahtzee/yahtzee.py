class ThrowRoll:
    def __init__(self, dice_values: list) -> None:

        if len(dice_values) != 5:
            raise ValueError("Array must have 5 values")

        dice_values.sort()

        self.dice_values = dice_values

        self.value_dic = self.create_value_dic(dice_values)

    def create_value_dic(self, dice_values):
        value_dic = {}
        for dic_value in dice_values:
            if dic_value in value_dic:
                value_dic[dic_value] += 1
            else:
                value_dic[dic_value] = 1
        return value_dic

    def is_full_house(self) -> bool:
        has_two_count = False
        has_three_count = False

        for key, value in self.value_dic.items():
            if value == 2:
                has_two_count = True

            if value == 3:
                has_three_count = True

        return has_two_count and has_three_count

    def is_long_straight(self) -> bool:
        index = 1

        while index < 5:

            if self.dice_values[index] - (self.dice_values[0] + index) != 0:
                return False

            index += 1

        return True

    def is_short_straight(self) -> bool:
        if 1 in self.value_dic \
                and 2 in self.value_dic \
                and 3 in self.value_dic \
                and 4 in self.value_dic:
            return True

        if 2 in self.value_dic \
                and 3 in self.value_dic \
                and 4 in self.value_dic \
                and 5 in self.value_dic:
            return True

        return False
