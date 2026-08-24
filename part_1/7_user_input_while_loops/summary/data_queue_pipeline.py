'''
Concepts Covered: Using `while` loops to move items from one list to another, Removing all occurrences of a specific item from a list, Populating a dictionary dynamically with user input, and Interactive multi-stage polling loops.

Task: Simulate a data processing pipe that cleans a queue, transfers elements safely, and indexes the records inside an associative dictionary mapping.
'''

incoming_buffer = [
    'task_alpha', 
    'corrupted', 
    'task_beta', 
    'corrupted', 
    'task_gamma'
    ]

while 'corrupted' in incoming_buffer:
    incoming_buffer.remove('corrupted')
print(incoming_buffer)

processed_queue = []

# while incoming_buffer is not []: <- 'is' compares objects in memory, the actual identity
#     popped = incoming_buffer.pop()
#     print(popped)
#     processed_queue.append(popped)

while incoming_buffer: # while incoming_buffer still has elements
    popped = incoming_buffer.pop()
    print(popped)
    processed_queue.append(popped)

print(f"Incoming buffer: {incoming_buffer}")
print(f"processe queue: {processed_queue}")


assigned_registry = {}

while True:    
    key = input("Please insert your name: \t")
    val = int(input("Please insert your system access role: \t"))
    assigned_registry[key] = val

    confirmation = input("Register another entity? (yes/no): ")
    if confirmation != "yes" :
        break

print(assigned_registry)


