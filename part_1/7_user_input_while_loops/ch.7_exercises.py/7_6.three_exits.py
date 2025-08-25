prompt = "\nEnter your pizza topping."
prompt += "\n(Enter 'quit' to end the program). "

number_of_toppings = 0

while number_of_toppings < 10:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        number_of_toppings += 1
        print(f"You added: {message} pizza topping, you have {number_of_toppings} left")
