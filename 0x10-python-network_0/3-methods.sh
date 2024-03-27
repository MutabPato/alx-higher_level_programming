#!/bin/bash
#cURL only Methods
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
