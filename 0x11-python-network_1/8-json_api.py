#!/usr/bin/python3
"""Sends a letter via POST"""


import requests
from sys import argv


if __name__ == "__main__":
    text = "" if len(argv) == 1 else argv[1]
    URL = "http://0.0.0.0:5000/search_user"
    values = {'q': text}
    response = requests.post(URL, data=values)
    try:
        json_r = response.json()
        if json_r == {}:
            std = "No result"
        else:
            std = "[{}] {}".format(json_r['id'], json_r['name'])
    except ValueError:
            std = "Not a valid JSON"
    print(std)
