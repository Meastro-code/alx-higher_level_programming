#!/usr/bin/python3
import math
"""
MagicClass implementation
"""
class MagicClass:
    """
    This class represents a magic class.

    Attributes:
        __radius (float or int): The radius of the circle.

    Methods:
        __init__(self, radius=0): Initializes a new instance of the MagicClass class.
        area(self): Returns the area of the circle.
        circumference(self): Returns the circumference of the circle.
    """
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.

        Args:
            None

        Returns:
            The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Returns the circumference of the circle.

        Args:
            None

        Returns:
            The circumference of the circle.
        """
        return 2 * self.__radius * math.pi

    @property
    def radius(self):
        """
        Getter method to retrieve the radius of the circle.

        Args:
            None

        Returns:
            The radius of the circle.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Setter method to set the radius of the circle.

        Args:
            value (float or int): The radius of the circle.

        Returns:
            None
        """
        if not isinstance(value, (float, int)):
            raise TypeError("radius must be a number")
        elif value < 0:
            raise ValueError("radius must be >= 0")
        self.__radius = value
