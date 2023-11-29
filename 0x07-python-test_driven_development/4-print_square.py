#!/usr/bin/python3
'''printing a square'''


def print_square(size):
    ''' printing square with the given size with # chracter'''

    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            size = int(size)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
