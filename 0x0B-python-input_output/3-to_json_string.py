#!/usr/bin/python3
"""

No class created

"""


import json


def to_json_string(my_obj):
    """

    returns the JSON representation of an object (string)

    """

    json_file = json.dumps(my_obj)

    return (json_file)
