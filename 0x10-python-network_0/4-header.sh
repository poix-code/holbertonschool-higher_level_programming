#!/bin/bash
# Sends a GET request to a given URL and displays its body
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
