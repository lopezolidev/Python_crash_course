alien_0 = {
    'color': 'green',
    'points': 5
}

# adding more key-value pairs to the alien dict
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)
# {'color': 'green', 'points': 5, 'x-position': 0, 'y-position': 25}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
# You just earned 5 points!

print(alien_0['color']) # green
print(alien_0['points']) # 5



'''
simple_dict ='color' : 'yellow'
File "<stdin>", line 1
    simple_dict ='color' : 'yellow'
                         ^
SyntaxError: invalid syntax → dictionaries need braces 
'''

simple_dict = {'color' : 'yellow'}

# ----------------------------------------------------------------------------

alien_0 = {} 
alien_0['color'] = 'red'
alien_0['points'] = 20
print(alien_0)
# {'color': 'red', 'points': 20}

print(f"The alien is {alien_0['color']}")
# The alien is red

alien_0['color'] = 'yellow'
print(f"The alien color is now {alien_0['color']}")
# The alien color is now yellow

# ----------------------------------------------------------------------------

alien_0 = {
    'x-position' : 0,
    'y-position' : 25,
    'speed' : 'fast'
}
print(f"Original position: {alien_0['x-position']}")
# Original position: 0

# moving the alien to the right
# determining how far to move the alien based on its curren speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# new_position = old_position + increment
alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New position: {alien_0['x-position']}")
# New position: 3

# ----------------------------------------------------------------------------

alien_0 = {
    'color' : 'green',
    'points' : 5
}
print(alien_0)
# {'color': 'green', 'points': 5}

del alien_0['color']
print(alien_0)
# {'points': 5}

