import json

# Load the username, if it has been stored previously
# Otherwise, prompt for the username and store it
# Encapsulating the preceeding logic in 3 functions

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username    

def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        condition = input(f"Is {username} your correct username? ")
        if condition.lower() == 'yes' or condition.lower() == 'y': 
            print(f"Welcome back {username}!")
        else:
            real_username = get_new_username()
            print(f"We'll remember you when you come back, {real_username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()