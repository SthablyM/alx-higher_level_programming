#!/usr/bin/python3
"""Define the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """check if object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    return False
