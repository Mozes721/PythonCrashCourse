import json
try:
    with open('favourite_number.json') as f:
        load = json.load(f)
except FileNotFoundError:
    number = input("Enter number! ")
    with open('favourite_number.json', 'w') as f:
        f.write(number, f)

with open('favourite_number.json') as f:
    load = json.load(f)
    print("Is this the one? " +  load)