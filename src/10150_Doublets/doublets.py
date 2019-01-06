def has_more_than_one_difference(word1: str, word2: str):
    if abs(len(word1) - len(word2)) > 1:
        return True

    diff_count = 0

    for letter_index in range(len(word1)):
        if word1[letter_index] != word2[letter_index]:
            diff_count += 1
            if diff_count > 1:
                return True

    return False

