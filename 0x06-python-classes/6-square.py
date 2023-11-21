#!/usr/bin/python3

'''defining square class'''


class Square:
    '''square definition'''
    def __init__(self, size=0, position=(0, 0)):
        '''check the size to be integer and greater than zero '''
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
        if len(position) != 2:
            print("position must be a tuple of postive integers")
            raise TypeError
        elif len(position) == 2:
            if (type(position[0]) is not int or type(position[1]) is not int):
                print("position must be a tuple of postive integers")
                raise TypeError
            else:
                self.__position = position

    @property
    def size(self):
        '''getter of the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter of the size'''
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        '''getter for the position'''
        return self.position

    @position.setter
    def position(self, value):
        '''setter for position'''
        if len(value) != 2:
            print("position must be a tuple of postive integers")
            raise TypeError
        elif len(value) == 2:
            if (type(value[0]) is not int or type(value[1]) is not int):
                print("position must be a tuple of postive integers")
                raise TypeError
            else:
                self.__position = value

    def area(self):
        '''the area of the square'''
        return self.__size * self.__size

    def my_print(self):
        '''print # character in the square size'''
        for i in range(self.size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print()
