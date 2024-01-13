#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda array: list(map(lambda i: i ** 2, array)), matrix))
