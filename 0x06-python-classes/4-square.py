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

    @property
    def size(self):
        """retrieves size
        Returns:
            int: size of square
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """sets size to value
        Arguments:
            value(int): value to set as new size
        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(value)

    def area(self):
        """area of a square is its size squared
        Return:
            current square area
        """
        return (self.__size * self.__size)
