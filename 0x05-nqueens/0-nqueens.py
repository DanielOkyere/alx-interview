#!/usr/bin/python3
"""Nqueens"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    """Solves nqueens"""
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack(s, q):
    """queen under attach"""
    (row1, col1) = s
    (row2, col2) = q
    return (row1 == row2)  or (col1 == col2) or\
            abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    """Safe positions"""
    for queen in queens:
        if attack(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
