requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # mushrooms is different than anchovies
    print("Hold the anchovies!")
# Hold the anchovies!


# -----------------------------------------------------------

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding musrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
    # this condition runs wheter or not previous conditions did
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
'''
Adding musrooms.
Adding extra cheese.

Finished making your pizza!
'''
# in an if-elif-else block this code wouldn't run


# -----------------------------------------------------------

if 'mushrooms' in requested_toppings:
    print("Adding musrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings: 
# this condition won't run, because the code stops at the fullfiling condition
    print("Adding extra cheese.")    
print("\nFinished making your pizza!")
'''
Adding musrooms.

Finished making your pizza!
'''


# -----------------------------------------------------------

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we're out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# -----------------------------------------------------------

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# Are you sure you want a plain pizza?


# -----------------------------------------------------------

available_toppings = ['mushrooms',
                      'olives',
                      'green peppers',
                      'pepperoni',
                      'pineapple',
                      'extra cheese'
                      ]

requested_toppings = ['mushrooms',
                      'french_fries',
                      'extra cheese'
                      ]

for requested_topping in requested_toppings:
    if requested_topping not in available_toppings:
        print(f"Sorry, we don't have {requested_topping}")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")    
'''
Adding mushrooms.
Sorry, we don't have french_fries
Adding extra cheese.

Finished making your pizza!
'''