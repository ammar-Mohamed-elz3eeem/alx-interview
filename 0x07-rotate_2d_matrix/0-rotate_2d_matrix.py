#!/usr/bin/env python3

def rotate_2d_matrix(mat):
    if len(mat) == 0:
        return
    for row in range(0, len(mat)):
        for col in range(0, len(mat[row])):
            if col >= row:
                temp = mat[row][col]
                mat[row][col] = mat[col][row]
                mat[col][row] = temp
    return mat


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
