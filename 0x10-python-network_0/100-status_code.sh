#!/bin/bash
#Only status code
curl -s /dev/null -w "%{http_code}" "$1"
