#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_a, t_b = tuple_a + (0, 0), tuple_b + (0, 0)
    return (t_a[0] + t_b[0], t_a[1] + t_b[1])
