#!/bin/bash
# Sends a request to a URL and displays only the status code of the response.
curl -soI "$1" -w "%{http_code}"
