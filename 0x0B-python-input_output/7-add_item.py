#!/usr/bin/python3
'''adding argument and saving to json file'''


import os
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


value = []
if os.path.exists("add_item.json"):
    value = load_from_json_file("add_item.json")
for val in sys.argv[1:]:
    value.append(val)

save_to_json_file(value, "add_item.json")
