cubes = [ cube ** 3 for cube in range(1, 10)]

print("the first three cubes in the list are:\n")
for cube in cubes[:3]:
    print(cube)
    '''
    1
    8
    27
    '''

print("The last 3 cubes in the list of cubes are:\n")
for cube in cubes[-3:]:
    print(cube)
    '''
    343
    512
    729
    '''

print("The cubes in the middle of the list are:\n")
for cube in cubes[3:6]:
    print(cube)
    '''
    64
    125
    216
    '''

    