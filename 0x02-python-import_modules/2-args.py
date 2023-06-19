#!/usr/bin/python3
import sys
if __name__ == "__main__":
    r = len(sys.argv)
    if r == 1:
        print("{} arguments.".format(r - 1))
    elif r == 2:
        print("{} argument:".format(r - 1))
        print("{}: {}".format(r - 1, sys.argv[1]))
    elif r > 2:
        print("{} arguments:".format(r - 1))
        for i in range(2, r + 1):
            print("{}: {}".format(i - 1, sys.argv[i - 1]))
