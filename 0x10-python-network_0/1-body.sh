#!/bin/bash
#cURL body size
curl -s -o response.txt -w "%{http_code}" "$1" | tail -n 1 | grep -q "200" && cat response.txt | sed '$d'
