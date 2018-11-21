responses = {}

polling_active = True

while polling_active:
    name = input("\n Whats your name? ")
    response = input("Which mountain would you like to climb some day? ")

    responses[name] = response

    repeat = input("Whould you like to let another person respond? (yes/no")
    if repeat == 'no':
        polling_active = False
print("\n ---Pool Results---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
