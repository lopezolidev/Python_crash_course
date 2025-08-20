print("typical floats situation")
print(0.1 + 0.2)
print("or...")
print(0.1 * 3)
print("or even...")
print(0.1 ** 0.1)

print(0.3 * 4)
# 1.2

print(0.44 + 7)
# 7.44

print(4 / 2)
# 2.0 ← results in a float even if the result is a whole number

print("age of the universe:", 14_000_000_000)
# age of the universe: 14000000000 ← python doesn't care if the number has underscores

# multiple assignment
x, y, z = 0, 0, 0
print(f"x: {x}, y: {y}, z: {z}")

# is this a constant?
MAX_CONNECTIONS = 5000 

# MAX_CONNECTIONS = 3 ← should never happen, because its a constant

