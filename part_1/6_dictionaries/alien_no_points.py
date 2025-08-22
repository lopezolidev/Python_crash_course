alien_0 = {
    'color' : 'green',
    'speed' : 'slow'
}
'''
print(alien_0['points'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'points'
'''

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
# No point value assigned

point_value_2 = alien_0.get('points')
print(point_value_2)
# None ← happens when no second argument is passed