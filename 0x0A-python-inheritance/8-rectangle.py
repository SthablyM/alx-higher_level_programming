#!/usr/bin/python3
"""Define  class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent rectangle"""

    def __init__(self, width, height):
        """Initialize a new rectangle
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
