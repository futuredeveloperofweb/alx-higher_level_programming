#!/usr/bin/python3
'''Module to test the Square class'''

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    '''tests for Square class'''

    def setUp(self):
        '''import module'''
        self.square_instance = Square(5)

    def tearDown(self):
        '''cleans after each test_method'''
        pass

    # ----------------

    def test_class(self):
        '''test square class type'''
        self.assertEqual(str(Square), '<class \'models.square.Square\'>')

    def test_inheritence(self):
        '''check if Square inherites from Base'''
        self.assertTrue(issubclass(Square, Base))

    def test_missing_instance(self):
        '''test the constractor'''
        with self.assertRaises(TypeError) as a:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(a.exception), s)

    def test_too_much_instance(self):
        '''test the constractor with too many args'''
        with self.assertRaises(TypeError) as a:
            r = Square(2, 4, 6, 8, 5, 2)
        s = "__init__() takes from 2 to 5 positional arguments but 7 were given"
        self.assertEqual(str(a.exception), s)

    def test_instance(self):
        '''tests instance'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))

        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 8}
        self.assertDictEqual(r.__dict__, d)

    def test_instance_type(self):
        '''test the instance type'''
        with self.assertRaises(TypeError):
            self.square_instance.size = '1'

    def test_instance_value_negative(self):
        '''test the instance type'''
        with self.assertRaises(ValueError):
            self.square_instance.size = -1

    def test_instantiation_positional(self):
        '''Tests positional instantiation'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 13}
        self.assertEqual(r.__dict__, d)

    def test_instantiation_keyword(self):
        '''Tests positional instantiation'''
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)


if __name__ == '__main__':
    unittest.main()
