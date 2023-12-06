#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        i = [x**2 for x in i]
        new_matrix.append(i)
    return (new_matrix)
