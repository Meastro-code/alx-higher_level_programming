#!/usr/bin/python3
"""
   class rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ class rectangle """
    def __init__(self, width, height):
        """" function instance for rectangle """
        self.__width = 0
        self.__height = 0
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ function to string """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ function to calculate area """
        return self.__width * self.__height
