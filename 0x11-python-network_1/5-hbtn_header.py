#!/usr/bin/python3
'''printing the content of the response header'''
import requests
import sys


url = sys.argv[1]
r = requests.get(url)
print(r.headers.get('X-Request-Id'))
