#!/usr/bin/python3
"""
Base class of this project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """adding the static method dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
