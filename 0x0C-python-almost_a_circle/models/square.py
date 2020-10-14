#!/usr/bin/python3
"""
Program that defines a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defined the instance attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """Defines the construtor, inherits the attributes
        from the class Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Using of the magic method 'str()'"""
        return "[Square] {()} {}/{} - {}".format(self.id,
                                               self.x,
                                               self.y,
                                               self.width)
