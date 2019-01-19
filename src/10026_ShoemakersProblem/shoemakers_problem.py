import copy
import sys


class ShoeJob:
    def __repr__(self) -> str:
        return "time: %i fine: %i order %i" % (self.time, self.fine, self.order)

    def __init__(self, time: int, fine: int) -> None:
        self.time = time
        self.fine = fine
        self.order = 0
        self.sort_order = fine / time


def get_sort_order(j: ShoeJob):
    return j.sort_order


def get_cost(jobs: list):

    copy_jobs = copy.copy(jobs)

    cost = 0
    day_counter = 0

    working_job = copy_jobs[0]
    del copy_jobs[0]

    current_job_day_count = 0

    while len(copy_jobs) > 0 and day_counter < 1000:

        if current_job_day_count >= working_job.time:
            working_job = copy_jobs[0]
            del copy_jobs[0]
            current_job_day_count = 1
        else:
            current_job_day_count += 1

        for fine_job in copy_jobs:
            cost += fine_job.fine

        day_counter += 1

    return cost


def get_best_order(jobs: list):

    for index, job in enumerate(jobs):
        job.order = index + 1

    jobs.sort(key=get_sort_order, reverse=True)

    result = []

    for index, job in enumerate(jobs):
        result.append(job.order)

    return result

def run_from_standard_in():

    first_line = sys.stdin.readline()
    number_of_test_cases = int(first_line.strip())
    blank_line = sys.stdin.readline()

    for test_case_counter in range(number_of_test_cases):

        current_line = sys.stdin.readline().strip()
        job_count = int(current_line)

        jobs = []

        for jc in range(job_count):
            current_line = sys.stdin.readline().strip()
            line_split = current_line.split(" ")
            jobs.append(ShoeJob(int(line_split[0]), int(line_split[1])))

        order_result = get_best_order(jobs)

        print(" ".join([str(o) for o in order_result]))

        if test_case_counter < number_of_test_cases:
            blank_line = sys.stdin.readline()

        if test_case_counter < number_of_test_cases - 1:
            print("")


def main():
    run_from_standard_in()


if __name__ == '__main__':
    main()