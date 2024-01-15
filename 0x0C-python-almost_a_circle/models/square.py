#!/usr/bin/python3
"""
Third class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self._Rectangle__width)

    @size.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
    """
    @property
    def x(self):
        return (self.x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @property
    def y(self):
        return (self.y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.y = value
    """
    def area(self):
        return (self.width * self.height)

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value

            if key == "size":
                self.size = value

            if key == "x":
                self.x = value

            if key == "y":
                self.y = value

    def to_dictionary(self):
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.x})
