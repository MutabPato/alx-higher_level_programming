#!/bin/bash
#cURL body size
curl -s "$1" -w "%{http_code}" | awk '/^200$/{getline; print}'
