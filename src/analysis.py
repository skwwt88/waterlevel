import config

import json

id = "63301150"
record = {}

input_file = open (config.river_data)
json_array = json.load(input_file)
store_list = []

for item in json_array:
    
    store_list.append(item)


print(store_list)