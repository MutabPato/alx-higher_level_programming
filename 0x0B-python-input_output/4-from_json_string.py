#!/usr/bin/python3
"""

No class created

"""


import json


def from_json_string(my_str):
    """

    returns an object (Python data structure) represented by a JSON string

    """

    my_obj = json.loads(my_str)

    return (my_obj)
