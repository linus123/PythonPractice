def is_jolly_jumper(values):
    if len(values) <= 0:
        raise ValueError("values must have at least one value")

    if len(values) == 1:
        return True

    diff1 = abs(values[0]) - abs(values[1])

    if abs(diff1) == 1:
        return True

    return False
