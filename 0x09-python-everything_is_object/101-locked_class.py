#!/usr/bin/python3
"""Module for LockedClass class"""


class LockedClass:
    """prevent the user to use any attribute excepte 'first_name'"""
    __slots__ = ['first_name']
