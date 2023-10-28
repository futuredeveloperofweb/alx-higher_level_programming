#!/usr/bin/python3
def matrix_divided(matrix, div):
    for lists in matrix:
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    length = len(matrix[0])
    for raw in matrix[1:]:
        if len(raw) != length:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in range(length):
        raw = []
        for j in range(length):
            j = round(j / div, 2)
            raw.append(j)
        new_matrix.append(raw)
    return new_matrix
