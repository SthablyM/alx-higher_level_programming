#!/usr/bin/python3
"""Define BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent basegeomentry"""
    def __init__(self, width, height):
        """Intialize a new rectangle"""
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
