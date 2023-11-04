#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            print("{}{}".format(matrix[i][j], " " if j + 1 != len(matrix)
                                else ""), end="")
            j += 1
        print()
