def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(*toppings) # outputs as a single string
    print(toppings) # outputs as a tuple


def make_pizza_2(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings: # starred expression can't be used here
        print(f"- {topping}")


def make_pizza_3(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings: # starred expression can't be used here
        print(f"- {topping}")