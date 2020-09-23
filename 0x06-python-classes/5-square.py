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
    def size(self, value):
        """Set size value"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of a square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints the squarer"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
