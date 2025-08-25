vacations = {}

polling_active = True

while polling_active:
    # prompting the user for their name and response

    name = input("\nWhat's your name? ")
    response = input("\nIf you could visit one place in the world, where would you go? ")

    # storing response and name in the dictionary
    vacations[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("\nWould you like to let another person respond? (yes / no)  ")
    if repeat == 'no':
        polling_active = False

# polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in vacations.items():
    print(f"\n{name} would like to visit {response}.")

    