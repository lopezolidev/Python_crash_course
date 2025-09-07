import json

def fav_number(filename):
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        with open(filename, 'w') as f:
            number = input("What's your favorite number? ")
            json.dump(number, f)
    else:
        print(f"Your favorite number is... {fav_number}!")


filename = 'favorite_number.json'

fav_number(filename)