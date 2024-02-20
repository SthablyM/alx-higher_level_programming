#!/usr/bin/python3
"""Define MyInt that inherits from int """


class MyInt(int):
    """invert int operator == and !="""
    def __eq__(self, value):
        """Override == operator with != behaviour"""
        return self.real != value

    def __ne__(self,value):
        """Override != operator with == behaviour. """
        return self.real == value
