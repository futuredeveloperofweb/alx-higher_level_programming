#!/usr/bin/python3
"""Module for from_json_string function"""
import json


def from_json_string(my_str):
    """returns an object  represented by a JSON string
    Args:
        my_str: the string to turn
    """
    return json.loads(my_str)
