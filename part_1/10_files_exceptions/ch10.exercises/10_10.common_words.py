"""
Count the number of the word 'the' and 'the ' in a given text
"""
def count_words(filename):
    """Count the approximate number of words in a file."""
    thes = 0
    try:
        with open(filename) as f:
            content = f.readlines()
            for line in content:
                thes += int(line.lower().count('the '))
        # inside the 'open' structure
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exists.")
        pass
    else:
        print(f"The file {filename} has an aproximate of {thes} total 'the' 's")

files = ["../alice_in_wonderland.txt", "../amadis_gaula.txt", "../siddhartha.txt", "../mobby_dick.txt"]
for file in files:
    count_words(file)
"""
The file ../alice_in_wonderland.txt has an aproximate of 2582 total 'the' 's
The file ../amadis_gaula.txt has an aproximate of 7625 total 'the' 's
The file ../mobby_dick.txt has an aproximate of 20139 total 'the' 's
"""