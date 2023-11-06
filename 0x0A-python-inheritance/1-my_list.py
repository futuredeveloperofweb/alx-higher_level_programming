#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """Class that has a sort function"""
    def print_sorted(self):
        """Function that sorts lists"""
        print(sorted(self))
