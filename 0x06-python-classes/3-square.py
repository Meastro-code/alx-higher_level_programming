#!/usr/bin/python3
"""
A square class defining a square 
"""
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area(self): Returns the area of the square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Args:
            None

        Returns:
            The area of the square.
        """
        return self.__size ** 2
