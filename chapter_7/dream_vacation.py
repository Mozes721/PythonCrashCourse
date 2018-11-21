name_promt = "\nWhats your name?"
vacation_promt = "\nWhats your dream vacation destination"
continue_or_not = "\nWhould you like to continue"

responces = {}

while True:
    name = input(name_promt)
    vacation = input(vacation_promt)

    responces[name] = vacation

    repeat = input(continue_or_not)
    if repeat != "yes":
        break

print("\n--- Results ---")
for name, vacation in responces:
    print(name.title() + " would like to visit " + vacation.title() + ".")