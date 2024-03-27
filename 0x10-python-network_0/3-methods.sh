#!/bin/bash
#cURL only Methods
curl -s -i -X OPTIONS "$1" | grep 'Allow:' | awk '{print $2}'
