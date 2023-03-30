#!/usr/bin/python3
import sys
res = 0
r = len(sys.argv)
if r > 1:
    for i in range(1, r):
        res = res + int(sys.argv[i])
print("{}".format(res))
