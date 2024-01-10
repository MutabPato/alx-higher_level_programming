#!/usr/bin/python3
"""

No class created

"""

json = __import__('json')


def class_to_json(obj):
    """

    returns the dictionary description with simple data structure

    """

    json_obj = json.dumps(obj.__dict__)

    return (json_obj)
