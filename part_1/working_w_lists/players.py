players = [
    "Alba",
    "Eli",
    "Ale",
    "Andrea",
    "Jenn",
    "Laura",
    "Sara"
]

print(players[:]) # ['Alba', 'Eli', 'Ale', 'Andrea', 'Jenn', 'Laura', 'Sara']
print(players[1:]) # ['Eli', 'Ale', 'Andrea', 'Jenn', 'Laura', 'Sara']
print(players[2:]) # ['Ale', 'Andrea', 'Jenn', 'Laura', 'Sara']
print(players[2:4]) # ['Ale', 'Andrea']
print(players[:3]) # ['Alba', 'Eli', 'Ale'] up to the second_index - 1


# using backwards notation

print(players[-3:-1]) # ['Jenn', 'Laura']
print(players[-3:]) # ['Jenn', 'Laura', 'Sara']
print(players[2:-2]) # ['Ale', 'Andrea', 'Jenn'] from the element at index 2 up until the last 2 elements

# using a third index to signal step
print(players[:4:2]) # ['Alba', 'Ale']

print(players[::3]) # ['Alba', 'Andrea', 'Sara']

print(players[:-3: 2]) # ['Alba', 'Ale']



