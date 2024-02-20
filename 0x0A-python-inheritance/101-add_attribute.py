#!/usr/bin/python3
"""Define the function that add attribute to an object"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object
    Args:
        obj(any): The object to add attribute
        att(str):The string
        value(any): The value of att
    Raises:
        TypeError: if the attribute cannot add"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
