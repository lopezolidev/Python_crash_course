import json

def whats_your_fav_number(filename):
    """Prompts the user for their favorite number and writes it to a file"""
    fav_number = input("What's your favorite number? ")

    with open(filename, 'w') as f:
        json.dump(fav_number, f)

    
def your_fav_number_is(filename):
    """Reads user favorite number from a file"""
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        print(f"Sorry, {filename} doesn't exists")
    else:
        print(f"Your favorite number is: {fav_number}")

filename = 'favorite_number.json'

whats_your_fav_number(filename)
your_fav_number_is(filename)