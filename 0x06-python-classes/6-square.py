#!/usr/bin/python3
"""No module description"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method
        Arguments:
            size: size attribute
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        elif type(position) is not tuple or len(position) != 2 or\
             type(position[0]) is not int or type(position[1]) is not int or\
                position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__size = int(size)
            self.__position = position

    @property
    def size(self):
        """retrieves size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """sets size to value
        Arguments:
            value: value to be set
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

    def my_print(self):
        """prints a square"""
        x, y = self.__position
        if self.__size == 0:
            print()
        else:
            for num in range(y):
                print()
            for i in range(self.__size):
                for num in range(x):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """retrieves position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets position
        Arguments:
            value: value to be set
        """
        if type(value) is not tuple or len(value) != 2 or\
            type(value[0]) is not int or type(value[1]) is not int or\
                value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
