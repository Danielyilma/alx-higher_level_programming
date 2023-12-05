#!/usr/bin/python3


def append_write(filename="", text=""):
    '''appending to a file'''
    with open(filename, "a", encoding="utf-8") as f:
        print(len(text))
        return f.write(text)
