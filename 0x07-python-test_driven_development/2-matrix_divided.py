#!/usr/bin/python3
"""
Module on division  ofa matrix
"""


def matrix_divided(matrix, div):
    """
    Dividing a matrix but after some checks
    """
    if type(matrix) != list or len(matrix) < 1:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix[0]) != list or len(matrix[0]) < 1:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    a = len(matrix[0])
    b = []
    for i in matrix:
        if type(i) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != a:
            raise TypeError("Each row of the matrix must have the same size")
        b1 = []
        for x in i:
            if type(x) != int and type(x) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            b1.append(round(x/div, 2))
        b.append(b1)
    return b
