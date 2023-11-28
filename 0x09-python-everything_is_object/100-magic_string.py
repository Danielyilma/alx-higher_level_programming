#!/usr/bin/python3

def count(length):
    def magic_string():
        nonlocal length
        result = ""
        length += 1
        for i in range(length):
            result += "BestSchool"
            if i != length - 1:
                result += ", "
        return result
    return magic_string
magic_string = count(0)