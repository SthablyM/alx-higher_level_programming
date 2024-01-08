#!/usr/bin/python3
"""Define the inheritance class checking"""


def inherits_from(obj, a_class):
    """check  if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class"""
    if type(obj) != a_class:
        return True
    return False
