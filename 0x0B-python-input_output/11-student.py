#!/usr/bin/python3
"""

No class created

"""


class Student():
    """

    returns the dictionary description with simple data structure

    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is not None:
            return ({
                attr: getattr(
                    self, attr) for attr in attrs if hasattr(self, attr)
                })

        return ({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            })

    def reload_from_json(self, json):

        for key, value in json.items():
            setattr(self, key, value)
