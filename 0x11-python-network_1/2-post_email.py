#!/usr/bin/python3
'''post an email adderess to the given url'''
from urllib import request, parse
import sys


url = sys.argv[1]
param = {
    'email': sys.argv[2]
}

data = parse.urlencode(param).encode('ascii')
url = request.Request(url, param)

with request.urlopen(url) as response:
    print(response.read().decode('utf-8'))
