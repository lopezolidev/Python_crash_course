'''

Concepts Covered: The `input()` function, Clear Multi-line Prompts, Numeric Type Conversion using `int()`, The Modulo Operator (`%`), and Basic Conditional Loops.

Task: Build an interactive triage script that evaluates user-submitted numerical identifiers.
'''

print("Hello user, please insert your ID or type 'quit' to end the program")

while True:
    prompt_msg = input('ID or quit: \n\t')
    if prompt_msg == 'quit':
        break
    prompt_msg = int(prompt_msg)
    if prompt_msg % 2 == 0:
        print(f"Node {prompt_msg} allocated to Even Routing Infrastructure.")
    else:
        print(f"Node {prompt_msg} allocated to Odd Routing Infrastructure.")

print("Exiting the program")

