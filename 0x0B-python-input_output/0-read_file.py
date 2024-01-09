#!/usr/bin/python3
"""

No class created

"""


def read_file(filename=""):
    """

    read_file: reads a text file (UTF8) and prints it to stdout

    """

    with open(filename, encoding="utf-8") as f:
        read_file = f.read().splitlines()

    for line in read_file:
        print(line)
