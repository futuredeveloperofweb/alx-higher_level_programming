#!/usr/bin/python3
"""Module for save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        mu_obj: the object to turn
        filename: the file to write in
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
