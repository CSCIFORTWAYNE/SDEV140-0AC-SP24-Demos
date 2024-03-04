import unittest
from rectangle import Rectangle
import random

class TestRectangle(unittest.TestCase):
    def setUpClass(self):
        self.rectangle = Rectangle(0,0)
    def test_normal_case(self):
        length = random.randint(1,100)
        width = random.randint(1,100)
        rectangle = Rectangle(length, width)
        self.assertEqual(rectangle.get_area(), length * width, "incorrect area")
    def test_negative_case(self): 
        """ expect -1 as output to denote error when looking at negative area """
        rectangle = Rectangle(-1, 2)
        self.assertEqual(rectangle.get_area(), -1, "incorrect negative output negative width")
        rectangle = Rectangle(1,-2)
        self.assertEqual(rectangle.get_area(),-1,"incorrect negative output negative height")
    def test_assert_raises(self):    
        with self.assertRaises(AttributeError):
            rectangle = Rectangle(-1,0)
    
""" def test_normal_case():
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, "incorrect area" """

if __name__ == "__main__":
    unittest.main()