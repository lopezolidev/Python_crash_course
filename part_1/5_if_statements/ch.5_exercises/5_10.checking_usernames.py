current_users = [
    "alice", "bob", "charlie", "david", "eve"
]

new_users = [
    'Alice', 'EVE', 'Frank', 'Grace', 'Helen'
]

for new_user_name in new_users:
    if new_user_name.lower() in current_users:
        print(f"Sorry, {new_user_name} is not available, please enter a different username")
    else:
        print(f"{new_user_name} is available")
'''
Sorry, Alice is not available, please enter a different username
Sorry, EVE is not available, please enter a different username
Frank is available
Grace is available
Helen is available
'''