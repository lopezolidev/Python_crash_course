prompt = "\nEnter your age to enter the movie theater"
prompt += "\n(Enter 'quit' to end the program. )"

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 0 or age > 100:
        print("\n\tPlease enter a valid age")
        continue

    if age < 3:
        print("\nYou have a free ticket")
    elif age < 12:
        print("\nYour ticket if $10")
    else:
        print("\nYour ticket is $15")