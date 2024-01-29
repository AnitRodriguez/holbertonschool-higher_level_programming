#!/usr/bin/python3def
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_new = ()
    for y in range(2):
        tuple_new += (tuple_a[y] + tuple_b[y], )
    return tuple_new
