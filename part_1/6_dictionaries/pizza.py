pizza = {
    'crust' : 'thick' ,
    'toppings' : ['mushrooms', 'extra cheese']
}

# summarizing the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following ingredients:")

# printing the toppings 
for topping in pizza['toppings']:
    print("\t" + topping)

