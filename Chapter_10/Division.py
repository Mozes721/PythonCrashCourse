print("Give me two numbers")
print("Enter 'q' to quit")

while True:
    first = input("Enter first number: ")
    if first == 'q':
        break
    second = input("Enter first number: ")
    if second == 'q':
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("Cant divide!")
    else:
        print(answer)