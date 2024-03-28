#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    request = r.headers.get('X-Request-Id')
    print(request)
