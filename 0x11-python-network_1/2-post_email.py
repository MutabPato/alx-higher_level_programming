#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    # req = urllib.request.Request(url, data)

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
    print("Your email is:", body.decode('utf-8'))
