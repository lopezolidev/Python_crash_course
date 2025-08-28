def formatted_name(first_name, last_name,  middle_name=''):
    '''Return a full name, neatly formatted.'''
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
         full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print(musician)
# prints without a middle name, because its optional

musician = formatted_name('john', 'hooker', 'lee')
print(musician)

# infinite loop unless we signal 'q'
while True:
    print(f"\nPlease tell me your name.")
    print(f"(Enter 'q' at any time to quit)")

    f_name = input("Enter your first name. ")
    
    if f_name == 'q':
        break

    l_name = input("Enter your last name. ")
    
    if l_name == 'q':
        break

    full_name = formatted_name(f_name, l_name)
    print(f"\nHello, {full_name}!")