#!/bin/bash
#cURL body size
curl -s "$1" -o response.txt -w "%{http_code}" | awk '/^200$/{getline; print}'
