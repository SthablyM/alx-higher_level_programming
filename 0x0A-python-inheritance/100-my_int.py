#!/usr/bin/python3
"""Define the class MyInt"""


class MyInt(int):
    """Invert operator"""
    def __eq__(self, value):
        """MyInt has == and != operators inverted"""
        return super().__ne__(value)

    def __ne__(self, value):

        return self.real == value
