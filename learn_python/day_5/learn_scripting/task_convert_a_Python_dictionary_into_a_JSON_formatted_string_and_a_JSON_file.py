
## what is a JSON string?
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data) # USE THE .dumps METHOD TO CONVERT TO A JSON STRING
print(json_string)

## JSON STRING DEFINITION:
# A JSON string is a text representation of data structured in the
# JavaScript Object Notation (JSON) format.
# JSON is a lightweight data interchange format that is easy for humans
# to read and write, and easy for machines to parse and generate.
# It is commonly used for transmitting data in web applications.

## EXERCISE:
# create the dictionary

servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# convert this Python dictionary to a JSON-formatted string
json_string_of_python_dict = json.dumps(servers_dict)
print(f"\nThe JSON string of the Python 'servers_dict' dictionary is:\n{json_string_of_python_dict}.")

# convert this Python dictionary into a JSON file
with open('servers_dict.json', 'w') as my_json_file:
    json.dump(servers_dict, my_json_file, indent=4)

## SUMMARY:
# json.dumps() ==> converts a Python dictionary into a JSON-formatted string
# json.dump() ==> converts a Python dictionary into a JSON file.


n.dump() ==> converts a Python dictionary into a JSON file.

## DEMO
# 1. convert Python dictionary to Json string:
# new_json_string = json.dumps(servers_dict)
# print(new_json_string)

# 2. convert Python dict to Json file.
with open('fresh_dump_servers_dict.json', 'w') as my_json_file:
    json.dump(servers_dict, my_json_file, indent=4) # servers_dict is the Python dict