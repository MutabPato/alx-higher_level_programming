#!/bin/bash
#Only status code
curl -Ls -X HEAD -W "%{http_code}" "$1" 
