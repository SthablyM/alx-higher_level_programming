#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing a new rectangle.
        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += '#' * self.__width
                if i < self.__height - 1:
                    rectangle_str += '\n'
            return rectangle_str

    def __repr__(self):
        rectangle_str = "Rectangle(" + str(self.__width)
        rectangle_str += ", " + str(self.__height) + ")"
        return (rectangle_str)

    def __del__(self):
        print("Bye rectangle...")
