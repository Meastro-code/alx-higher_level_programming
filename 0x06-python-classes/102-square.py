#!/usr/bin/python3
"""
A class square that defines a square
"""
class Square:
    """
    This class represents a square.

    Attributes:
        __size (float or int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        area(self): Returns the area of the square.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        __eq__(self, other): Returns True if the area of the square is equal to the area of the other square.
        __ne__(self, other): Returns True if the area of the square is not equal to the area of the other square.
        __gt__(self, other): Returns True if the area of the square is greater than the area of the other square.
        __ge__(self, other): Returns True if the area of the square is greater than or equal to the area of the other square.
        __lt__(self, other): Returns True if the area of the square is less than the area of the other square.
        __le__(self, other): Returns True if the area of the square is less than or equal to the area of the other square.
    """
    def __init__(self, size=0):
        self.size = size

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
            value (float or int): The size of the square.

        Returns:
            None
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """
        Returns True if the area of the square is equal to the area of the other square.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the square is equal to the area of the other square, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Returns True if the area of the square is not equal to the area of the other square.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the square is not equal to the area of the other square, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Returns True if the area of the square is greater than the area of the other square.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the square is greater than the area of the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Returns True if the area of the square is greater than or equal to the area of the other square.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the square is greater than or equal to the area of the other square, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Returns True if the area of the square is less than the area of the other square.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the square is less than the area of the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Returns True if the area of the square is less than or equal to the area of the other square.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the square is less than or equal to the area of the other square, False otherwise.
        """
        return self.area() <= other.area()
