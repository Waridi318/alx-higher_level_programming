#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return(1)
    elif b < 0:
        res = 1
        for i in range(b, 0):
            res = res * (1 / a)
    else:
        res = 1
        for i in range(1, (b + 1)):
            res *= a
    return res
