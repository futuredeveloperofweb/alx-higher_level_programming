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

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            'matrix must be a matrix (list of lists) ' + 'of integers/floats')

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                'matrix must be a matrix (list of lists) ' +
                'of integers/floats')

        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) ' +
                    'of integers/floats')

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
