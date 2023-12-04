#!/usr/bin/python3
''' class Square module'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''implementing Square class and inhereting from Rectangle'''

    def __init__(self, size):
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)

    def area(self):
        return super().area()
