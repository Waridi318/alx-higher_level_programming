#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

values = {'email': argv[2]}
data = urlencode(values)
data = data.encode('utf-8')
req = Request(argv[1], data)
with urlopen(req) as response:
    body = response.read().decode('utf-8')
    print(body)
