#!/usr/bin/python3
"""
displays the body of the response.
"""


from sys import argv
from requests import post

if __name__ == "__main__":
    payload = {'email': argv[2]}
    p = post(argv[1], payload)
    print(p.text)
