'''
Concepts Covered: List of Dictionaries, Lists Nested Inside a Dictionary, and Dictionaries Nested Inside a Dictionary.

Task: Build and query a multi-tiered data structure that implements all three fundamental nesting archetypes described in the text.
'''
# 1. Archetype A (List of Dictionaries)
endpoint_cluster = []

for i in range(1, 7):
    my_dict = {'node_id': i, 'os': i*i*i}
    endpoint_cluster.append(my_dict)

for dictionary in endpoint_cluster:
    dictionary['environment'] = 'production'

print(endpoint_cluster)

# 2.Archetype B (List Inside a Dictionary)
security_profile = {
    # Standard scalar fields (strings, integers, booleans)
    "profile_name": "Tier_1_App_Defenses",
    "risk_level": "High",
    "max_login_attempts": 3,
    "mfa_required": True,
    "assigned_rules": [
        "read",          
        "write",         
        "execute",       
        "delete",        
        "admin",         
        "read_write",    
        "sudo",          
        "audit"]
}

for rule in security_profile["assigned_rules"]:
    print(f"\t assigned rule: {rule}")

# 3. Archetype C (Dictionary Inside a Dictionary)
network_map = {
    "subnet_aplha" : 
        {
            'gateway_ip': '192.168.0.1',
            'vlan_id': 0
        },
    "subnet_beta" : 
        {
            'gateway_ip': '192.168.0.129',
            'vlan_id': 1
        },
    "subnet_gamma" : 
        {
            'gateway_ip': '192.168.1.1',
            'vlan_id': 2
        }
}

for item in network_map.items():
    print(f"Name of subnet: {item[0]}")
    for key, value in item[1].items():
        print(f"\t{key}: {value}")