#!/usr/bin/python3
'''loading json file to python object'''
import json


def load_from_json_file(filename):
    '''implementation'''
    with open(filename, 'r') as f:
        return json.load(f)