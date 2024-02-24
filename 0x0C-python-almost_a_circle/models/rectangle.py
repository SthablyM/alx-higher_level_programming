#!/usr/bin/python3
"""Defines  new class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Representing the new rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the new rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ that returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """ that prints in stdout the Rectangle instance with the #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for j, l in kwargs.items():
                if j == "id":
                    if l is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = l
                elif j == "width":
                    self.width = l
                elif j == "height":
                    self.height = l
                elif j == "x":
                    self.x = l
                elif j == "y":
                    self.x = l

    def __str__(self):
        """Return the print() and str() representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.y, self.x, self.width, self.height)
