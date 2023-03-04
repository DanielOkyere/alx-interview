#!/usr/bin/python3
"""Program to solve N-queen problem"""
import sys
from typing import List, Tuple


def solveNQueens(n: int) -> List[List[int]]:
    """Solves N-Queen Problem using backtrack method
    Args:
        n: int - size of the board
    Returns:
        position in a list
    """
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [[0] * n for i in range(n)]

    def backtrack(r: int):
        """Helper to solve recursively"""
        row_index = 0
        if r == n:
            copy = [row * 1  for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = 1
            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = 0
    backtrack(0)
    return res


if __name__ == '__main__':
    import sys

    n = 0

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N muste be at least 4')
        sys.exit(1)

    print(solveNQueens(n))
