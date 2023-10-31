#!/usr/bin/python3
num = 97
while num < 123:
    if chr(num) != "q" and chr(num) != "e":
        print(f"{num:c}", end="")
    num += 1
