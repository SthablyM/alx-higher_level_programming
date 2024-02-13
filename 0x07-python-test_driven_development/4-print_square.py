#!/usr/bin/python3
"""Defines a square-printing"""


def print_square(size):
    """print a square with #
    Args:
        size (int): The height/width of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is < 0"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
