#!/usr/bin/python3
"""Module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass representation for Square class"""
    def __init__(self, size):
        """constractor
        Args:
            size: the size of the square
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2
