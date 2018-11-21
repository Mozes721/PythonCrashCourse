def get_formated_name(first_name, last_name='Kamasaki'):
    full_name = first_name + ' ' + last_name
    print("So your full name is " + full_name)
    return full_name.title()

get_formated_name('Robert')
message = get_formated_name('john', 'smith')
print(message)
