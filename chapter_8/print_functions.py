def print_models(unprinted_designes,completed_design):
    while unprinted_designes:
        models = unprinted_designes.pop()
        print("Printing model " + models)
        completed_design.append(models)

def show_completed_models(completed_design):
    print("The folowing models have been printed")
    for completed in completed_design:
        print(completed)

unprinted_designes = ['iphone case', 'robot pendant', 'dodecagedron']
completed_design = []

print_models(unprinted_designes, completed_design)
show_completed_models(completed_design)