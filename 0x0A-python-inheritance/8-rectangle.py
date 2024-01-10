#!/usr/bin/python3
"""
Module 8-rectangle.py
Defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry. """
    def __init__(self, width, height):
        """ Initializes an instance of Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Returns a string representation of the Rectangle instance. """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Computes the area of the Rectangle instance. """
        return self.__width * self.__height
