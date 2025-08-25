prompt = "\nEnter your pizza topping."
prompt += "\n(Enter 'quit' to end the program). "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"You added: {message} pizza topping")