numbers = list(range(5))
print(numbers)

print(range(0,5))
#range(0, 5)

for value in range(1,5):
    print(value)
    '''
    1
    2
    3
    4
    '''

for value in range(0, 5):
    print(value)
    '''
    0
    1
    2
    3
    4
    '''

for value in range(1, 6):
    print(value)
    '''
    1
    2
    3
    4
    5
    
    prints starting from the first number but stops at the second without printing it
    '''

for value in range(6): # returns the numbers from 0 to argument - 1
    print(value)
    '''
    0
    1
    2
    3
    4
    5
    '''
# using the 'list()' function to convert a range into a list

numbers = list(range(1,6))
print(numbers)
# [1, 2, 3, 4, 5]

