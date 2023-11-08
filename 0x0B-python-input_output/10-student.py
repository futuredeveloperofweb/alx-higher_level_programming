#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """constractor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        d = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                d[k] = v
        return d
