#!/usr/bin/python3
"""
Pascals Triangle 2 alternative
"""


def pascal_triangle(n):
    """
    Returns with a list of rows for the pascal triangle
    """
    if n <= 0:
        return []

    a = [[1]]
    for i in range(n-1):
        temp = [0] + a[-1] + [0]
        row = []
        for j in range(len(a[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        a.append(row)
    return a
