#!/usr/bin/python3
''' Base class to all objects'''
import json
import csv


class Base:
    '''base class implementation'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_serial = []

        if list_objs is None or list_objs == []:
            with open(filename, "w") as f:
                f.write("[]")
            return

        for obj in list_objs:
            json_serial.append(obj.to_dictionary())

        data = Base.to_json_string(json_serial)
        with open(filename, "w") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if dictionary == {}:
            return None

        if "size" in dictionary.keys():
            dummy = Square(1, 1)
        else:
            dummy = Rectangle(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        list_obj = []

        with open(filename, "r") as f:
            data = f.read()

        if data is None:
            return list_obj

        list_of_dict = Base.from_json_string(data)
        for dic in list_of_dict:
            list_obj.append(Base.create(**dic))
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        list_of_dict = [dic.to_dictionary() for dic in list_objs]

        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        with open(filename, "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file,
                                        fieldnames=fieldnames, delimiter=",")
            csv_writer.writeheader()
            for line in list_of_dict:
                csv_writer.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        list_of_obj = []

        with open(filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                list_of_obj.append(Base.create(**line))
        return list_of_obj
