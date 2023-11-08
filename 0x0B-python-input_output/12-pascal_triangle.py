#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal triangle"""
    if n <= 0:
        return []
    l = [[1]]
    while len(l) != n:
        t = l[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        l.append(tmp)
    return l
