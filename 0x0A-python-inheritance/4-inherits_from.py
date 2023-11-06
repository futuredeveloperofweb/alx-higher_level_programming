#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """check if the obj is instance of a specific class
    Args:
        obj: the object to check
        a_class: the class to check the obj with
    Returns:
        True if obj is an instance of a_class, False otherwise
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
