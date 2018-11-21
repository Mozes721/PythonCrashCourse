prompt = "How old are you? "
prompt += "\n Enter 'quit' if your finished"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age <= 3:
        print("its free!")
    elif age >= 3 and age <= 12:
        print("the ticket is 10$")
    else:
        print("15$ price")
