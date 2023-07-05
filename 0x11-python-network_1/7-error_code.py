#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and
displays the body of the response
"""


from sys import argv
from requests import get

if __name__ == "__main__":
    bad_r = get(argv[1])
    if bad_r.status_code < 400:
        print(bad_r.text)
    else:
        print(f"Error Code: {bad_r.status_code}")
