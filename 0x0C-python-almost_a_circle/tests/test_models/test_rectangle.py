#!/usr/bin/python3
'''Module to test Rectangle class'''

import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO


class TestRectangleMethods(unittest.TestCase):

    def setUp(self):
        """Set up for the test"""
        self.rectangle_instance = Rectangle(5, 10, 2, 3, 1)

    def test_valid_attributes(self):
        """Test the value of each instance"""
        self.assertEqual(self.rectangle_instance.width, 5)
        self.assertEqual(self.rectangle_instance.height, 10)
        self.assertEqual(self.rectangle_instance.x, 2)
        self.assertEqual(self.rectangle_instance.y, 3)
        self.assertEqual(self.rectangle_instance.id, 1)

    # -------------------test of setters for instances-------

    def test_invalid_width_type(self):
        """Test width with invalid type"""
        with self.assertRaises(TypeError):
            self.rectangle_instance.width = '1'

    def test_invalid_width_value(self):
        """Test width with invalid width value"""
        with self.assertRaises(ValueError):
            self.rectangle_instance.width = -1

    def test_invalid_width_value_0(self):
        """Test width with invalid width value"""
        with self.assertRaises(ValueError):
            self.rectangle_instance.width = 0

    def test_invalid_height_type(self):
        '''test height with invalid type'''
        with self.assertRaises(TypeError):
            self.rectangle_instance.height = '2'

    def test_invalid_height_value(self):
        '''test height with invalid value'''
        with self.assertRaises(ValueError):
            self.rectangle_instance.width = -2

    def test_invalid_height_value_0(self):
        '''test height with invalid value'''
        with self.assertRaises(ValueError):
            self.rectangle_instance.width = -2

    def test_invalid_x_type(self):
        '''test x with invalid type'''
        with self.assertRaises(TypeError):
            self.rectangle_instance.x = '1'

    def test_invalid_x_value(self):
        '''test x with invalid value'''
        with self.assertRaises(ValueError):
            self.rectangle_instance.x = -1

    def test_invalid_y_type(self):
        '''test y with invalid type'''
        with self.assertRaises(TypeError):
            self.rectangle_instance.y = '2'

    def test_invalid_y_value(self):
        '''test y with invalid value'''
        with self.assertRaises(ValueError):
            self.rectangle_instance.y = -1

    # --------------test the area function-----------------
    def test_area(self):
        """Test the area function"""
        self.assertEqual(self.rectangle_instance.area(), 50)

        r = Rectangle(4, 3)
        self.assertEqual(r.area(), 12)

        r1 = Rectangle(7, 6, 3, 4, 1)
        self.assertEqual(r1.area(), 42)

    # ---------------test the display function--------------
    def test_display(self):
        """Test the display function"""
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        self.rectangle_instance.display()

        printed_output = sys.stdout.getvalue()

        sys.stdout = original_stdout

    # -------------test the to_dictionary function------------
    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        rectangle_instance = {'x': 2, 'y': 3,
                              'id': 1, 'height': 10, 'width': 5}
        self.assertEqual(
            self.rectangle_instance.to_dictionary(), rectangle_instance)

        r = Rectangle(2, 3)
        a = {'x': 0, 'y': 0, 'id': 4, 'height': 3, 'width': 2}
        self.assertEqual(r.to_dictionary(), a)

        r = Rectangle(1, 2, 3, 4, 5)
        a = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r.to_dictionary(), a)

    def test_update(self):
        """Test the update function"""
        self.rectangle_instance.update(2, 7, 15, 4, 6)

        self.assertEqual(self.rectangle_instance.id, 2)
        self.assertEqual(self.rectangle_instance.width, 7)
        self.assertEqual(self.rectangle_instance.height, 15)
        self.assertEqual(self.rectangle_instance.x, 4)
        self.assertEqual(self.rectangle_instance.y, 6)


if __name__ == '__main__':
    unittest.main()
