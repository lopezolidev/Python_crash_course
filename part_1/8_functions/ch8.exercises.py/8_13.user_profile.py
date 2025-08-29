# for myself
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('Sergio' , 'Lopez',
                             likes=['technology', 'sports', 'engineering'],
                             foods=['peanut butter', 'tomato', 'meat'])

print(user_profile)
# {'likes': ['technology', 'sports', 'engineering'], 
# 'foods': ['peanut butter', 'tomato', 'meat'], 
# 'first_name': 'Sergio', 
# 'last_name': 'Lopez'}