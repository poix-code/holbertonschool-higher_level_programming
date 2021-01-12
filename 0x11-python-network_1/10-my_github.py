#!/usr/bin/python3
"""Display mi ID using the Github API"""


import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    url = "https://api.github.com/user"
    pair = requests.get(url, auth=(user, passwd)).text
    try:
        std = pair[pair.index("id") + 4: pair.index("node") - 2]
    except ValueError:
        std = "None"
    print(std)
