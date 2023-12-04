#!/usr/bin/python3
''' class baseGeometry module'''


class BaseGeometry:
    '''implementation'''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be integer".format(name))
        if value <= 0:
            raise ValueError("{} must be grater than 0".format(name))
