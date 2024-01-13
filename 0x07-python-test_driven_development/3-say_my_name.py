#!/usr/bin/python3
"""Module for say_my_name funcion"""


def say_my_name(first_name, last_name=""):
    """a function that prints a name

    Args:
        first_name (str): the first argument
        last_name (str): the second argument

    Raises:
        TypeError: if first_name or last_name arguments are not of type str
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
