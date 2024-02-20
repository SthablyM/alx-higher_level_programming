#!/usr/bin/python3
"""Define a class and inherited"""


def is_kind_of_class(obj, a_class):
    """check if an object is an istance or inherited
    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of the obj
    Return:
        True otherwise False"""

    if isinstance(obj, a_class):
        return True
    return False
