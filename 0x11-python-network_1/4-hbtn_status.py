#!/usr/bin/python3
'''using request module'''
import requests

url = "https://alx-intranet.hbtn.io/status"

r = requests.get(url)

data = r.content.decode('utf-8')
print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(data), data))
