#!/bin/bash
# displaying status code of HTTP response
curl -s -o /dev/null -w "%{http_code}" $1
