#!/usr/bin/python3
"""Module for Base class"""

from json import loads, dumps
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
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            list_objs is a list of instances who inherits of Base
        """
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open('{}.json'.format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string is a string representing a list of dictionaries
        """
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            cls: the objects name
            **dictionary: as a double pointer to a dictionary
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        from os import path
        file = f'{cls.__name__}.json'
        if not path.isfile(file):
            return []
        with open(file, 'r') as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """a function that serializes in CSV"""
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file_csv(cls):
        """a function that deserializes in CSV"""
        from os import path
        file = f'{cls.__name__}.csv'
        if not path.isfile(file):
            return []
        with open(file, 'r') as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
