#!/bin/bash
#cURL only Methods
curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print $2}'
