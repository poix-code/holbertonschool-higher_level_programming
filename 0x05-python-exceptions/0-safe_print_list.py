#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = 0
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            length += 1
        print()
        return length
    except:
        print()
        return length
