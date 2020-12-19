#!/bin/bash
# You got me too!
curl -so dev/null 0.0.0.0:5000/catch_me -w 'You got me!'
