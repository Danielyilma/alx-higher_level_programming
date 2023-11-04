#!/usr/bin/python3


def no_c(my_string):
    list = ""
    for i in my_string:
        if i not in "cC":
            list += i
    return list
