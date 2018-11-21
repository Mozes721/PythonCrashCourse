unprinted_designes = ['iphone case', 'robot pendant', 'dodecagedron']
completed_design = []

while unprinted_designes:
    finished_design = unprinted_designes.pop()
    print("Printing model " + finished_design)
    completed_design.append(finished_design)

print("The folowing models have been printed")

for finished in completed_design:
    print(finished)

    