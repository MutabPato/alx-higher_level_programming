#!/usr/bin/python3
"""

No class created

"""


import json


def save_to_json_file(my_obj, filename):
    """

    writes an Object to a text file, using a JSON representation

    """

    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
