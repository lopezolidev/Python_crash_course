'''
Task: Intentionally trigger and diagnose runtime constraints to ensure defensive coding.

Concepts Covered: Index Errors, Indexing Empty Lists, and Traceback Diagnostics.
'''

# simple_list = ['A', 'B', 'C']
# print(f"Accessing 4th element: {simple_list[3]}")
'''
    print(f"Accessing 4th element: {simple_list[3]}")
                                    ~~~~~~~~~~~^^^
IndexError: list index out of range
'''

# empty_list = []
# print(f"{empty_list[-1]}")
'''
    print(f"{empty_list[-1]}")
             ~~~~~~~~~~^^^^
IndexError: list index out of range
'''

'''
To access the Nth element of a list, you must index the N-1 number

my_list = [A, B, C, D]

A is 1st element
B is 2nd element
C is 3rd element
D is 4th element

my_list[2] = C

And indexing -1 catches the end of the list:
my_list[-1] = D

Negative indexing serves as indexing from last to first starting from -1 to -(length)
'''


