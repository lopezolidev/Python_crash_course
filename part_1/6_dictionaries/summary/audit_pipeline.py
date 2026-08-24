'''
Concepts Covered: Looping Through Key-Value Pairs (`.items()`), Looping Through Keys (`.keys()`), On-The-Fly Sorted Sorting (`sorted()`), Looping Through Values (`.values()`), and Value De-duplication via `set()`.

Task: Process a collection of categorized objects using specialized loop iterators and cross-referencing logic from Chapter 5.
'''

# 1. Define a dictionary containing at least five keys representing process names and map each to an operational severity status.  Ensure at least two services share the exact same status value.

system_services = {
    'ssh' : 'nominal' ,
    'cron' : 'active' ,
    'http' : 'critical' ,
    'ftp' : 'disabled' ,
    'smtp' : 'nominal' ,
    'tcp' : 'enabled'
}

# 2. Looping pairs
for key_value in system_services.items():
    print(f"{key_value[0].title()}: {key_value[1].title()}")

print("\n")

# 3. Looping Keys & Sorting and 4. conditional verifications
for key in sorted(system_services.keys()):
    print(f"Key: {key}")
    if 'firewall' not in sorted(system_services.keys()):
        print('firewall is missing')

# 5. Looping Unique Values
for value in set(system_services.values()):
    print(f"Status: {value}")