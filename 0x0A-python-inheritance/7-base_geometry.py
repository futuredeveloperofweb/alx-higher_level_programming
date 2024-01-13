#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """a function that raise an exeption
        Raises:
            Exception: raise an error
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """a function that validate the arg value
        Args:
            name: the name
            value: the value
        Raises:
            TypeError: if value is not of type int
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
