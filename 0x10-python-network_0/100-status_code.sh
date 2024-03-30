#!/bin/bash
#Only status code
curl -s -L -X HEAD -w "%{http_code}" "$1"
