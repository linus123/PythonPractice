def balance_money(amounts):
    pennyAmounts = convert_dollars_to_pennies(amounts)

    grandTotal = get_sum(pennyAmounts)

    average = grandTotal // len(pennyAmounts)

    adjustedAmounts = create_list_of_amount(average, len(pennyAmounts))

    runningTotal = average * len(pennyAmounts)

    index = 0;

    while (runningTotal < grandTotal):
        adjustedAmounts[index] += 1;
        runningTotal += 1
        index += 1

    return convert_pennies_to_dollars(adjustedAmounts)


def convert_dollars_to_pennies(amounts):
    final = []

    for amount in amounts:
        final.append(amount * 100)

    return final


def convert_pennies_to_dollars(amounts):
    final = []

    for amount in amounts:
        final.append(amount / 100)

    return final


def get_sum(amounts):
    total = 0

    for amount in amounts:
        total += amount

    return total


def create_list_of_amount(amount, length):
    final = []

    for index in range(0, length):
        final.append(amount)

    return final


#def main():
#    threeNPlus1FromFile("110101.txt")

#if __name__ == '__main__':
#    main()


