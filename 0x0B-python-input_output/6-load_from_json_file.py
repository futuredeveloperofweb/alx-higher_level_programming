#!/usr/bin/python3
"""Module for load_from_json_file function"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a  “JSON file”
    Args:
        filename: the file to work with
    """
    with open(filename, 'r', encoding='utf-8') as file:
        j_f_content = file.read()
    obj = json.loads(j_f_content)
    return obj
