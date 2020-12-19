#!/usr/bin/python3
"""Interview challenge"""


def find_peak(ls):
    """Find a peak in an unsorted list"""

    if len(ls) == 0:
        return None
    length = len(ls)
    if length == 1:
        return ls[0]
    floor_div = length // 2
    if floor_div == length - 1:
        if ls[floor_div] > ls[floor_div - 1]:
            return ls[floor_div]
        return ls[floor_div - 1]
    if ls[floor_div] > ls[floor_div + 1] and ls[floor_div] > ls[floor_div - 1]:
        return ls[floor_div]
    if ls[floor_div + 1] >= ls[floor_div]:
        return find_peak(ls[floor_div:])
    else:
        return find_peak(ls[:floor_div])
