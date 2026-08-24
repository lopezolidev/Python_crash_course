"""
### Exercise 2: The Queue Pipeline Manager (Reference Mutation & Parameter Unpacking)

**Concepts Covered:** Passing Lists to Functions, Modifying Lists In-Place, Preventing Mutation via Slicing `[:]`, Arbitrary Positional Arguments (`*args`), and Arbitrary Keyword Arguments (`kwargs`).

- **Task:** Build a function engine that processes dynamic arrays and handles un-structured parameter lists.
    
    1. **Part A (Array Reference Management):** Write a function named `process_queue()` that takes two arguments: a list of `pending_tasks` and an empty list of `completed_tasks`. Inside, write a `while` loop (from Chapter 7) that pops tasks from the pending list and appends them to the completed list, printing an update for each action.
        
    2. Define a master list containing four task strings. Run `process_queue()` by passing a **slice copy** (`[:]`) of your master list as the first parameter.
        
    3. Print both the master list and the completed list right after execution. Add an inline comment explaining why the master list remained fully un-mutated despite being run through an in-place loop.
        
    4. **Part B (Dynamic Argument Unpacking):** Write a separate function named `log_incident()` that accepts a mandatory positional argument `severity`, an arbitrary number of positional elements using `*args`, and an arbitrary number of key-value assignments using `kwargs`.
        
    5. Inside `log_incident()`, print out the elements packed into `*args` as a tuple and iterate through the keys/values trapped inside `kwargs`. Call this function with a single line of code that passes a severity integer, three separate target names as raw positional parameters, and two specific flags like `status="down"` and `node=4` as trailing keyword parameters.
    """

# part A
def process_queue(pending_tasks, completed_tasks):
    while len(pending_tasks) != 0 :
        el = pending_tasks.pop()
        completed_tasks.insert(0, el)
        print(f'pending tasks: {pending_tasks} \ncompleted_tasks: {completed_tasks}\n')

    return completed_tasks

master_list = ['task 1', 'task 2', 'task 3', 'task 4', 'task 5']
sliced_list = master_list[0:3]
print(sliced_list)

processed_list = process_queue(sliced_list, [])
print(f"Master list: {master_list}, and processed list {processed_list}.\nMaster list remains un-mutated because a copy in memory gets created before passing into the in-place loop")

def log_incident(severity, *args, **kwargs):
    if args:
        print("Details:")
        for detail in args:
            print(f"- {detail}")
            
    if kwargs:
        print("Error Structure:")
        for k,v in kwargs.items():
            print(f"{k} : {v}")

    # Avoid mutating kwargs directly
    return {"severity": severity, "details": list(args), **kwargs}

# Positional arguments MUST come before keyword arguments
log_incident('Red', 'a', 'b', 'c', 'd', 'e', status='down', node=4)