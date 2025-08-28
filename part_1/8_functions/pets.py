def describe_pet(pet_name, animal_type='dog'): 
    # default arguments must follow non default arguments
    '''Display information about a pet.'''
    article = 'a'
    if animal_type[0] in ('a', 'e', 'i', 'o', 'u'):
        article = 'an'

    print(f"\nI have {article} {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet('hamster', 'juil')
# describe_pet('octopus', 'kraken')
# calling the function multiple times

describe_pet(pet_name='toy', animal_type='parrot') 
# the default value is overwritten by 'parrot'
describe_pet(animal_type='parrot', pet_name='toy')
# both work the same

describe_pet(pet_name='boots')
# I have a dog
# My dog's name is Boots

describe_pet('boots')

describe_pet('goody')
describe_pet('octie')
describe_pet('albi', 'squirrel')
describe_pet('albi', animal_type='squirrel')
# all of these work perfectly fine

#-----------------------------------------------------------------------------


# causing an argument error
'''
describe_pet()
Traceback (most recent call last):
  File "path/to/file/Python_crash_course/part_1/8_functions/pets.py", line 36, in <module>
    describe_pet()
TypeError: describe_pet() missing 1 required positional argument: 'pet_name'
'''
'''
describe_pet('a', 'b', 'c')
Traceback (most recent call last):
  File "path/to/file/Python_crash_course/part_1/8_functions/pets.py", line 43, in <module>
    describe_pet('a', 'b', 'c')
TypeError: describe_pet() takes from 1 to 2 positional arguments but 3 were given
'''

