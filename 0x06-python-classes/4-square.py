#!/usr/bin/python3
"""
A class square defining a square
"""
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area(self): Returns the area of the square.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
    """
    def __init__(self, size=0):
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

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Args:
            None

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The size of the square.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
