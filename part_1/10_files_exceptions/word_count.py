"""
This time a function that counts words will count the words of a series of text
files we send that are available in the current folder. Also we test 'silent 
failing'.
"""

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f:
            content = f.read()
        # inside the 'open' structure
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exists.")
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has an aproximate of {num_words} total words")


files = ["alice_in_wonderland.txt", "amadis_gaula.txt", "siddhartha.txt", "mobby_dick.txt"]
for file in files:
    count_words(file)
"""
The file alice_in_wonderland.txt has an aproximate of 30389 total words
The file amadis_gaula.txt has an aproximate of 85598 total words
Sorry, the file siddhartha.txt does not exists.
The file mobby_dick.txt has an aproximate of 215838 total words

w/ pass:
The file alice_in_wonderland.txt has an aproximate of 30389 total words
The file amadis_gaula.txt has an aproximate of 85598 total words
The file mobby_dick.txt has an aproximate of 215838 total words
"""

