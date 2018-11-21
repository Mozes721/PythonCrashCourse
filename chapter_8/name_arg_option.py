def formated_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = formated_name('john', 'smith')
print(musician)

musician = formated_name('john', 'kavagan', 'smith')
print(musician)