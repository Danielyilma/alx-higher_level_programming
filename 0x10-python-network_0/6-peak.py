#!/usr/bin/python3
'''finding peak from a list'''

def find_peak(list_of_integers):
    '''the function that finds a peak from a list'''
    max = list_of_integers[0]
    for val in list_of_integers:
        if val > max:
            max = val
    return max
