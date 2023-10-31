#!/usr/bin/python3
def print_last_digit(number):
    num = int(number)
    r = str(num)[-1]
    print("{0}".format(r), end="")
    return (r)
