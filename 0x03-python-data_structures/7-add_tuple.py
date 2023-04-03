#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    else:
        tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    else:
        tuple_b = tuple_b[:2]
    x, y = tuple_a
    a, b = tuple_b
    tuple_c = x+a, b+y
    return(tuple_c)
