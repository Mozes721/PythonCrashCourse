import json

with open('favourite_number.json') as f:
    load = json.load(f)

print("Is this the one? " +  load)