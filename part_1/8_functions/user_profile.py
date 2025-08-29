# arbitrary keyword arguments → creating a dictionary that accepts any key-value pair

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('Richard', 'Feynman',
                             location='Princeton',
                             field='physics')

print(user_profile)
# {'location': 'Princeton', 'field': 'physics', 
# 'first_name': 'Richard', 'last_name': 'Feynman'} 