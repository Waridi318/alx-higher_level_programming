#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and
displays the value of the variable X-Request-Id
in the response header
"""


from sys import argv
from requests import get

if __name__ == "__main__":
    r = get(argv[1])
    try:
        # if (r.headers['X-Request-Id']):
        print(r.headers['X-Request-Id'])
    except Exception:
        pass
