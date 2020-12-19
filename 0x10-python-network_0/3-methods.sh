#!/bin/bash
# Takes an URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep 'OPTIONS' | cut -d ' ' -f 2-
