name = input("What's your name? ")
guest = 'guest.txt'

with open(guest, 'w') as f:
    file_object = f.write(guest)


