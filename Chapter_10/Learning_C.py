text = 'python_learn.txt'

with open(text) as f:
    file = f.readlines()

for line in file:
    line = line.rstrip()
    print(line.replace('Python', 'C'))

    