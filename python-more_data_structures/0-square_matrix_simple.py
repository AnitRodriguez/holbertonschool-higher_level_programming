#!/usr/bin/python3def
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) > 0:
        for elements in matrix[:]:
            new_matrix.append(list(map(lambda x: x ** 2, elements)))
    return new_matrix
