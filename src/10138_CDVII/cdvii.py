import sys


class HighwayRecord:
    def __init__(self, record_text: str) -> None:
        split_text = record_text.split(" ")
        self.license_number = split_text[0]

        if split_text[2] == "enter":
            self.is_exit = False
            self.is_enter = True
        else:
            self.is_exit = True
            self.is_enter = False

        self.ramp_number = int(split_text[3])

        time_split = split_text[1].split(":")

        self.minute_count = int(time_split[1]) * 60 * 60 \
            + int(time_split[2]) * 60 \
            + int(time_split[3])

        self.hour = int(time_split[2])


class BillRecord:
    def __init__(self, license_number: str) -> None:
        self.license_number = license_number
        self.__trips = []

    def add_trip(self, amount: int):
        self.__trips.append(amount)

    def get_bill_amount(self):
        amount = 0

        for trip in self.__trips:
            amount += trip + 100

        return amount + 200


def get_sort_order(hr: HighwayRecord):
    return hr.license_number, hr.minute_count


def get_all_billing_records(
        tolls: list,
        highway_records: list
) -> list:
    highway_records.sort(key=get_sort_order)

    bills = []

    current_bill = BillRecord(highway_records[0].license_number)

    current_index = 0

    while True:
        if current_index + 1 >= len(highway_records):
            break

        enter_record = highway_records[current_index]

        if not enter_record.is_enter:
            current_index += 1
            continue

        exit_record = highway_records[current_index + 1]

        if not exit_record.is_exit:
            current_index += 1
            continue

        if enter_record.license_number != exit_record.license_number:
            current_index += 1
            continue

        if enter_record.license_number != current_bill.license_number:
            current_bill = BillRecord(enter_record.license_number)

        distance = abs(exit_record.ramp_number - enter_record.ramp_number)

        toll = tolls[enter_record.hour]

        current_bill.add_trip(distance * toll)

        if len(bills) == 0:
            bills.append(current_bill)

        if bills[-1].license_number != current_bill.license_number:
            bills.append(current_bill)

        current_index += 2

    return bills


def run_from_standard_in():

    first_line = sys.stdin.readline()
    number_of_test_cases = int(first_line.strip())
    blank_line = sys.stdin.readline()

    for test_case_counter in range(number_of_test_cases):

        current_line = sys.stdin.readline().strip()
        string_toll = current_line.split(" ")
        tolls = [int(t) for t in string_toll]

        current_line = sys.stdin.readline().strip()

        highway_records = []

        while current_line != "":
            highway_records.append(HighwayRecord(current_line))
            current_line = sys.stdin.readline().strip()

        results = get_all_billing_records(tolls, highway_records)

        for r in results:
            print("%s %s" % (r.license_number, '${:.2f}'.format(r.get_bill_amount() / 100)))

        if test_case_counter < number_of_test_cases - 1:
            print("")


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()