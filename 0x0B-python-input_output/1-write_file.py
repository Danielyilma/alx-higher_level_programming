#!/usr/bin/python3
'''writing to a file'''


def write_file(filename="", text=""):
    '''write to a file implementation'''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
