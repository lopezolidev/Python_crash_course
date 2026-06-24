name = "\n\t  aDa LOVeLaCE  "
user_role = "     \n\n\n   reD  TeAMeR   "
 
name = name.lstrip()
name = name.rstrip()
# print(name)

user_role = user_role.lstrip()
user_role = user_role.rstrip()
# print(user_role)

name = name.title()
# print(name)

user_role = user_role.upper()
# print(user_role)

greeting_message = f"Hello, {name}, you signed in as {user_role}."

print(greeting_message)

# formatting strings improves legibility, clarity and ease of use
