#!/usr/bin/python3
'''student module'''


class Student:
    '''class Student implementation'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        if type(attr) is list:
            dic = {}
            for key in attr:
                dic[key] = self.__dict__[key]
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        for key in json.keys():
            setattr(self, key, json[key])
