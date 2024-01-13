#!/usr/bin/python3
"""Module for add_attribute function"""


def add_attribute(obj, att, value):
    """adds a new attribute to an object if it’s possible
    Args:
        obj: he object to add
        att: the name of the attribute to add
        value: the value of attribute
    Raises:
        TypeError: if the attribute cannot be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
