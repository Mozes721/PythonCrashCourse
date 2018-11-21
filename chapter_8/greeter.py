def get_formated_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nEnter full name: ")
    print("\n Enter quit 'q' if want to stop the process: " )
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formated_name = get_formated_name(f_name,l_name)
    print("Hello " + formated_name)