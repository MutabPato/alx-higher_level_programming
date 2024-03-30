#!/usr/bin/python3
"""
takes a repository name and owner name and uses the GitHub API
to display 10 most recent commits of the repository
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"

    r = requests.get(url)

    json_r = r.json()

    for commit in json_r:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print("{}: {}".format(sha, author))
