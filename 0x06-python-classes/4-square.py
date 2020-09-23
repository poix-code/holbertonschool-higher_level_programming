#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Define the object/instance
    Attributes: size(int)"""

    def __init__(self, size=0):
        """Define attributes of the instance
        and raise on a safe mode."""

        self.size = size

    @property
    def size(self):
        """Get size value"""

        return self.__size

    @size.setter
    def size(self, size):
        """Set size value"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of a square"""

        return self.__size * self.__size
