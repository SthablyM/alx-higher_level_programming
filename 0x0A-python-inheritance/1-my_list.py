#!/usr/bin/python3
"""Define the inharitance from list"""


class MyList(list):
    """Impliment the sorted printing"""
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
