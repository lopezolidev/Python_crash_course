'''Task: 
Build a script that tracks a highly volatile inventory or connection registry.

**Concepts Covered:** List Definition (`[]`), Indexing (`0`, `-1`), f-strings with List Elements, Modifying Elements, `append()`, `insert()`, `del`, `pop()`, and `remove()`.
'''

active_targets = ['host-a','host-b', 'host-c','host-d','host-e','host-f']

print(f'We are detecting vulnerable targets, which are {active_targets[0]} and {active_targets[-1]}')

active_targets[1] = 'OFFLINE_TARGET'

print(f'We have detected an intrusion, previous host-b has changed status: {active_targets[1]}')

active_targets.insert(0, 'critical_host')
# always has an index to insert values 

active_targets.append('low_priority_target')

print(active_targets)

out = active_targets.pop()
print(f"{out} has been offloaded")

out = active_targets.pop()
print(f"{out} has been offloaded")

out = active_targets.pop()
print(f"{out} has been offloaded")

out = active_targets.pop()
print(f"{out} has been offloaded")

out = active_targets.pop()
print(f"{out} has been offloaded")

out = active_targets.pop()
print(f"{out} has been offloaded")

print(f"we're left with: {active_targets}")

del active_targets[0]
print(active_targets)

active_targets.remove('host-a')
print(active_targets)