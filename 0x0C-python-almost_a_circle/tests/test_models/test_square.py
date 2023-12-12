#!/usr/bin/python3
'''test module for Square class'''
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_square(unittest.TestCase):
    '''testing every functionality of Square class'''
    @classmethod
    def setUpClass(cls):
        '''setting up the class before testing'''
        cls.square1 = Square(5, 0, 0, 11)

    def test_instance(self):
        '''checking if the instance is proberly created'''
        self.assertIsInstance(self.square1, Square)

    def test_inheritance(self):
        '''checking proper class inheritance'''
        self.assertIsInstance(self.square1, Rectangle)
        self.assertIsInstance(self.square1, Base)

    def test_getter(self):
        '''checking the getter of the attibute'''
        self.assertEqual(self.square1.size, 5)

    def test_setter(self):
        '''checking all the class private attibute setter'''
        with self.assertRaises(TypeError) as e:
            self.square1.size = "e"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            self.square1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

        self.square1.size = 3
        self.assertEqual(self.square1.size, 3)

    def test_update(self):
        '''checking the functionality of update'''
        dic = {
            "id": 12,
            "size": 5,
            "x": 2,
            "y": 6
        }
        self.square1.update(12, 5, 2, 6)
        self.assertEqual(self.square1.to_dictionary(), dic)

    def test_to_dictionary(self):
        '''checking the functionality of to_dictionary'''
        dic = {
            "id": 12,
            "size": 5,
            "x": 2,
            "y": 6
        }

        square = Square(5, 2, 6, 12)
        self.assertEqual(square.to_dictionary(), dic)

if __name__ == "__main__":
    unittest.main()
