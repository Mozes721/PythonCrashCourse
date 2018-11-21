with open('pi_digits.txt') as file_reader:
    conetents = file_reader.read()
    print(conetents.rstrip(''))

file_path = '/Users/richard/Documents/LPTHW/text.txt'
with open(file_path) as file:
    for i in file:
        print(i)
