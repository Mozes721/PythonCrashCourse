from chapter_11.name_function import get_formated_name

print("Enter 'q' at any time to quit")
while True:
    first = input("\nPlease give a first name: ")
    if first == 'q':
        break
    second = input("\nPlease give a first name: ")
    if second == 'q':
        break
    formated_names = get_formated_name(first, second)

    print("So the formatted name is  " + formated_names)