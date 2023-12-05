#!/usr/bin/python3
'''reading from a file'''


def read_file(filename=""):
    '''reading from a file implementation'''
    with open(filename, encoding="utf-8") as f:

        for line in f:
            print(line, end="")
        print()
