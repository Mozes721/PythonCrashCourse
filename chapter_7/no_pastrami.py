sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    print("Sorry no pastrami!")
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwitch = sandwich_orders.pop()
    print("I am working on your " + current_sandwitch + " sandwitch")
    finished_sandwiches.append(current_sandwitch)

print("\n")
for sandwitch in finished_sandwiches:
    print("Your " + sandwitch + " is done!")