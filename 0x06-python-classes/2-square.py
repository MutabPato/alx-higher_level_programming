#!/usr/bin/python3
"""No module description"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """__init__ method
        Arguments:
            size: size attribute
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)