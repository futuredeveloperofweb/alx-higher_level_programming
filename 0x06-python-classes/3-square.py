#!/usr/bin/python3
"""Square module"""


class Square:
    """Define the sqare class"""

    def __init__(self, size=0):
        """constaractor

        Args:
            size: length of a side in the square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the square

        Returns:
            The size squared
        """
        return self.__size ** 2
