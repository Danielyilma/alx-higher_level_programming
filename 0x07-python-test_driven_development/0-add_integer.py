#!/usr/bin/python3

'''
implementing integer addition that accepts
two integer and adds them
if the arguments are not integer and \
float it raises Typeerror
'''


def add_integer(a, b=98):
    '''
      integer addition
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
