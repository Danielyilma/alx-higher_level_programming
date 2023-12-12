#!/usr/bin/python3
'''test module for Rectangle class'''
import unittest
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    '''testing every functionality of Rectangle class'''

    @classmethod
    def setUpClass(cls):
        '''setting up the class before testing'''
        cls.rec1 = Rectangle(2, 3, 0, 1, 11)

    def test_isinstance(self):
        '''checking if the instance is properly created'''
        self.assertIsInstance(self.rec1, Rectangle)

    def test_inheritance(self):
        '''checking proper base class inheritance'''
        self.assertIsInstance(self.rec1, Base)

    def test_validateinput(self):
        '''checking the validate function'''
        with self.assertRaises(TypeError) as e:
            Rectangle("cc", 1)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(1, "ww")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(-1, -1)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 3)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(3, -1)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_getter(self):
        '''checking the getter of all the class private attribute'''
        self.assertEqual(self.rec1.width, 2)
        self.assertEqual(self.rec1.height, 3)
        self.assertEqual(self.rec1.x, 0)
        self.assertEqual(self.rec1.y, 1)

    def test_setter(self):
        '''checking all the class private attribute setter'''
        with self.assertRaises(TypeError) as e:
            self.rec1.width = "vv"
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            self.rec1.height = "vv"
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            self.rec1.x = "vv"
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            self.rec1.y = "vv"
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            self.rec1.width = 0
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            self.rec1.height = 0
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            self.rec1.x = -1
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            self.rec1.y = -1
        self.assertEqual(str(e.exception), "y must be >= 0")

        self.rec1.width = 3
        self.assertEqual(self.rec1.width, 3)

        self.rec1.height = 2
        self.assertEqual(self.rec1.height, 2)

        self.rec1.x = 2
        self.assertEqual(self.rec1.x, 2)

        self.rec1.y = 4
        self.assertEqual(self.rec1.y, 4)

    def test_area(self):
        '''checking the functionality of the area method'''
        rec = Rectangle(1, 10)
        self.assertEqual(rec.area(), 10)

        rec = Rectangle(2, 3)
        self.assertEqual(rec.area(), 6)

        rec = Rectangle(1, 1)
        self.assertEqual(rec.area(), 1)

    def display(self):
        '''checking the functionality of display method'''
        rec = Rectangle(1, 2)
        pic = "#\n#"
        self.assertEqual(rec.display(), pic)

        rec = Rectangle(2, 2, 1, 1)
        pic = "\n ##\n ##"
        self.assertEqual(rec.display(), pic)

        rec = Rectangle(2, 2, 1)
        pic = "\n##\n##"
        self.assertEqual(rec.display(), pic)

        rec = Rectangle(2, 2, 0, 1)
        pic = " ##\n ##"
        self.assertEqual(rec.display(), pic)

    def test_str(self):
        '''checking the custom dunder method of str'''
        rec = Rectangle(2, 1, 0, 0, 4)
        repr = "[Rectangle] (4) 0/0 - 2/1"
        self.assertEqual(str(rec), repr)

        rec = Rectangle(5, 1, 1, 1, 12)
        repr = "[Rectangle] (12) 1/1 - 5/1"
        self.assertEqual(str(rec), repr)

    def test_update(self):
        '''checking the functionality of update method'''
        rec = Rectangle(2, 3)
        rec.update(11, 4, 5, 7, 3)
        string = "[Rectangle] (11) 7/3 - 4/5"
        self.assertEqual(str(rec), string)

        dic = rec.to_dictionary()
        dic["id"], dic["width"], dic["height"] = 12, 5, 6
        rec.update(**dic)
        self.assertDictEqual(rec.to_dictionary(), dic)

    def test_to_dictionary(self):
        '''checking the functionality of to_dictionary method'''
        dic = {
            "id": 21,
            "width": 4,
            "height": 6,
            "x": 1,
            "y": 1
        }
        rec = Rectangle(4, 6, 1, 1, 21)
        self.assertDictEqual(rec.to_dictionary(), dic)

        rec.update(id=12, width=8, x=0)
        dic["id"], dic["width"], dic["x"] = 12, 8, 0
        self.assertDictEqual(rec.to_dictionary(), dic)

if __name__ == "__main__":
    unittest.main()
