"""
URL:
https://www.codingame.com/training/medium/sudoku-solver

My Solution:

import sys
import math

# the mat of the sudoku
mat = [list(map(int, input())) for x in range(9)]

def check(row, col, num):

    # check the row and col
    for x in range(9):
        if mat[row][x] == num or mat[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    # check the set
    for i in range(3):
        for j in range(3):
            if mat[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(row, col):
    # If we embedded the whole board:
    if (row == 8 and col == 9):
        return True

    # if we have done whithe the row
    if col == 9:
        row += 1
        col = 0

    if mat[row][col] > 0:
        return Suduko(row, col + 1)

    for num in range(1, 10):
        # Checking whether it is possible to put num there:
        if check(row, col, num):
            mat[row][col] = num
            # Checking if this leads to solution:
            if Suduko(row, col + 1):
                return True
        # Replacement of num with zero because no solution was found with num:
        mat[row][col] = 0
    return False

if (Suduko(0, 0)):
    for i in range(9):
        for j in range(9):
            print(mat[i][j], end="")
        print()

mat.clear()

# I helped with the code: https://www.askpython.com/python/examples/sudoku-solver-in-python

"""
