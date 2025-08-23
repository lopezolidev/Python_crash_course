person_0 = {
    'first_name' : 'Alba',
    'last_name' : 'Bolivar',
    'age' : 19 ,
    'city' : 'Caracas'
}

person_1 = {
    'first_name' : 'Juan',
    'last_name' : 'Bessemberg',
    'age' : 34 ,
    'city' : 'Guatire'
}

person_2 = {
    'first_name' : 'Grisbelis',
    'last_name' : 'Rodriguez',
    'age' : 20 ,
    'city' : 'La Guaira'
}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Hi, my name is {full_name}, I'm {person['age']} years old, and "
          f"I live in {person['city'].title()}")
'''
Hi, my name is Alba Bolivar, I'm 19 years old, and I live in Caracas
Hi, my name is Juan Bessemberg, I'm 34 years old, and I live in Guatire
Hi, my name is Grisbelis Rodriguez, I'm 20 years old, and I live in La Guaira
'''