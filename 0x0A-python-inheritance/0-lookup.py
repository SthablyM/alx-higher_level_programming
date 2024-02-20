#!/usr/bin/python3
"""Define  the attributes functions"""


def lookup(obj):
    """Returns  the list of available attributes and methods of an obje"""
    return [attr for attr in dir(obj)]
