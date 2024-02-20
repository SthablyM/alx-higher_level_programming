#!/usr/bin/python3
"""Define an inherited class"""


def inherits_from(obj, a_class):
    """check if an object is an istance or inherited
    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of the obj
    Return:
        True otherwise False"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
