def build_person(first_name, last_name, age=None):
    '''Return a dictionary with information about a person'''
    person = {'first': first_name,
              'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', 27)
print(musician)
# using the positional argument of age

musician = build_person( last_name='hendrix', age=27, first_name='jimi',)
print(musician)
# keyword arguments and builds the same person
