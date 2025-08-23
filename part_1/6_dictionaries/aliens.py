alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
'''
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
'''

# creating aliens iteratively, appending them to a list and then showing a few

# empty list of aliens
aliens = []

# iterative creation of aliens and appending them to list
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5}
    aliens.append(new_alien)

# making the first 3 aliens yellow and medium fast
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# showing 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# number of aliens created
print(f"Total number of aliens: {len(aliens)}")
'''
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
...
30
'''

# attempting a hashmap
# number_aliens = {}

# for alien in aliens:
#     if number_aliens[alien] == None:
#         number_aliens[alien] = 1
#     else:
#         number_aliens[alien] += 1

# print(number_aliens)