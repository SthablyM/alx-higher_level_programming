#!/usr/bin/python3
""""Define the Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent the square class"""
    def __init__(self, size):
        """Initialize the new square"""
        self.size = size
        super().__init__(size, size)
        self.__size = size
