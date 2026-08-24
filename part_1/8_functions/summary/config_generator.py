"""
### Exercise 1: The Config Generator (Parameters, Defaults, & Returns)

**Concepts Covered:** Function Definitions (`def`), Docstrings , Positional vs. Keyword Arguments, Default Parameters, Optional Arguments (None/Empty assignments), and Returning Dictionaries.

- **Task:** Build a modular system metadata aggregator that builds and returns structural records.
    
    1. Define a function named `build_system_profile()` that accepts three mandatory positional parameters: `hostname`, `ip_address`, and `operating_system`.
        
    2. Add an optional fourth parameter named `assigned_vlan` with a default integer value of `1`.
        
    3. Add an optional fifth parameter named `service_tag` initialized to an empty string or `None`.
        
    4. Inside the function, include a descriptive docstring summarizing the expected input formats and the structural output design.
        
    5. Have the function construct and `return` an associative dictionary (from Chapter 6) containing all these parameters as properly formatted key-value pairs. If `service_tag` is provided, include it in the dictionary; if not, omit the key or handle it cleanly using a Chapter 5 conditional block.
        
    6. Execute the function at least three times down in your script to verify the return pathways:
        
        - Call it using strict positional arguments.
            
        - Call it out of order using explicit keyword arguments.
            
        - Call it with a custom `service_tag` string to verify the optional conditional block executes perfectly. Wrap each execution in a `print()` call to inspect the generated dictionary.
"""

def build_system_profile(hostname, ip_addres, operating_system, assigned_vlan=1, service_tag=None):
    """
    INPUT: 
    - 3 mandatory parameters and 2 optional parameters.
    - The former mandatory are hostname, ip_address and operating_system.
    - The latter optional are assigned_vlan and service_tag, which respectively have 1 and None as default values

    OUTPUT:
    - Associative dictionary that contains all these parameters as properly formatted key-value pairs. If `service_tag` is provided, it is included in the dictionary, so as assigned_value.
    """

    assoc_dict = {
        'hostname' : hostname ,
        'ip_address' : ip_addres ,
        'operating_system' : operating_system
    }

    if assigned_vlan != 1:
        assoc_dict['assigned_vlan'] = assigned_vlan

    if service_tag != None :
        assoc_dict['service_tag'] = service_tag

    return assoc_dict


print(build_system_profile('Albita_calvita', '172.168.242.255', 'Albita_OS', 1, 'Albita_service'))

print(build_system_profile(operating_system='Albita_OS', ip_addres='172.168.242.255',  hostname='Albita_calvita'))

print(build_system_profile(operating_system='Albita_OS', ip_addres='172.168.242.255',  hostname='Albita_calvita', service_tag=3))
