guests = input("Welcome!")
guest = 'guest.txt'

with open(guest, 'w') as f:
    f.write(guests)
    