import json

filename = 'numbers.json'

with open(filename) as f_read:
    username = json.load(f_read)
    if username == 'Richard':
        print("Welcome back " + username)
    else:
        print("Not in the system")