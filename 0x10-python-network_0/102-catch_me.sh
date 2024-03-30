#!/bin/bash
#Only status code
curl -s -L -X PUT -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
