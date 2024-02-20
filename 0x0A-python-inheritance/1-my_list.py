#!/usr/bin/python3
"""Define an inherited list"""


class MyList(list):
    """Implements sorted printing for list class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
