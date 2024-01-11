#!/usr/bin/python3
"""
   Class Rectangle
"""

class Rectangle:
    """A class that defines Rectangles."""

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """int: The area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """int: The perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
