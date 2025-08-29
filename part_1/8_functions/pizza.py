def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(*toppings) # outputs as a single string
    print(toppings) # outputs as a tuple

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("----------------------------------------------------------------------")

def make_pizza_2(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings: # starred expression can't be used here
        print(f"- {topping}")

# make_pizza_2('pepperoni')

# make_pizza_2('mushrooms', 'green peppers', 'extra cheese')
# Making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

# make_pizza_2(('mushrooms', 'green peppers', 'extra cheese'))
# Making a pizza with the following toppings:
# - ('mushrooms', 'green peppers', 'extra cheese') ← prints a sole tuple

print("----------------------------------------------------------------------")

# if mixing positional and arbitrary arguments, the latter must be put at the end
def make_pizza_3(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings: # starred expression can't be used here
        print(f"- {topping}")

# make_pizza_3(12, 'mushrooms', 'green peppers', 'extra cheese')
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

# make_pizza_3(16, 'mushrooms', 'extra cheese')
# Making a 16-inch pizza with the following toppings:
# - mushrooms
# - extra cheese