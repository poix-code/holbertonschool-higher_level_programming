#!/usr/bin/python3
"""Sends a POST request to the passed URL"""


import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    mail = argv[2]
    value = {'email': mail}
    req = requests.post(url, value)
    print(req.text)
