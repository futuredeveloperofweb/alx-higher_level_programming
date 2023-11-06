#!/usr/bin/python3
"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """check if an object is instance of a given class
    Args:
        obj: the object to check
        a_class: the specified class
    Returns:
        True if it is, False otherwise
    """
    if type(obj) is a_class:
        return True
    return False
