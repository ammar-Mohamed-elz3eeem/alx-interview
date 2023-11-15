#!/usr/bin/python3
"""N queens problem algorithm"""
import sys


def isAttacking(columns):
    rowId = len(columns) - 1
    for i in range(0, rowId):
        diff = abs(columns[i] - columns[rowId])
        if diff <= 0 or diff == (rowId - i):
            return False
    return True


def n_queens(n, row, columns, result):
    if row == n:
        print(result)
    else:
        for i in range(0, n):
            columns.append(i)
            result.append([row, i])
            if isAttacking(columns):
                n_queens(n, row + 1, columns, result)
            columns.pop()
            result.pop()


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

n_queens(N, 0, [], [])
