#!/usr/bin/python3
"""Sends a request to an URL and isplays the value of a variable"""


import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    req = requests.get(url)
    print(req.headers['X-Request-Id'])
