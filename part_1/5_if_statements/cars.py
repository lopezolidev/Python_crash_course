cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
'''
Audi
BMW
Subaru
Toyota
'''

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
'''
Is car == 'subaru'? I predict True.
True
'''

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
'''
Is car == 'audi'? I predict False.
False
'''
