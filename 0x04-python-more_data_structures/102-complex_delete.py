#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    list1 = list(a_dictionary.keys())
    for i in list1:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
