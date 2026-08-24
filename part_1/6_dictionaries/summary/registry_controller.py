'''
Concepts Covered: Defining Dictionaries, Accessing Values via Keys, Adding/Modifying Key-Value Pairs, Removing Data (`del`), and Error-Resilient Lookups with the `.get()` Method.

Task: Build a program that initializes and mutates a single-item data object while handling missing information safely.
'''
# 1. Define a dictionary containing three initial key-value pairs
target_node = {
    'hostname': 'alpha_tango',
    'ip_address': '192.168.175.201',
    'status': True
}

# 2. Print out the node's current IP address by directly referencing its key inside a formatted f-string.
print(f"Node's current IP address: {target_node['ip_address']}")
# Node's current IP address: 192.168.175.201

# 3. Add a new key-value pair to the dictionary representing its `'port'` configuration.
target_node['port'] = 22
target_node['status'] = 'active'

print(f"Current target node stats: {target_node}")
# Current target node stats: 
# {'hostname': 'alpha_tango', 
# 'ip_address': '192.168.175.201', 
# 'status': 'active', 
# 'port': 22}

# 4. Use the `del` statement to permanently purge the `'ip_address'` key from the dictionary.
del target_node['ip_address']

print(f"Current target node stats: {target_node}")
# Current target node stats: 
# {'hostname': 'alpha_tango', 
# 'status': 'active', 
# 'port': 22}

# 5. The Safe Retrieval Test of an inexistent key
# print(f"Special key retrieval: {target_node['encryption_type']}")
'''
    print(f"Special key retrieval: {target_node['encryption_type']}")
                                    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'encryption_type'
'''

# 6. lookup with the `.get()` method
print(f"Special key retrieval: {target_node.get('encryption_type', 'Not Configured')}")
# Special key retrieval: Not Configured
# a second argument to the 'get()' function changes the None answer to Not Configured
