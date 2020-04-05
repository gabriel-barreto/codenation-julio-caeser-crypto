def find_occurrences(char: str, source: str) -> list:
    found = []
    for i, each in enumerate(source):
        if each == char:
            found.append(i)

    return found


def replace_index(source: str, index: int, new_value: str) -> str:
    if index == 0:
        return new_value + source[1:]
    if index == len(source):
        return source[:-1] + new_value

    if index < 0 or index > len(source):
        raise IndexError('Index not found on source string')

    return source[:index] + new_value + source[(index + 1):]


def decrypt_char(encrypted_char: str, index_diff: int) -> str:
    min_ascii_code = 97 # 97 represents a
    max_ascii_code = 123 # 124 represents next w

    ascii_code = ord(encrypted_char)

    if ascii_code - index_diff >= min_ascii_code:
        return chr(ascii_code - index_diff)
    return chr(max_ascii_code + ((ascii_code - index_diff) - min_ascii_code))


def decrypt(encrypted_phrase: str, index_diff: int) -> str:
    """
    Decrypt a phrase encrypted using Julius Caesar crypto

    :param encrypted_phrase: Phrase you want to decrypt
    :param index_diff: Number of index change
    :return: A decrypted phrase
    """
    phrase_chars = filter(
        lambda each: each.isalpha() and not each.isdigit(),
        encrypted_phrase,
    )

    decrypted_chars = {
        each: {
            "indexes": find_occurrences(each, encrypted_phrase),
            "decrypted_value": decrypt_char(each, index_diff)
        }
        for each in phrase_chars
    }

    decrypted_phrase = encrypted_phrase
    for each in decrypted_chars.values():
        for i in each['indexes']:
            decrypted_phrase = replace_index(
                decrypted_phrase,
                i,
                each['decrypted_value']
            )

    return decrypted_phrase
