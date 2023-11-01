#!/usr/bin/python3
""" Module for the print_square function"""


def print_square(size):
    """ a function that prints a square with the character #

    Args:
        size (int): the size of the square

    Returns:
        a square with # letter of size 'size'

    Raises:
        TypeError: if size is not integer
        ValueError: if size is null
        TypeError: if size float and less then zero
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size < 0 and isinstance(size, float):
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
