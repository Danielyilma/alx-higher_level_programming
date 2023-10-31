#!/usr/bin/python3
def uppercase(str):
    for i, char in enumerate(str):
        if ord(char) >= 97:
            char = chr(ord(char) - 32)
        if i == len(str) - 1:
            print("{0}".format(char))
        else:
            print("{0}".format(char), end="")
