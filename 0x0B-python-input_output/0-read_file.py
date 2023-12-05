#!/usr/bin/python3
'''reading from a file'''


def read_file(filename=""):
    '''reading from a file implementation'''
    with open(filename, "r", encoding="UTF-8") as f:
        line = f.readline()
        while line:
            print(line, end="")
            line = f.readline()
