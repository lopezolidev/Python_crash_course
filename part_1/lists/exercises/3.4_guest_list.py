guest_list = [
    "Xavier",
    "Jacqueline",
    "Albany",
    "Luis",
    "Cal",
    "Alejandra",
    "Vanessa",
    "Charles"
]

print(f"Hello {guest_list[-1]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-2]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-3]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-4]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-5]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-6]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-7]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-8]}, I'd like to invite you to dinner")

popped_guest = guest_list.pop(6)

print(f"Looks like {popped_guest.title()} can't make it")

new_guest = 'Saree'

guest_list.insert(6, new_guest)

print(f"We have a new guest! Please, welcome {guest_list[6]}")

print(guest_list)


print("Dear guests, we've found a bigger dinner table! We can invite 3 more people")

guest_list.insert(0, 'Dayannis')
guest_list.insert(4, 'Nicole')
guest_list.append('Oliver')

print(f"Hello {guest_list[-1]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-2]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-3]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-4]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-5]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-6]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-7]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-8]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-9]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-10]}, I'd like to invite you to dinner")

print(f"Hello {guest_list[-11]}, I'd like to invite you to dinner")

print("Looks like the new dinner table won't arrive on time")

guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop(2)
guest_list.pop(0)

print(guest_list)

print(f"{guest_list[0]} and {guest_list[1]}, you're still invited")

del guest_list[0]
del guest_list[0]

print(guest_list)


