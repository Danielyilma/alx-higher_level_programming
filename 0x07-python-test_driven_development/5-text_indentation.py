#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    chars = ['.', '?', ':']
    i = 0
    space=""
    for v in text:
        if i == 0 and v == " ":
            continue
        if v == " ":
            space += " "
            continue
        else:
            print(space, end="")
            space = ""
        print(v, end="")
        i += 1
        if v in chars:
            print("\n")
            i = 0