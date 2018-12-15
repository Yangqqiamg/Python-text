import json

with open('data.json', 'r') as file:
    str = file.read()
    print(type(str))
    data = json.loads(str)
    print(data)