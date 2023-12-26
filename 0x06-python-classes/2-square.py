#!/usr/bin/python3
"""
Class Square that describes a square
"""
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        None
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
