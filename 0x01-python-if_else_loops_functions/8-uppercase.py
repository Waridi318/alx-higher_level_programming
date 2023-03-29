#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        uppercase = chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        uppercase_str += uppercase
    print("{}".format(uppercase_str))
