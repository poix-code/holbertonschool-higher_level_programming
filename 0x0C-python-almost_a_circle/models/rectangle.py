#!/usr/bin/python3
"""
Class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Defined the instance attributes(Privates)"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Defines the constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width and raises"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get the height, maybe raises"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of 'x'"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of 'x', mabe raises"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of 'y'"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of 'y', maybe raises"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
