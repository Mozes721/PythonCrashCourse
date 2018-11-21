biology = '/Users/richard/Downloads/biology.txt'

with open(biology, 'r') as f:
    count = f.read()
    count = count.count('as')
    print(count)
