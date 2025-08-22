pizzas = [ "pepperoni", "four seasons", "bacon"]
friend_pizzas = pizzas[:]
# copy of pizzas

# append a new pizza to each list
pizzas.append('4 cheese')
friend_pizzas.append('barbecue')

print("My favourite pizzas are:\n")
for pizza in pizzas:
    print(pizza)
'''
My favourite pizzas are:

pepperoni
four seasons
bacon
4 cheese
'''
print("\n")

print("My friends favourite pizzas are:\n")
for pizza in friend_pizzas:
    print(pizza)
'''
My friends favourite pizzas are:

pepperoni
four seasons
bacon
barbecue
'''