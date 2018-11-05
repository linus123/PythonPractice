def crypt_decrypt(encrypted_line, word_dictionary):

    encrypted_line = encrypted_line.strip()
    encrypted_words = encrypted_line.split(' ')
    encrypted_words = [word.strip() for word in encrypted_words]

    word_dictionary = [word.strip() for word in word_dictionary]

    if encrypted_line == "":
        return ""

    decode_letters = {}

    for encrypted_word in encrypted_words:
        if encrypted_word in decode_letters:
            f = decode_letters[encrypted_word]
            for dic_work in word_dictionary:
                if len(f) == 0:
                    return get_no_solution(encrypted_words)
        else:
            f = []

            if is_already_mapped(word_dictionary[0], decode_letters):
                return get_no_solution(encrypted_words)

            f.append(word_dictionary[0])
            decode_letters[encrypted_word] = f

    s = ""

    for encrypted_word in encrypted_words:
        s += str(decode_letters[encrypted_word][0]) + " "

    return s.strip()


def get_no_solution(encrypted_words):
    s = ""

    for _ in encrypted_words:
        s += "* "

    return s.strip()


def is_already_mapped(letter, decode_letters):
    for key, letter_array in decode_letters.items():
        if letter in letter_array:
            return True
    return False
