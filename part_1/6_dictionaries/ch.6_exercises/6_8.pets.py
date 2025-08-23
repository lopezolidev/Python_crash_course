pet_0 = {
    'kind' : 'fish',
    'owner' : 'Xavier'
}

pet_1 = {
    'kind' : 'dog' ,
    'owner' : 'Jennifer'
}

pet_2 = {
    'kind' : 'hamster',
    'owner' : 'Natascha'
}

pets = [pet_0, pet_1, pet_2]

# print all that we know about the pets

for pet in pets:
    print(f"\nThis is a {pet['kind']} and its owner is {pet['owner']}")
'''
This is a fish and its owner is Xavier

This is a dog and its owner is Jennifer

This is a hamster and its owner is Natascha
'''

