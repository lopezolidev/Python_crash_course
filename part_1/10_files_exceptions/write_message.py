filename = "programming.txt"

with open(filename, 'w') as file_object: 
    # w = write to the file → deleting what previously had 
    file_object.write("And this is a new line in the file.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")  

with open(filename, 'a') as file_object: 
    # appending to the file, adding to what previously had
    file_object.write("And everyting started from scratch again...\n")
    number = 4
    file_object.write(str(number)) # data written to the file must be string

with open(filename) as file_object: # reads by default
    contents = file_object.read()
    print(contents)
"""
And this is a new line in the file.
And everyting started from scratch again...
4
"""