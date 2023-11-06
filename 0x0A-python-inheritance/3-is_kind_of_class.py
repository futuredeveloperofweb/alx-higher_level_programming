#!/usr/bin/python3
"""Module for is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """check if the obj is an instance of a given class
    Args:
        obj: the object to check
        a_class: the class to check with
    Returns:
        True if obj is instance of the a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
