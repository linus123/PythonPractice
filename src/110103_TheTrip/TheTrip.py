import sys


def balance_money(amounts):
    grand_total = get_sum(amounts)

    average = grand_total // len(amounts)

    adjusted_amounts = create_list_of_amount(average, len(amounts))

    running_total = average * len(amounts)

    index = 0

    while running_total < grand_total:
        adjusted_amounts[index] += 1
        running_total += 1
        index += 1

    return adjusted_amounts


def get_minimum_exchange(amounts):
    amounts.sort(reverse=True)
    adjusted_amounts = convert_dollars_to_pennies(amounts)
    balanced_amounts = balance_money(adjusted_amounts)

    index = 0

    amount_to_move = 0

    for balanced_amount in balanced_amounts:
        diff = balanced_amount - adjusted_amounts[index]

        if diff < 0:
            amount_to_move += diff

        index += 1

    return (amount_to_move * -1) / 100


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


def run_from_standard_in():
    amount_count = int(sys.stdin.readline())

    while amount_count != 0:

        counter = 0

        amounts = []

        while counter < amount_count:
            amount = float(sys.stdin.readline())
            amounts.append(amount)
            counter += 1

        exchange_money = get_minimum_exchange(amounts)

        print('${:.2f}'.format(exchange_money))

        amount_count = int(sys.stdin.readline())


def main():
   run_from_standard_in()


if __name__ == '__main__':
   main()

