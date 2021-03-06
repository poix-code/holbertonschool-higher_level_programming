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

    def area(self):
        """Computes the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle drawed by '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for y in range(self.__y):
            print()
        for i in range(self.__height - 1):
            print(' ' * self.__x + '#' * self.__width)
        print(' ' * self.__x + '#' * self.__width, end='')
        print()
        return ''

    def __str__(self):
        """Use of the magic method 'str()'"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Updates the values of the attributes of the class
        in the way of key/value"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for j in kwargs:
                setattr(self, j, kwargs[j])

    def to_dictionary(self):
        """Return de dictionary representation"""
        return {'id': self.id,
                'width': self.__width,
                'height': self.height,
                'x': self.__x,
                'y': self.__y}
