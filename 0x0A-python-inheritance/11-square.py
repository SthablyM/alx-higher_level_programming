#!/usr/bin/python3
"""Define the square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent the square class"""
    def __init__(self, size):
        """Initialize the new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
