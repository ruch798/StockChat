import json

with open("data.json") as filename:
        data=json.load(filename)
print(data.keys())

