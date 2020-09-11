#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l_tmp = [i for i, val in a_dictionary.items() if val == value]
    for i in l_tmp:
        del a_dictionary[i]
    return a_dictionary
