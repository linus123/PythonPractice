class ThrowRoll:
    def __init__(self, dice_values: list) -> None:

        if len(dice_values) != 5:
            raise ValueError("Array must have 5 values")

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
