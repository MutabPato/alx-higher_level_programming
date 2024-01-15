#!/usr/bin/python3
"""
second class
"""

from models.base import Base


class Rectangle(Base):
    """
    inherits base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle.
        """

        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle.
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle.
        """

        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.
        """

        return (self.__width * self.__height)

    def display(self):
        """
        Displays the rectangle by printing its representation.
        """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """

        return (f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle
        using positional and keyword arguments.
        """

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value

            if key == "width":
                self.__width = value

            if key == "height":
                self.__height = value

            if key == "x":
                self.__x = value

            if key == "y":
                self.__y = value

    def to_dictionary(self):
        """
        Converts the rectangle's attributes to a dictionary.
        """

        return({'x': self.__x, 'y': self.__y,
                'height': self.__height, 'width': self.__width})
