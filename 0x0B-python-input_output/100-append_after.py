#!/usr/bin/python3
'''reading and writing to a file'''


def append_after(filename="", search_string="", new_string=""):
    '''implementation'''
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
