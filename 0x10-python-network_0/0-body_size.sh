#!/bin/bash
# Displays the size of the body of a give URL
curl -soI "$1" -w '%{size_download}\n'
