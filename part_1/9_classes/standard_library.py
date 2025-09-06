from random import randint, choice

print(randint(1, 6))
# 5

players = ['alba', 'milla', 'eli', 'nicole', 'agnes']
first_up = choice(players) # accepts a tuple and returns a random choice
print(first_up)
# milla