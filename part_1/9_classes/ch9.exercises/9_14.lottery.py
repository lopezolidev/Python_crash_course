from random import randint, choice

my_list = ['a', 53, 16, 'c', 'w', 71, 'k', 4, 9, 13, 'z', 'r', 26, 'g', 75, 'b', 0]

print(f"Whoever that matches the folloing 4 elements will win the prize:")
first = choice(my_list)
second = choice(my_list)
third = choice(my_list)
fourth = choice(my_list)

print(f"{first} {second} {third} {fourth}")