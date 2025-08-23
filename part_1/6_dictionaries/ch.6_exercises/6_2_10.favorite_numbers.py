favorite_numbers = {
    'Xavier' : list(range(0, 30, 7)),
    'Jacqueline' : list(range(0,30, 5)) ,
    'Alba' : list(range(0, 30, 3)) ,
    'George' : list(range(0,30,9))
}

print(f"Xavier's favorite numbers are:")
for number in favorite_numbers['Xavier']:
    print(f"\t {number}")
'''
Xavier's favorite numbers are:
         0
         7
         14
         21
         28
'''

print(f"Jacqueline's favorite numbers are:")
for number in favorite_numbers['Jacqueline']:
    print(f"\t {number}")
'''
Jacqueline's favorite numbers are:
         0
         5
         10
         15
         20
         25
'''


print(f"Alba's favorite numbers are:")
for number in favorite_numbers['Alba']:
    print(f"\t {number}")
'''
Alba's favorite numbers are:
        0
        3
        6
        9
        12
        15
        18
        21
        24
        27
'''

print(f"George's favorite numbers are:")
for number in favorite_numbers['George']:
    print(f"\t {number}")
'''
George's favorite numbers are:
        0
        9
        18
        27
'''
