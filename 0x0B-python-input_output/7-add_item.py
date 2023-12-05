#!/usr/bin/python3
'''adding argument and saving to json file'''

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

value = []
for val in sys.argv[1:]:
    value.append(val)

save_to_json_file(value, "add_item.json")
