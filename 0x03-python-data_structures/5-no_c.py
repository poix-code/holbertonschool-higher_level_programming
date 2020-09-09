#!/usr/bin/python3
def no_c(my_string):
    cut_str = ""
    for i in my_string:
        if i not in 'cC':
            cut_str += i
    return cut_str
