#!/usr/bin/python3
"""
The program writes a string to a text file.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file, return the length"""
    with open(filename, mode="w", encoding='utf-8') as fd:
        string = fd.write(text)
    return string
