fileopen = 'pi_digits.txt'
with open(fileopen) as filename:
    lines = filename.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))