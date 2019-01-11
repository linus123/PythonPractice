class CrossResult:
    def __init__(self) -> None:
        self.total_number_of_seconds = 0
        self.crossings = []

    def add_crossing(self, crossing: list):
        self.crossings.append(crossing)


def get_min_time_to_cross(people: list) -> CrossResult:
    if len(people) == 1:
        cr = CrossResult()
        cr.total_number_of_seconds = people[0]
        cr.add_crossing([people[0]])
        return cr

    if people[0] > people[1]:
        cr = CrossResult()
        cr.total_number_of_seconds = people[0]
        cr.add_crossing([people[0], people[1]])
        return cr

    cr = CrossResult()
    cr.total_number_of_seconds = people[1]
    cr.add_crossing([people[0], people[1]])
    return cr