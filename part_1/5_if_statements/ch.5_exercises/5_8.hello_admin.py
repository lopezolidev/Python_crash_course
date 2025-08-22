usernames = [
#              'Jaden',
#              'Joey',
#              'Mickayla',
#              'Leila',
#              'Peter',
#              'Admin',
#              'Lindsey'
             ]
if usernames:
    for name in usernames:
        if name.lower() == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f'Hello {name}, thanks for loggin in again')
else:
    print("We need to find some users!")
'''
Hello Jaden, thanks for loggin in again
Hello Joey, thanks for loggin in again
Hello Mickayla, thanks for loggin in again
Hello Leila, thanks for loggin in again
Hello Peter, thanks for loggin in again
Hello admin, would you like to see a status report?
Hello Lindsey, thanks for loggin in again


... 
We need to find some users!
'''