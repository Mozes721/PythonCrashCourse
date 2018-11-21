import json

number = input("Whats your favourite number?")

with open('favourite_number.json', 'w') as f:
    json.dump(number, f)
    print("Is this your number of choice " + number)
