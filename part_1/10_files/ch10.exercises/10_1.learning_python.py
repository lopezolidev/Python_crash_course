filename = "learning_python.txt"

with open(filename) as file_object:
    contents = file_object.read()
    print(f"First time: {contents.rstrip()}\n")
    # if above code is executed, ahead code cannot. The file was read already

    print("Second time: ")
    for line in file_object:
        print(line.rstrip())
    print("\n")

    lines = file_object.readlines()

print("Third time: ")
for line in lines:
    print(line.rstrip())

print("\n")
