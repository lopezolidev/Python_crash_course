name = input("Please enter your name: ")
print(f"\nHello, {name}!")
'''
Please enter your name: Sergio

Hello, Sergio!
'''

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
'''
If you tell us who you are, we can personalize the messages you see.
What is your first name? Javier

Hello, Javier!
'''

'''
>>> age = input("How old are you? ")
How old are you? 27
>>> age >= 18  →→→→ '27' instead of 27
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
'''