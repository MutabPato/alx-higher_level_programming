#!/bin/bash
#Only status code
curl -s -L -X HEAD -W "%{http_code}" "$1" 
