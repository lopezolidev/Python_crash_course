name = input("Please insert your first name: ")

filename = "guests.txt"

with open(filename, 'w') as file_object:
    file_object.write(name)

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)