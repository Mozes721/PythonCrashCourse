def show_magicians(magicians):
    for magic in magicians:
        print(magic.title())


def great_magician(magicians):
    greatest_magicians = []

    while magicians:
        magician = magicians.pop()
        greatest_ones = magician + ' Greates!'
        greatest_magicians.append(greatest_ones)

    for great in greatest_magicians:
        magicians.append(great)
    return magicians


magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magician = great_magician(magicians[:])
show_magicians(great_magician)

print("\nOriginal magicians:")
show_magicians(magicians)