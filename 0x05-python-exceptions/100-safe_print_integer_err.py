#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    printed = False
    try:
        print("{:d}".format(value))
        printed = True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    return printed
