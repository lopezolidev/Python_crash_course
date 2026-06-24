'''
Concepts Covered: List Comprehensions, Array Slicing (`[start:stop]`, `[:3]`, `[-3:]`), Deep Copying via Slices (`list_b = list_a[:]`), and Direct Pointer Referencing (`list_b = list_a`).

Task: Implement efficient data initialization and inspect how Python manages list objects in memory.
'''

master_log = [i * i * i for i in range(1, 13)]
print(master_log)

first_third = master_log[:3]
print(first_third)

second_third = master_log[3:6]
print(second_third)

last_third = master_log[-3:]
#negative slicing considering that last item is never touched if indexed
print(last_third)

#true copy for master_log
cleared_log = master_log[:]
print(cleared_log)

#shared copy of master_log
shared_log = master_log
print(shared_log)

master_log.insert(3, 'XYZXYZXYZ')
print(f"master_log: {master_log}")
print(f"shared_log: {shared_log}")
print(f"cleared_log: {cleared_log}")

'''
Python tracks values in memory as a pointer reference. If two lists are copied as pointers

list_1 = list_2 

then whatever we do in one list will reflect on the other

if one list is copied through like so

list_1 = list_2[:]

then it doesn't matter what we do to each list, they will be separate in memory
'''

