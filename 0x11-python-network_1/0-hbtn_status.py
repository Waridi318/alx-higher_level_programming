#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
"""


from urllib.request import urlopen, Request

req = Request('https://alx-intranet.hbtn.io/status')

with urlopen(req) as response:
    body = response.read()

print("Body response:")
print(f"\t- type: {type(body)}\n\t- content: {body}")
print(f"\t- utf8 content: {body.decode()}")
