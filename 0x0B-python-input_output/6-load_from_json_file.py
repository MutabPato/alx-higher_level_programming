#!/usr/bin/python3
"""

No class created

"""


import json


def load_from_json_file(filename):
    """

    creates an Object from a “JSON file”

    """

    with open(filename, 'r') as json_file:
        my_obj = json.load(json_file)

    return (my_obj)
