#!/bin/bash
#cURL body size
curl -sI "$1" | wc -c
