#!/bin/bash
# Sends a POST request to a given URL and displays the body
curl -sX POST "$1" -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
