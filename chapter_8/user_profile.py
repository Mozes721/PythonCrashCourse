def user_profile(first, last, **items):
    dict = {}
    dict['first name'] = first
    dict['last name'] = last
    for key, values in items.items():
        dict[key] = values
    return dict

a = user_profile('rick', 'johnes', location='Kansas', age=27, occupation='backend developer')
print(a)