import unittest
max_integer = __import__('6-max_integer').max_integer

class testmax_integer(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1,2,3,4]), 4)
    def test_nonemax(self):
        self.assertEqual(max_integer([]), None)
    def test_negmax(self):
        self.assertEqual(max_integer([-1, -7, 23, -40]), 23)
    def test_lowmax(self):
        self.assertEqual(max_integer([0, 0 ,0 , -10000]), 0)
    def test_floatmax(self):
        self.assertEqual(max_integer([1.0, 2.4, 5.9, 9.9]), 9.9)
    def test_halfFloatmax(self):
        self.assertEqual(max_integer([1.0, 2.4, 5, 6, 9]), 9)


if __name__ == "__main__":
    unittest.main()
        
        