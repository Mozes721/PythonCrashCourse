cats_dogs = ['cats.txt', 'dogs.txt']
for filename in cats_dogs:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print("\nReading file: " + filename)
        print(contents)