prompt = "\n Enter 'quit' if no more entry"
prompt += "\n Enter pizza toppings you want: "


while True:
    toppings = input(prompt)
    if toppings != 'quit':
        print("Your toppings are: " + toppings)
    else:
        break
