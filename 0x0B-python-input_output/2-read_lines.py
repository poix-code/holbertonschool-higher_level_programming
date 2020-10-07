#!/usr/bin/python3
"""
The program reads n lines of a text file and print it
"""


def read_lines(filename="", nb_lines=0):
    """Print the lines base on the offset"""
    with open(filename, encoding='utf-8') as fd:
        if nb_lines <= 0:
            print(fd.read(), end='')
        else:
            print(fd.readline() * nb_lines)
