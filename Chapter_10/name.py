import json

username = input("Username: ")

filename = 'numbers.json'

with open(filename, 'w') as f_name:
    json.dump(username, f_name)
