#!/usr/bin/python3
"""The script fetches 'https://intranet.hbtn.io/status'"""


import requests


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    get = requests.get(url)
    print("Body response:")
    print("\t- type:", type(get.content.decode('utf-8')))
    print("\t- content:", get.content.decode('utf-8'))
