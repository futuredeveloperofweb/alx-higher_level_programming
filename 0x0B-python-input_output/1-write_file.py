#!/usr/bin/python3
"""Module for write_file"""


def write_file(filename="", text=""):
    """returns the number of characters written
    Args:
        filename: the to write to
        text: the text to write
    """
    with open(filename, 'w') as file:
        return file.write(text)
