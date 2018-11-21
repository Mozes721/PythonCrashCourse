guest = 'guest_book.txt'
print("Enter 'quit' when you are finished.")
list = []
while True:
    name = input("Your name? ")
    if name == 'quit':
        break
    else:
        with open(guest, 'a') as f:
            f.write(name + "\n")
            list.append(f)
        print("hi " + name + ", you've been added to the guest book.")

