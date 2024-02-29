#!/usr/bin/python3
'''finding peak from a list'''


def find_peak(list_of_integers):
    '''the function that finds a peak from a list'''
    if list_of_integers is []:
        return None
    peak = int()

    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i - 1] <= list_of_integers[i]\
        and list_of_integers[i] >= list_of_integers[i + 1]:
             peak = list_of_integers[i]
             i += 2
    return peak
