#!/usr/bin/python3
"""Module for to_json_string function"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)
    Args:
        my_obj: the element to turn
    """
    j_str = json.dumps(my_obj)
    return j_str
