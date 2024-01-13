#!/usr/bin/python3
"""Module for square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """definition of the class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constractore
        Args:
            size: the size of the square
            x: the element x
            y: the element y
            id: the id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """display a message"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, n_size):
        self.width = n_size
        self.height = n_size

    def update(self, *args, **kwargs):
        """ assigns attributes
        Args:
            args: is the list of arguments
            kwargs: can be thought of as a double pointer to a dictionary
        """
        if args:
            for k, v in zip(['id', 'size', 'x', 'y'], args):
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
