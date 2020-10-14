#!/usr/bin/python3
"""
Base class of this project
"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON rep. in a file"""
        ls = []
        filename = "{}.json".format(cls.__name__)
        if list_objs:
            for instance in list_objs:
                ls.append(instance.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        obj = []
        filename = cls.__name__ + '.json'
        if not os.path.isfile(filename):
            return obj
        with open(filename, mode='r', encoding='utf-8') as f:
            list_dicts = cls.from_json_string(f.read())
            for d in list_dicts:
                obj.append(cls.create(**d))
            return obj
