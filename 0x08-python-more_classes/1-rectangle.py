#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represent a rectange."""

    def __init__(self, width=0, height=0):
        """Initailize a new Rectangle.

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
