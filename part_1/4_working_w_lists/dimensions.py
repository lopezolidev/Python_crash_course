rectangle = (200, 50) # this is a tuple

another_rectangle = 30, 50 # another tuple

# tuples are identified by the presence of a comma

print(rectangle) # (200, 50)
print(rectangle[0]) # 200
print(rectangle[1]) # 50

print(another_rectangle) # (30, 50)
print(another_rectangle[0]) # 30
print(another_rectangle[1]) # 50

'''
another_rectangle[0] = 80
Traceback (most recent call last):
  File "path/to/file/Python_crash_course/part_1/working_w_lists/dimensions.py", line 15, in <module>
    another_rectangle[0] = 80
    ~~~~~~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment

we cannot alter values of tuples
'''
# single element tuple
single_tuple = 3,
another_single_tuple = (7,)

print(single_tuple) # (3,)
print(another_single_tuple) # (7,)

cube_dimensions = 200, 50, 170

for dimension in cube_dimensions:
    print(dimension)
'''
200
50
170
'''

# redefining a tuple by reassigning a variable

print("Original cube dimensions:\n")
for dimension in cube_dimensions:
    print(dimension)
'''
Original cube dimensions:

200
50
170
'''
print("\n")

cube_dimensions = (300, 180, 240)

print("New cube dimensions:\n")
for dimension in cube_dimensions:
    print(dimension)
'''
New cube dimensions:

300
180
240
'''
