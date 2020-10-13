#!/usr/bin/python3
"""
Class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Defined the instance attributes(Privates)"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Defines the constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, maybe raises"""
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get the height, maybe raises"""
        self.__height = value

    @property
    def x(self):
        """Get the value of 'x'"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of 'x', mabe raises"""
        self.__x = value

    @property
    def y(self):
        """Get the value of 'y'"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of 'y', maybe raises"""
        self.__y = value
