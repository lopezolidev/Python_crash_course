# 1. Simple Equality Test
# Test if the variable color is equal to the string 'blue'.
color = 'blue'
print(f"The color is:\n")
if color == 'blue':
    print('blue')
else:
    print('not blue')
# The color is:
# blue

# 2. Simple Inequality Test
# Test if the variable animal is not equal to the string 'dog'.
animal = 'parrot'
if animal != 'dog':
    print(f"An {animal} is not a dog!")
# An parrot is not a dog!

# 3. Test if the variable age is equal to the number 30.
age = 30
if age == 30:
    print("the age is exactly 30 years old")
# the age is exactly 30 years old

# 4. Case-Sensitive Equality Test
# Test if the string 'Apple' is equal to the string 'apple' without considering case.
fruit = 'Apple'

if fruit.lower() == 'apple':
    print("It's an apple")
# It's an apple
else:
    print(f"That's an {fruit} not an apple!")
# That's an Apple not an apple! ← first time

# 5. Greater Than Numerical Test
# Test if the variable score is greater than the number 85.
score = 90
if score > 85:
    print(f"{score} is greater than 85")
# 90 is greater than 85

# 6. Less Than or Equal To Numerical Test
# Test if the variable temperature is less than or equal to 25.
temperature_inside = 25
temperature_outside = 18
if temperature_inside <= 25 or temperature_outside <= 25:
    print(f"{temperature_inside} is exactly below 25, so as {temperature_outside}")
# 25 is exactly below 25, so as 18

# 7. Logical 'AND' Test
# Test if the variable a is greater than 10 AND the variable b is less than 20.
a = 12
b = 15
if a > 10 and b < 20:
    print(f"Effectively, {a} is greater than 10 and {b} is less than 20")
# Effectively, 12 is greater than 10 and 15 is less than 20

# 8. Logical 'OR' Test
# Test if the variable c is equal to 'red' OR the variable d is equal to 'green'.
c = 'blue'
d = 'green'

if c == 'red' or d == 'green':
    print(f"either {c} is 'red' or {d} is 'green'")
# either blue is 'red' or green is 'green'

# 9. Membership Test (in a list)
# Test if the string 'banana' is present in a list of fruits.
fruits = ['apple', 'lemon', 'watermelon', 'banana']
if 'banana' in fruits:
    print(f"'banana' is in fruits")
# 'banana' is in fruits

# 10. Non-Membership Test (not in a list)
# Test if the string 'car' is NOT present in a list of vehicles.
vehicles = ['warthog', 'jetski', 'boat', 'submarine', 'spacecraft', 'truck']
if 'car' not in vehicles:
    print("'car' is not present in the list of vehicles")
# 'car' is not present in the list of vehicles




