#!/bin/bash
# printing all HTTP mothods
curl -sLi -X OPTIONS $1 | awk '{if ($1=="Allow:") {sub($1 FS, ""); print}}'
