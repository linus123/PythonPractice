def has_more_than_one_difference(word1: str, word2: str):
    if abs(len(word1) - len(word2)) > 1:
        return True

    diff_count = 0

    longer_len = len(word1)

    if len(word2) > longer_len:
        longer_len = len(word2)

    letter_index = 0
    word1_index = 0
    word2_index = 0

    while letter_index < longer_len:

        if word1_index >= len(word1):
            diff_count += 1
            if diff_count > 1:
                return True

        elif word2_index >= len(word2):
            diff_count += 1
            if diff_count > 1:
                return True

        elif word1[word1_index] != word2[word2_index]:
            diff_count += 1
            if diff_count > 1:
                return True

            if word1_index + 1 < len(word1)\
                    and word1[word1_index + 1] == word2[word2_index]:

                word2_index -= 1

                if len(word1) == len(word2):
                    longer_len += 1

            if word2_index + 1 < len(word2)\
                    and word1[word1_index] == word2[word2_index + 1]:

                word1_index -= 1

                if len(word1) == len(word2):
                    longer_len += 1

        word1_index += 1
        word2_index += 1
        letter_index += 1

    return False

