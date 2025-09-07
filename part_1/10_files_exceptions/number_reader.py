import json

filename = 'numbers.json'

with open(filename) as f:
    numbers  = json.load(f)
    # json.load(<object to read from in json format>)

print(numbers)