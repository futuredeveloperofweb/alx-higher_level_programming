#!/usr/bin/python3
"""Square module"""


class Square:
    """define the sqare class"""

    def __init__(self, size=0):
        """constaractor

        Args:
            size: length of a side in the square
        """
        self.__size = size

    @property
    def size(self):
        """Proprety for the lenght of a side square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area of the square

        Return:
            the size square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end='')
                print()
