#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        value = number * -1
    else:
        value = number
    value %= 10
    print(value, end='')
    return value
