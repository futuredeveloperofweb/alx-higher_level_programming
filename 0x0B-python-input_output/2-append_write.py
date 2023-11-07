#!/usr/bin/python3
"""Module for append_write function"""


def append_write(filename="", text=""):
    with open(filename, 'a') as file:
        return file.write(text)
