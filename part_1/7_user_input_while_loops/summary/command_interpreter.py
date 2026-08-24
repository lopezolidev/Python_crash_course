'''

Concepts Covered: Active State Flags (Boolean Control Switches), The `break` Statement, and The `continue` Statement.

Task: Code a program that demonstrates the exact execution behavior differences between tracking state with a boolean flag, terminating early with `break`, and bypassing blocks with `continue`.
'''

shell_active = True

while shell_active:
    user_prompt = input("Please insert a command: \n\t")
    if user_prompt == 'clear':
        continue
        print("HELLOOOOO")
    if user_prompt == 'halt':
        print("Halting the shell")
        break
    if user_prompt == 'quit':
        shell_active = False
    print(f"{user_prompt}")

