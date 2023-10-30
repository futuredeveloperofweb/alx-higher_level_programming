#!/usr/bin/python3
"""Module for width and heigth attributes"""


class Rectangle:
    """defines two attributes"""
    def __init__(self, width=0, height=0):
        """arguments of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def heigth(self):
        """getter for the private instance height"""
        return self.__height

    @heigth.setter
    def heigth(self, value):
        """setter for the private instance height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
