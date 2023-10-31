#!/usr/bin/python3
num = 97
while num < 123:
    if chr(num) != "q" and chr(num) != "e":
        print("{0:c}".format(num), end="")
    num += 1
