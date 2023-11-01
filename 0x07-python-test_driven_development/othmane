#!/usr/bin/python3
"""Module for matrix_division function"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix.

    Args:
        matrix: a list of lists
        div: the integer to devide withi
    Returns:
        a new matrix where all the elements are divided by div
    Raises:
        TypeError: If matrix is not list of lists containing int or float
        TypeError: If sublists are not all same size
        TypeError: If div is not int or float
        ZeroDivisionError: If div is zero
    """

    for lists in matrix:
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError
            ('matrix must be a matrix (list of lists) of integers/floats')
    length = len(matrix[0])
    for raw in matrix[1:]:
        if len(raw) != length:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for raw in matrix:
        new_raw = []
        for e in raw:
            e = round(e/div, 2)
            new_raw.append(e)
        new_matrix.append(new_raw)
    return new_matrix


if __name__ == '__main__':
    import doctest
    dectest.testfile('tests/2-matrix_divided.txt')
