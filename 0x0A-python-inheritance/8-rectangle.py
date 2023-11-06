#!/usr/bin/python3
"""Module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherite from BaseGeometry class"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('hight', height)
        self.__width = width
        self.__height = height
