#!/usr/bin/python3
"""
solves the Nqueens problem
"""
import sys

def isSafe(board, row, col, N):
    """ function isSafe """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col, N):
    """ function solveNQUtil """
    if col == N:
        print([[i, board[i].index(1)] for i in range(N)])
        return True
    res = False
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1, N) or res
            board[i][col] = 0
    return res

def solveNQ(N):
    """ function solveNQ """
    board = [[0 for x in range(N)] for y in range(N)]
    if solveNQUtil(board, 0, N) == False:
        print("No solution exists")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQ(N)
