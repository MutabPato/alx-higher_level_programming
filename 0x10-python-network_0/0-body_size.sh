#!/bin/bash
#cURL body size
curl -sI "$1" |grep -i content-lenght | awk '{print $2}' | tr -d '\r'
