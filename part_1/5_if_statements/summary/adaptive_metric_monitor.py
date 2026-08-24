'''
Simple `if` statements, The `if-else` block, The `if-elif-else` multi-stage chain, and Multiple Independent `if` statements.

Code two distinct monitoring blocks to understand when to terminate a evaluation chain early versus when to check every condition sequentially.
'''

# Part A
system_load = 82

if system_load < 50:
    print("System load: Nominal")
elif system_load in range(50, 80):
    print("System load: Elevated")
else:
    print("System load: Critical - Action Required")

# Part B
active_flags = ['disk_full', 'unauthorized_ip', 'kernel_outdated']

if 'disk_full' in active_flags:
    print("warning: must clear space")

if 'unauthorized_ip' in active_flags:
    print("alert: high-priority connection")

if 'kernel_outdated' in active_flags:
    print("maintenance notice")

# an if-elif-else chain would fail above test. It's not a sequential check, only one condition must be met not many

