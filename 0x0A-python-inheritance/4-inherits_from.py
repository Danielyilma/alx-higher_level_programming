#!/usr/bin/python3
'''using issubclass builtin method'''


def inherits_from(obj, a_class):
    '''returns boolean'''
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
