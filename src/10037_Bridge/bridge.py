def get_min_time_to_cross(people: list):
    if len(people) == 1:
        return people[0]

    if people[0] > people[1]:
        return people[0]

    return people[1]