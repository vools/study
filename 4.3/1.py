import json

with open("1.json", "r") as js:
    json_dict=json.load(js)

print(json_dict)