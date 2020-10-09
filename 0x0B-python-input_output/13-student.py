#!/usr/bin/python3
"""
The class Student defines a student based on: 11-student.py
"""


class Student:
    """Defines the attributes of the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        dic = {}
        for item in attrs:
            if type(item) != str:
                return self.__dict__
            elif item in self.__dict__.keys():
                dic.update({item: self.__dict__.get(item)})
        return dic

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        if len(json):
            self.__dict__.clear()
            for i in json:
                self.__dict__[key] = json[key]
