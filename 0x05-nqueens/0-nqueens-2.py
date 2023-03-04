#!/usr/bin/python3
"""Program to solve N-queen problem"""
import sys


def is_valid(board, row, col, n):
    """Checks for valid position"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve(board, row, n):
    """Solves for the board"""
    if row == n:
        print('{%s}' % ','.join(str(col+1) for col in board))
        return
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col
            solve(board, row+1, n)


def main():
    """Main Function"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    board = [-1] * n
    solve(board, 0, n)


if __name__ == '__main__':
    main()
