#!/usr/bin/python3
"""Define a class-checking function"""


def is_same_class(obj, a_class):
    """check if an object is exatly an istance
    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of the obj
    Return:
        True otherwise False"""

    if type(obj) == a_class:
        return True
    return False
