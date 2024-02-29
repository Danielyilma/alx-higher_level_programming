#!/usr/bin/python3
''''''

def find_peak(list_of_integers):
    ''''''
    max = list_of_integers[0]
    for val in list_of_integers:
        if val > max:
            max = val
    return max
