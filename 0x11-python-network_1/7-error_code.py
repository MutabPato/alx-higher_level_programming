#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and
 displays the body of the response (decoded in utf-8)
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
