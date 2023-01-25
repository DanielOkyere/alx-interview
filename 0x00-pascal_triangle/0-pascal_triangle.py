#!/usr/bin/env python3
""" Implementation of pascal Challenge"""


def pascal_triangle(n):
    """return list of number"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        n_row = [0] * (i+1)
        n_row[0] = 1
        n_row[len(n_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(n_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                n_row[j] = a + b
        pascal_triangle[i] = n_row

    return pascal_triangle
