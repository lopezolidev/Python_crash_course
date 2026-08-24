'''
Concepts Covered: Checking if a list is empty (`if list_name:`), The `in` operator, The `not in` operator, Combining `for` loops with conditional logic, and Cross-Referencing Multiple Lists.

Task: Process multiple arrays dynamically while handling edge cases and empty data structures.
'''

# 1. Define a list of blacklisted hacker group identifiers
blacklisted_identifiers = ["fancy_bear", "charming_kitten", "lazarus_group"]

# 2. Define incoming registrations with a mix of standard names, 
# an admin keyword, and a blacklisted hacker group
incoming_registrations = [
    "user_alpha88",      # Standard identifier
    "admin",             # Special administrative word
    "fancy_bear",        # Matches an item in the blacklist
    "cyber_security_9",  # Standard identifier
    "guest_account"      # Standard identifier
]

if incoming_registrations == []:
    print("Incoming registrations is empty")
else:
    for item in incoming_registrations:
        if item == 'admin' or item == 'root':
            print("Default administrative credentials detected! Structural modification required.")
        if item in blacklisted_identifiers:
            print("Registration denied: Target identity is explicitly restricted.")
        else:
            print(f"Identity {item} successfully cross-referenced and approved.")