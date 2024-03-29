#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # This script is for computing a matrix total number base when they're all squared.
    new_matrix = matrix.copy()
    for n in range(len(matrix)):
        new_matrix[n] = list(map(lambda x: x**2, matrix[n]))
    return (new_matrix)