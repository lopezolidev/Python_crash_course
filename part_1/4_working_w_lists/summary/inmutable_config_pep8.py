'''
Concepts Covered: Tuple Definition `()`, Type Errors via Immutability, Overwriting Tuple Variables, and PEP 8 Design Rules (Line Limits, Whitespace).

Task: Secure system settings using immutable structures and evaluate structural constraints.
'''

system_dimensions = (1024, 768)

for el in system_dimensions:
    print(f"coordinate: {el}")

# system_dimensions[0] = 2048
'''
    system_dimensions[0] = 2048
    ~~~~~~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

#we must change the whole tuple to corretly change values
system_dimensions = (2048, 1080)
print(system_dimensions)

#this code follows PEP8