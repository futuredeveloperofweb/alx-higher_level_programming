#!/usr/bin/python3
"""Module for width and heigth attributes"""


class Rectangle:
    """defines two attributes"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """arguments of the rectangl
        Args:
            width: the rectangle's width
            height: the rectangle's height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance height"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        """a function that returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """a function that returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """will print the rectangle with the character #"""
        s = ''
        if self.__width != 0 and self.__height != 0:
            s += '\n'.join(str(self.print_symbol) *
                           self.__width for i in range(self.height))
        return s

    def __repr__(self):
        """will print a message"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """a message shown when a message is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """a function that return the biggest rectangle
        Args:
            rect_1: the first rectangle
            rect_2: the second rectangle
        Return:
            the biggest rectangle
        Raises:
            TypeError: if one of the variable is not of type Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        '''a function that return a square
        Args:
            size: the size of the square
        '''
        return cls(size, size)
