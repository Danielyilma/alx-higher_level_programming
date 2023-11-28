#!/usr/bin/python3
''' defining locked class'''


class LockedClass:
    ''' user can only set first name attribute'''

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has\
 no attribute 'last_name'")
        else:
            self.__dict__[name] = value
