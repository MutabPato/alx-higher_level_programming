#!/usr/bin/python3
"""

divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """ no modules

    """

    if not isinstance(matrix, list) or not\
            all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [list(
        map(lambda x: round(x / div, 2), row)) for row in matrix]

    return (new_matrix)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
