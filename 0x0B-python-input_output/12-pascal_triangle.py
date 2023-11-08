#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal triangle"""
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) != n:
        tel = tri[-1]
        tmp = [1]
        for i in range(len(tel) - 1):
            tmp.append(tel[i] + tel[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
