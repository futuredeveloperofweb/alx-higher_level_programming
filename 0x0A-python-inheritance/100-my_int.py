#!/usr/bin/python3
"""
Module for MyInt class"""


class MyInt(int):
    """definition of the MtInt class"""
    def __new__(cls, *args, **kwargs):
        """new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= become =="""
        return int(self) != other

    def __ne__(self, other):
        """== become !="""
        return int(self) == other
