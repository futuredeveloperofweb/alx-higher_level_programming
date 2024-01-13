#!/usr/bin/python3
"""Module for lazy_matrix_mul function"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy
    Args:
        m_a: a list of lists
        m_a: a list of lists
    Returns:
        the muliplication of m_a and m_b
    """
    return numpy.matmul(m_a, m_b)
