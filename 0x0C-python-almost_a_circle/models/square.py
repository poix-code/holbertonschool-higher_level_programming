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
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """Get the size of the object"""
        return self.width

    @size.setter
    def size(self, size):
        """Set the value of the object"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the value of the class Square"""
        attr =['id', 'size', 'x', 'y']
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for j in kwargs:
                setattr(self, j, kwargs[j])
