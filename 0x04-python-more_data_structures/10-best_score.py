#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    list_key = list(a_dictionary)
    max = 0
    for i in range(len(a_dictionary)):
        if a_dictionary[list_key[i]] > a_dictionary[list_key[max]]:
            max = i
    return list_key[max]
