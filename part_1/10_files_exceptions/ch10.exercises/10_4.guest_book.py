filename = "guest_book.txt"

with open(filename, 'a') as file_object:
    count = 0
    while count < 3:
        name = input("Please insert your name: ")
        greet = f"Greetings {name}!"
        file_object.write(f"{greet}\n")
        count += 1 # when 3 peoeple inserted their names, the task is completed

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)