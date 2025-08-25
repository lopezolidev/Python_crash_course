responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompting the user for their name and response

    name = input("\nWhat's your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # storing response and name in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("\nWould you like to let another person respond? (yes / no)  ")
    if repeat == 'no':
        polling_active = False

# polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"\n{name} would like to clim {response}.")

    