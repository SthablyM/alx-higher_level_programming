#!/usr/bin/python3
"""Define the new attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """an't add new attribute if the object can’t have
    new attribute"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
