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
        """
        Initializes square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get size
        """

        return (self._Rectangle__width)

    @size.setter
    def size(self, value):
        """
        Set size
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def area(self):
        """
        Return: area
        """

        return (self.width * self.height)

    def display(self):
        """
        Displays square
        """

        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """"
        Return: string representation of a square
        """

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """
        Updates square class arguments
        """

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
        """
        Returns: dictionary representation of a square
        """

        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
