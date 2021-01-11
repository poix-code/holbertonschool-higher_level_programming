#!/usr/bin/python3
"""Send a request and displays a value of a variable"""


from urllib import request
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
