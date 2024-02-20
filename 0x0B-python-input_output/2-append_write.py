#!/usr/bin/python3
"""Defines file-appending function"""


def append_write(filename="", text=""):
    """Write a function that appends a string at the end of a text file
    Args:
        filename (str): The name of the file to append
        text (str): The string to append
    Return:
        the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
