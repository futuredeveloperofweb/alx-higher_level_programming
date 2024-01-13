#!/usr/bin/python3
"""Define the MagicClass"""

import math


class MagicClass:
    """Define the circle"""

    def __int__(self, radius=0):
        """Constractor
        Args:
            radius (float or int): the raduis of MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference"""
        return (2 * math.pi * self.__radius)
