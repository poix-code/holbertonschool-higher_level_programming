#!/usr/bin/python3
"""Sends a POST request to an URL sending an email, display the body"""


from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    mail = argv[2]
    values = {'email': mail}
    values = parse.urlencode(values).encode('utf-8')
    with request.urlopen(url, values) as response:
        print(response.read().decode('utf-8'))
