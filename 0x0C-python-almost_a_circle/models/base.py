#!/usr/bin/python3
"""
first class
"""


import json


class Base():
    """
    base of all classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises Base
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns: JSON string representation of list_dictionaries
        """

        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """

        if list_objs is None:
            list_objs = []

        class_name = cls.__name__

        filename = f"{class_name}.json"

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)
