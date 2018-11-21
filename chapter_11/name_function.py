def get_formated_name(first,second, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + second
    else:
        full_name = first + ' ' + second
    return full_name.title()

