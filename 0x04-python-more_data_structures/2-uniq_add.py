#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique = set()
    sum = 0
    for i in my_list:
        unique.add(i)
    for i in unique:
        sum += i
    return sum
