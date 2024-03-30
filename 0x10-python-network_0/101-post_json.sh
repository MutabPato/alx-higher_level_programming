#!/bin/bash
#Only status code
curl -s -L "$1" -d "@$2" -X POST -H 'Content-Type: application/json'
