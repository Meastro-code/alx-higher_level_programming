#!/usr/bin/python3
"""
   class basegeometry
"""
class BaseGeometry:
    """ class basegeometry """
    def area(self):
        """ function area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function integer validator """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
