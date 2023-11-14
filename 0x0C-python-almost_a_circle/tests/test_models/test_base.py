#!/usr/bin/python3
"""Unittest module for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """tests for the base class"""

    def setup(self):
        """test a class attribute"""
        Base._Base__nb_objects = 0
        pass

    def test_nb_objects_exist(self):
        """test if an object exist"""
        self.assertTrue(hasattr(Base, '_base__nb_objects'))

    def test_nb_objects_value(self):
        '''check the nb_objects value'''
        self.assertEqual(getattr(Base, '_Base__nb_objects'), 0)

    def test_instance(self):
        '''test the instances of Base class'''
        b = Base()
        self.assertEqual(str(type(b)), '<class\'__main__.Base\'>')
        self.assertEqual(b.__dict__, {'id': 1})
        self.assertEqual(b.id, 1)

    def test_consecutive_id(self):
        '''Test consecutive ids'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_obj_and_inst(self):
        '''Test obj and instance'''
        b = Base()
        self.assertEqual(getattr(Base, '_Base__nb_objects'), b.id)

    def test_more_obj_inst(self):
        '''Test obj and instance'''
        b = Base()
        b = Base('Fo')
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, '_Base__nb_objects'), b.id)

    def test_id_int(self):
        '''test int id'''
        i = 88
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_str(self):
        '''test str id'''
        i = 'fooo'
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_as_arg(self):
        '''test id by args'''
        i = 433
        b = Base(id=i)
        self.assertEqual(b.id, i)

    #--------------test 15------------------

    def test_to_json_string(self):
        '''test the json string'''
        self.assertEqual(Base.to_json_strint(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        x = [{'x': 10, 'y': 203, 'width': 312, 'id': 52223,
            'height': 2724}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        x = [{'fooooo', 72462}]
        self.assertEqual(Base.to_json_string(d), '[{\'fooooo\', 72462}]')
        x = [{"foooo": 524643}, {"abc": 12}, {"H": 0}]
        self.assertEqual(Base.to_json_string(x), '[{"foooo": 524643}, {"abc": 12}, {"H": 0}]'

    #------------test 16------------------
    def test_save_to_file(self):
        '''test save_to_file test'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    #-------------test 17-----------------
    def test_from_json_string(self):
        '''test the from_json_string function'''
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 12, "y": 32, "width": 33, "id": 2, "height": 5},
            {"x": 124, "y": 20135, "width": 13531, "id": 35534, "height": 33530}]'
        d = [{"x": 12, "y": 32, "width": 33, "id": 2, "height": 5},
            {"x": 124, "y": 20135, "width": 13531, "id": 35534, "height": 33530}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"fooooo": 9842424}]
        s = '[{"fooooo": 9842424}]'
        self.assertEqual(Base.from_json_string(s), d)

        list_in = [
                {'id': 24, 'width': 33, 'height': 12},
                {'id': 5, 'width': 11, 'height': 35}
        ]
        list_out = Rectangle.from_json_string(Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)
        
    #-------------------test 18--------------------
    def test_create(self):
        '''test the create function'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    #-----------------test 19---------------------
    def test_laod_from_file(self):
        '''test the load_from_file function'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

if __name__ == '__main__':
    unittest.main()
