#!/usr/bin/python3
"""Square module"""


class Square:
    """Define the sqare class"""

    def __init__(self, size=0, position=(0, 0)):
        """Satart a new square

        Args:
            size (int): length of a side in the square
            position (int, int): the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Proprety for the lenght of a side square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """area of the square

        Return:
            the size square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print('')
            return

        [print('') for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            print('')

    def __str__(self):
        """Also print the square"""
        if self.__size != 0:
            [print('') for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            if i != self.__size - 1:
                print('')
        return ('')
