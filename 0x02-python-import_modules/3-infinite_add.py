#!/usr/bin/python3
import sys
if __name__ == "__main__":
    res = 0
    r = len(sys.argv)
    if r > 1:
        for i in range(1, r):
            res = res + int(sys.argv[i])
    print("{}".format(res))
