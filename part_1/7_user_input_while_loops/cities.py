prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter 'quit' when you are finished). "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city}")

#-----------------------------------------------------------------------------

cities = ['San Francisco', 'Caracas', 'Barquisimeto', 'Denver']
n = 0
while True:
    if n == 2:
        break # breaks the loop. Not executing following code
    print(cities[n])
    n += 1
