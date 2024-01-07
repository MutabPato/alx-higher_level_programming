#!/usr/bin/python3
"""

prints first name and last name

"""


def text_indentation(text):
    """ no modules

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char

        if char in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
