#!/usr/bin/python3
"""

No class created

"""


def append_write(filename="", text=""):
    """

    append_write: appends a string at the end of a text file (UTF8)

    """

    with open(filename, 'a', encoding="utf-8") as f:
        nb_char = f.write(text)

    return (nb_char)
