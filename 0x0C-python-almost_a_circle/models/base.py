#!/usr/bin/python3
"""
Base class of this project
"""


class Base:
    """Defines de instances of the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Defines the constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
