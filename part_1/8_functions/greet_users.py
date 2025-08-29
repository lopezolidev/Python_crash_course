def greet_users(users):
    """Print a simple greeting to each user in the list"""
    for name in users:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)