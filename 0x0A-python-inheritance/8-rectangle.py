#!/usr/bin/python3
"""Module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherite from BaseGeometry class"""

    def __init__(self, width, height):
        """constractore
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
