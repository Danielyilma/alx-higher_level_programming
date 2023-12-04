#!/usr/bin/python3
'''myList class'''


class MyList(list):
    '''MyList class implementation'''
    def __init__(self, *args):
        list.__init__(self, *args)

    def print_sorted(self):
        temp = MyList()
        temp = self.copy()
        temp.sort()
        print(temp)
