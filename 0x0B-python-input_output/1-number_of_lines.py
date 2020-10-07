#!/usr/bin/python3
"""
The program returns the number of lines of a text file.
"""


def number_of_lines(filename=""):
    """Opens/closes the file in a safe way,
       and returns the number of lines.
    """
    i = 0
    with open(filename, encoding='utf-8') as fd:
        for lines in fd:
            i += 1
        return i
