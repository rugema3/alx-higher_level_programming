#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Square each element of the matrix using nested list expressions
    squared_matrix = [[element**2 for element in row] for row in matrix]
    return squared_matrix
