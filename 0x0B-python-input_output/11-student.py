#!/usr/bin/python3
"""
Module that defines a class Student
"""


class Student:
    """Defines its instances"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary"""
        return self.__dict__
