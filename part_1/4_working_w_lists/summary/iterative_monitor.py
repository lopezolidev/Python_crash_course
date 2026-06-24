'''
Task: Automate data generation, perform statistical checks, and inspect loop scope constraints.

Concepts Covered: The `for` loop, Loop Variable Isolation, Logical Indentation Blocks, `range()` Sequence Generation, List Aggregation Statistics (`min()`, `max()`, `sum()`), and Indentation Errors.
'''

device_ids = list(range(101, 150, 2))
print(device_ids)

for i in device_ids:
    print(f"Provisioning secure environment for Node ID: {i}")

        # print("indentation test")
        #indentation test
'''
    print("indentation test")
IndentationError: unexpected indent
'''
# Python uses whitespace block nesting rather than curly braces `{}` to determine code execution context.

min_val = min(device_ids)
max_val = max(device_ids)
sum_vals = sum(device_ids)

print(f"The min value is: {min_val} \n max value is: {max_val} \n sum value is: {sum_vals}")

