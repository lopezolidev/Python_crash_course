def read_write_file(filename, option):
    """
    Reads, appends or writes to a file. If the file doesn't exist, raises an
    exception. If such file exists, it's written to, read from or appended.
    """
    while True:
        if option == 'r':
            try:
                with open(filename) as f:
                    contents = f.read()
                    print(contents)
                break      
            except FileNotFoundError:
                    # print(f"Sorry, {filename} file does not exists.")
                    pass
                    break
        elif option == 'w':
            try:
                with open(filename, 'w') as f:
                    text = input("Insert a pet name: ")
                    if text == 'q':
                        break
                    f.write(f"{text}\n")
                    break
            except FileNotFoundError:
                # print(f"Sorry, {filename} file does not exists")
                pass
                break
        elif option == 'a':
            try:
                with open(filename, 'a') as f:
                    text = input("Insert a pet name: ")
                    if text == 'q':
                        break
                    f.write(f"{text}\n")
            except FileNotFoundError:
                # print(f"Sorry, {filename} file does not exists")
                pass
                break
        else:
            print("insert a valid option")

filename = 'dogs.txt'
option = input("Insert an option ('w', 'a', 'r'): ")
read_write_file(filename, option)