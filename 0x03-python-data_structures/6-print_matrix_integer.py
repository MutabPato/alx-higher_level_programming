#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub in matrix:
        for index, elem in enumerate(sub):
            print("{}".format(elem), end="")
            if index < len(sub) - 1:
                print(" ", end="")
        print()
