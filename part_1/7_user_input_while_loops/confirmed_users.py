# start with users that need to be verified
# will use an empty list to store verified users
unconfirmed_users = ['alice', 'bob', 'candace']
confirmed_users = []

# verify users until there're no more unconfirmed users
while unconfirmed_users :
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# diplay all the confirmed users
print("The following users have been confirmed. ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())