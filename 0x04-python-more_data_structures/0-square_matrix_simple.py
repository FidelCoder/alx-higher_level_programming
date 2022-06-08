#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for row in matrix:
        c = list(map(lambda x: x**2, row))
        matrix2.append(c)
    return matrix2
