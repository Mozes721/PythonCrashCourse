file = 'python_learn.txt'
print("--- Reading in the entire file:")
with open(file) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(file) as f:
    for line in f:
        print(line.rstrip())
print("\n--- Storing the lines in a list:")
with open(file) as f:
    lines = f.readlines()

for i in lines:
    print(i.rstrip())