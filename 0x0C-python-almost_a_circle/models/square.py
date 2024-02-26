#!/usr/bin/python3
"""Defines class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing the Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, l in kwargs.items():
                if j == "id":
                    if l is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = l
                elif j == "size":
                    self.size = l
                elif j == "x":
                    self.x = l
                elif j == "y":
                    self.y = l

    def to_dictionary(self):
        """that returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y

        }

    def __str__(self):
        """Return the print() and str() representation of the square"""
        return "[Rectangle] ({}) {}/{} - {}".format(
                self.id, self.y, self.x, self.width)
