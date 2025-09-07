"""
We want to execute the reading of a file that contains Alice in Wonderland.
What happens if such file doesn't exists? We must use try-except structre to
handle the error
"""

filename = "alice.txt"
try:
    with open(filename) as f:
        content = f.read()
    # inside the 'open' structure
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exists.")
else:
    print(content)