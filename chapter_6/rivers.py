rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The river " + river.title() + " flows through " + country.title() + ".")

print("\n The following rivers are including this data set.")
for river in rivers.keys():
    print(" - " + river.title())

print("\n The following countries are including this data set.")
for river in rivers.values():
    print(" - " + river.title())
