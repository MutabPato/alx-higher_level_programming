#!/bin/bash
#cURL body size
curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r'
