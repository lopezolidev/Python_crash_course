filename = "programming_poll.txt"

with open(filename, 'a') as file_object:
    reason = ''
    while reason != 'q':
        reason = input("Tell me a reason you like programming: ")
        if reason != 'q':
            file_object.write(f"{reason}\n")

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)