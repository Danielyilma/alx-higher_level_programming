#!/usr/bin/python3
''' test module for Base class'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def read_file(filepath):
    '''reading from a given file'''
    with open(filepath, "r") as f:
        return f.read()


class Test_base(unittest.TestCase):
    '''testing every functionality of Base class'''
    @classmethod
    def setUpClass(cls):
        '''setting up the test class before
            testing each function of Base class
        '''
        cls.base1 = Base()
        cls.base2 = Base(12)
        cls.base3 = Base()
        cls.dict1 = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}
            ]
        cls.json_string = '[{"id": 1, "width": 10, "height": 7,'\
                          ' "x": 2, "y": 8}, {"id": 2, "width": 2,'\
                          ' "height": 4, "x": 0, "y": 0}]'

        cls.rec = Rectangle(5, 5, 1, 1, 11)
        cls.squ = Square(4, 1, 1)

    def test_instance(self):
        '''checking if the instance if properly created'''
        self.assertIsInstance(self.base1, Base)
        self.assertIsNot(self.base1, self.base2)
        self.assertIsInstance(self.rec, Base)
        self.assertIsInstance(self.squ, Base)

    def test_instance_attrubute(self):
        '''checking if the instance obj's id handled correctly'''
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 12)
        self.assertEqual(self.base3.id, 2)

    def test_to_json_string(self):
        '''checking the functionallity of to_json_string'''
        with self.assertRaises(TypeError):
            Base.to_json_string()
            Base.to_json_string({})
        self.assertMultiLineEqual(Base.to_json_string(self.dict1),
                                  self.json_string)

    def test_save_to_file(self):
        '''checking the functionality of save_to_file'''
        with self.assertRaises(TypeError):
            self.rec.save_to_file()

        Base.save_to_file(None)
        self.assertEqual(read_file("Base.json"), "[]")

        Base.save_to_file([])
        self.assertEqual(read_file("Base.json"), "[]")

        list_obj = [(Rectangle(i, i + 1)) for i in range(1, 4)]
        Rectangle.save_to_file(list_obj)
        data = Base.to_json_string([obj.to_dictionary() for obj in list_obj])
        self.assertEqual(read_file("Rectangle.json"), data)

        list_obj = [(Square(i, i + 1)) for i in range(1, 4)]
        Square.save_to_file(list_obj)
        data = Base.to_json_string([obj.to_dictionary() for obj in list_obj])
        self.assertEqual(read_file("Square.json"), data)

    def test_from_json_string(self):
        '''checking the functionality of from_json_string'''
        with self.assertRaises(TypeError):
            Base.from_json_string()

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(self.json_string), self.dict1)

    def test_create_obj(self):
        '''checking the functionality of creating object from dict'''
        self.assertEqual(Base.create(), None)

        recDic = self.rec.to_dictionary()
        new_square = Base.create(**recDic)
        self.assertIsInstance(new_square, Rectangle)
        self.assertDictEqual(new_square.to_dictionary(), recDic)

        squDic = self.squ.to_dictionary()
        new_square = Base.create(**squDic)
        self.assertIsInstance(new_square, Square)
        self.assertDictEqual(new_square.to_dictionary(), squDic)

    def test_load_from_file(self):
        '''checking the functionality of load_from_file'''
        # creating 3 different rectangle object
        list_obj = [(Rectangle(i, i + 1)) for i in range(1, 4)]

        # saving the rectangle object to a file
        Rectangle.save_to_file(list_obj)

        # loading the data from the file and creating object
        new_listobj = Rectangle.load_from_file()

        # testing if the content of the loaded obj are the same as before
        for new_obj, obj in zip(new_listobj, list_obj):
            self.assertDictEqual(obj.to_dictionary(), new_obj.to_dictionary())

        # cheking it with Square obj
        list_obj = [(Square(i, i + 1)) for i in range(1, 4)]

        Square.save_to_file(list_obj)
        new_listobj = Square.load_from_file()

        for new_obj, obj in zip(new_listobj, list_obj):
            self.assertDictEqual(obj.to_dictionary(), new_obj.to_dictionary())

if __name__ == "__main__":
    unittest.main()
