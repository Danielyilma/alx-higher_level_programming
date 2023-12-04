#!/usr/bin/python3
'''MyInt module'''


class MyInt(int):
    '''Myint implementation inherting from int'''
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
