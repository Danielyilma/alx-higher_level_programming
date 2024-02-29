#!/bin/bash
# post request with json file
curl -s -H "Content-type: application/json" -d @$2 $1
