#!/usr/bin/python3
"""

No class created

"""


def write_file(filename="", text=""):
    """

    write_file: writes a string to a text file (UTF8) and
    returns the number of characters written

    """

    with open(filename, 'w', encoding="utf-8") as f:
        nb_char = f.write(text)

    return (nb_char)
