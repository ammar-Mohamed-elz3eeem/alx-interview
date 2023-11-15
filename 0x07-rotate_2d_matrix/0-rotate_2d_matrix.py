#!/usr/bin/python3
"""Rotate 2D matrix algorithm"""


def rotate_2d_matrix(mat):
    """This function will rotate 2D matrix"""
    for row in range(0, len(mat)):
        for col in range(len(mat[row]) - 1, 0, -1):
            if col >= row:
                temp = mat[row][col]
                mat[row][col] = mat[col][row]
                mat[col][row] = temp
        mat[row].reverse()
    return mat
