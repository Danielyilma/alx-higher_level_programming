#!/bin/bash
# printing content length
curl -I -s "$1" | awk '{if ($1=="Content-Length:") {print $2}}'
