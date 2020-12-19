#!/bin/bash
# Displays the size of the body of a give URL
URL="$1"
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
