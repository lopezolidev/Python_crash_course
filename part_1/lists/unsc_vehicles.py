unsc_vehicles = [
    "Warthog",
    "Mongoose",
    "Scorpion",
    "Pelican",
    "Wasp",
    "Hornet",
    "Falcon",
    "Mantis",
    "Elephant",
    "Grizzly",
    "Cobra",
    "Sabre",
]

popped_vehicle = unsc_vehicles.pop()
message = f"The {popped_vehicle.title()} is a space fighter used for dogfights and atmospheric combat."

print(unsc_vehicles)
print(message)

unsc_vehicles[0] = 'Ghost'

print(unsc_vehicles)

forerunner_vehicles = []

forerunner_vehicles.append("Phaeton")
forerunner_vehicles.append("Warden Eternal's 'Body'")
forerunner_vehicles.append("War Sphynx")
# inserts at the end of the list, like stacking

print(forerunner_vehicles) 

forerunner_vehicles.insert(2, "Harrier")
# inserting at postion 2 the 'Harrier'
# all the elements from the list sift to the right
print(forerunner_vehicles)

del forerunner_vehicles[3]
# removing last element from the list
print(forerunner_vehicles)

popped_forerunner_vehicle = forerunner_vehicles.pop(2)
# when we send the index to the pop() method we extract that element from the list
print(forerunner_vehicles)
print(f"The {popped_forerunner_vehicle.title()} is a class of combat aircraft, known for its speed and agility.")

# if we want to remove an element by its value but we ignore the index, we use 'remove' method
'''
removed_forerunner_vehicle = forerunner_vehicles.remove('Phaeton')
print(removed_forerunner_vehicle)
None
'''
not_available = 'Phaeton'
forerunner_vehicles.remove('Phaeton')
# only removes the first occurence (from left to right) of that value

print(forerunner_vehicles)
print(f"\n a {not_available.title()} is not available in this halo ring")


