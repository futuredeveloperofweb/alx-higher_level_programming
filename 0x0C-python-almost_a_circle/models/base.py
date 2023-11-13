#!/usr/bin/python3
"""Module for Base class"""

import json

class Base:
    """defining the class Base
    Args:
        nb_object: a private class attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """constractore
        Args:
            id: the id instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries: is a list of dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            list_objs: is a list of instances who inherits of Base
        """
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        classname = cls.__name__
        filename = f'{classname}.json'
