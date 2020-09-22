#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    state = False
    try:
        print("{:d}".format(value))
        state = True
    except Exception as err:
        print("Exception: {}".format(err))
    return state
