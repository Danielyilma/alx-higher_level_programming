#!/usr/bin/python3


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):

    def __init__(self, size):
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
    
    def area(self):
        return super().area()

    def __Str__(self):
        return "[Square] {}/{}".format(super().__width, super().__height)
