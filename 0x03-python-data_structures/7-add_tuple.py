#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < 2:
        listT = list(tuple_b)
        while len(listT) <= 2:
            listT.append(0)
        tuple_b = tuple(listT)
    if len(tuple_a) < 2:
        listT = list(tuple_a)
        while len(listT) <= 2:
            listT.append(0)
        tuple_a = tuple(listT)
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
