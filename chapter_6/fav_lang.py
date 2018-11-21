fav_lang = {
    'jen': ['python', 'c'],
    'sarah': ['c', 'java'],
    'edward': ['ruby', 'c'],
    'phil': ['python', 'C#']
}
friends = ['phil', 'jen']
for name, lang in fav_lang.items():
    print(name.title() + "---")
    for languages in lang:
        print("\t" + languages.title())


