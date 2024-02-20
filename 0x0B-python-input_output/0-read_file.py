#!/usr/bin/python3
"""Defines a text file"""


def read_file(filename=""):
    """print the contents of a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
