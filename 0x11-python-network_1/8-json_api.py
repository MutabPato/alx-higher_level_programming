#!/usr/bin/python3
"""
that takes in a letter and sends a POST request to http://0.0.0.0:5000/search
_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    r = requests.post(url, data=data)
    json_r = r.json

    try:
        if json_r:
            print("{} {}".format(json_r['id'], json_r['name']))
        else:
            print("No result")
    except TypeError:
        print("Not a valid JSON")
