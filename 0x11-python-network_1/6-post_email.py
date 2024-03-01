#!/usr/bin/python3
'''post request'''
import requests
import sys


url = sys.argv[1]
post_data = {'email': sys.argv[2]}
r = requests.post(url, data=post_data)
print(r.content.decode('utf-8'))
