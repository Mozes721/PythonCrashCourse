while True:
    try:
        x = input("Give me first number")
        x = int(x)

        y = input("Give me second number")
        y = int(y)
    except ValueError:
        print("ValueError thrown")
    else:
        sum = x + y
        print(sum)