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
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)