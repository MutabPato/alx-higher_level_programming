#!/usr/bin/python3
"""
that takes in a letter and sends a POST request to http://0.0.0.0:5000/search
_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1 and isinstance(sys.argv[1], str):
        q = sys.argv[1]
    else:
        q = ""

    value = {'q': q}
    r = requests.post(url, data=value)

    try:
        json_r = r.json()
        if json_r:

            print("{} {}".format(json_r.get('id'), json_r.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
