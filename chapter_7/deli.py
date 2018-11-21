sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []
while sandwich_orders:
    current_sandwitch = sandwich_orders.pop()
    print("I am working on your " + current_sandwitch + " sandwitch")
    finished_sandwiches.append(current_sandwitch)

print("\n")
for sandwitch in finished_sandwiches:
    print("Your " + sandwitch + " is done!")