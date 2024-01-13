#!/usr/bin/python3
"""Module for class_to_json funtion"""


def class_to_json(obj):
    """a function that returns the dictionary description
    Args:
        obj: is an instance of a Class
    """
    return obj.__dict__
