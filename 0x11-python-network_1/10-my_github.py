#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    credentials = HTTPBasicAuth(username, password)
    r = requests.get(url, auth=credentials)

    json_r = r.json()
    print(json_r.get('id'))
