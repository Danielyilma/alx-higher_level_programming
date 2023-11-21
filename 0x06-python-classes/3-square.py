#!/usr/bin/python3

'''defining square class'''


class Square:
    '''square definition'''
    def __init__(self, size=0):
        '''check the size to be integer and greater than zero '''
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
