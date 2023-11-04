#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            print("{:d}".format(matrix[i][j]), end="")
            if j + 1 != len(matrix[i]):
                print(" ", end="")
            j += 1
        print()
        i += 1
