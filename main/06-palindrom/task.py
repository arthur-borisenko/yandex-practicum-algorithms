import re


def remove_all_except_letters_and_digits(string: str):
    """
    cpu - O(n)
    ram - O(n)
    :param string: string to parsse
    :return: string with only letters and digits
    """
    return "".join(map(lambda x: x if x.isalnum() else "", string))


def is_palindrome(phrase: str, ignore_case=True, only_letters_digits=True):
    """check if string is palindrome
    CPU - O(n)
    RAM - O(n)
    :param only_letters_digits:
    :param phrase: phrase to check
    :param ignore_case: if true(default) - ignore case
    :param only_letters_digits: if true(default) - only letters and digits are checked
    :return: True if string is palindrome
    """
    phrase = phrase.lower() if ignore_case else phrase
    phrase = (
        remove_all_except_letters_and_digits(phrase) if only_letters_digits else phrase
    )
    reversed_phrase = phrase[::-1]
    return phrase == reversed_phrase


def main():
    """
    CPU - O(n)
    RAM - o(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        phrase = inp.readline()
        print(is_palindrome(phrase), file=outp)


if __name__ == "__main__":
    main()
