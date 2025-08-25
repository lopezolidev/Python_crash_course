# message  = input("Tell me something and I will repeat it back to you: ")
# print(message)
'''
Tell me something and I will repeat it back to you: Hello everyone
Hello everyone
'''
#------------------------------------------------------------------------------

prompt  = "\nTell me something and I will repeat it back to you: "
prompt += "\n Enter 'quit' to finish the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else :
        print(message)
    # checking using a flag
