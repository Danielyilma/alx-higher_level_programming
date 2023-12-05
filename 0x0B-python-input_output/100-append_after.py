#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):

    with open(filename, "a+", encoding="utf-8") as f:
        line = f.readline()
        while line:
            if line.find(search_string) != -1:
                f.write(new_string)
            line = f.readline()
