#!/usr/bin/python3
"""
script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


from requests import post
from sys import argv
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}
    p = post(url, payload)
    try:
        json_data = p.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if json_data:
            if 'id' in json_data and 'name' in json_data:
                print(f"[{json_data['id']}] {json_data['name']}")
            else:
                print("No result")
        else:
            print("No result")
