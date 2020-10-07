#!/usr/bin/python3
"""
Check if the object is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """Using the method 'isinstance()' to check"""
    return type(obj) is a_class
