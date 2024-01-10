#!/usr/bin/python3
"""
  class square
"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """" class square """
    def __init__(self, size):
        """ function to create instance """
        super().__init__(size, size)

    def __str__(self):
        """ function to string """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"

    def area(self):
        """ function area """
        return self._Rectangle__width * self._Rectangle__height
