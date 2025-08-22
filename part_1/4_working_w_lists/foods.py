my_foods = [ "pizza", "carrot cake", "bittersween chicken"]

my_friends_foods = my_foods[:]
# making a 'slice-copy'

my_foods.append('cannoli')
my_friends_foods.append('ice cream')

print(f"My favourite foods are:\n{my_foods}") 
'''
My favourite foods are:
['pizza', 'carrot cake', 'bittersween chicken', 'cannoli']
'''

print("My favourite foods are:\n")
for food in my_foods:
    print(food)

print("\n")
'''
My favourite foods are:

pizza
carrot cake
bittersween chicken
cannoli
'''

print(f"My friend favourite foods are:\n{my_friends_foods}")
'''
My friend favourite foods are:
['pizza', 'carrot cake', 'bittersween chicken', 'ice cream']
'''

print("My friends favourite foods are:\n")
for food in my_friends_foods:
    print(food)

print("\n")
'''
My friends favourite foods are:

pizza
carrot cake
bittersween chicken
ice cream
'''


# variables that store lists are pointers. 
# If we equal them will result that both variables point to the same list

my_other_friend_foods = my_foods 
# both variables point to the same array

my_foods.append('fried fish')
my_other_friend_foods.append('tomato soup')

print(f"My favourite foods are:\n{my_foods}") 
'''
My favourite foods are:
['pizza', 'carrot cake', 'bittersween chicken', 'cannoli', 'fried fish', 'tomato soup']
'''

print(f"My other friend favourite foods are:\n{my_other_friend_foods}")
'''
My other friend favourite foods are:
['pizza', 'carrot cake', 'bittersween chicken', 'cannoli', 'fried fish', 'tomato soup']
'''

print("\n")

print("My other friend favourite foods are:\n")
for food in my_other_friend_foods:
    print(food)
'''
My other friend favourite foods are:

pizza
carrot cake
bittersween chicken
cannoli
fried fish
tomato soup
'''
