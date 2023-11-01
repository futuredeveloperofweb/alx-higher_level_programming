#!/usr/bin/python3
"""Module for matrix_mul function"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        the multiplication of m_a and m_b
    Raises:
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for raw in m_a:
        if not isinstance(raw, list):
            raise TypeError('m_a must be a list of lists')
    for raw in m_b:
        if not isinstance(raw, list):
            raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise TypeError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise TypeError('m_b can\'t be empty')
    for raw in m_a:
        for e in raw:
            if not isinstance(e, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for raw in m_b:
        for e in raw:
            if not isinstance(e, (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    l_a = len(m_a[0])
    l_b = len(m_b[0])

    for raw in m_a[1:]:
        if len(raw) != l_a:
            raise TypeError('each row of m_a must be of the same size')
    for raw in m_b[1:]:
        if len(raw) != l_b:
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    m_c = [[] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            m_c[i].append(c)
    return (m_c)


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/100-matrix_mul.txt')
