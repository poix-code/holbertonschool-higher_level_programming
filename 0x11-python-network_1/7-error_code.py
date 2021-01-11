#!/usr/bin/python3
"""Displays a body response of a URL request"""


import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    req = requests.get(url)
    if req.status_code == 200:
        print(req.content.decode('utf-8'))
    else:
        print("Error code:", req.status_code)
