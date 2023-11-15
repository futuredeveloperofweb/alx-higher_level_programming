#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """define the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constractore"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, n_width):
        if type(n_width) is not int:
            raise TypeError('width must be an integer')
        if n_width <= 0:
            raise ValueError('width must be > 0')
        self.__width = n_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, n_height):
        if type(n_height) is not int:
            raise TypeError('height must be an integer')
        if n_height <= 0:
            raise ValueError('height must be > 0')
        self.__height = n_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, n_x):
        if type(n_x) is not int:
            raise TypeError('x must be an integer')
        if n_x < 0:
            raise ValueError('x must be >= 0')
        self.__x = n_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, n_y):
        if type(n_y) is not int:
            raise TypeError('y must be an integer')
        if n_y < 0:
            raise ValueError('y must be >= 0')
        self.__y = n_y

    def area(self):
        """returns the area value of the Rectangle"""
        return self.width * self.height

    def display(self):
        """print the triangle with the # presantation"""
        for b in range(self.y):
            print()
        for h in range(self.height):
            for a in range(self.x):
                print(' ', end='')
            for w in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """print a message"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x,
                   self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            for k, v in zip(['id', 'width', 'height', 'x', 'y'], args):
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}


if __name__ == '__main__':
    print(str(Rectangle))
