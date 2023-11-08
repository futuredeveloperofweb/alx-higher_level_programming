#!/usr/bin/python3
"""Module for read_file function"""


def read_file(filename=""):
    """reads a file
    Args:
        filename: the file to read
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
