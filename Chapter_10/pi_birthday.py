filename = 'pi_digits.txt'

with open(filename) as file_input:
    file = file_input.readlines()

pi_lines = ''
for line in file:
    pi_lines += line.strip()

def lost():
    print("no worries")

birthday = input("Birhtday input:")
if birthday in pi_lines:
    print("great")
else:
    lost()


