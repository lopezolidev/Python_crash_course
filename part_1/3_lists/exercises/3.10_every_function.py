places_things_elements = [
    "Mount T'Kao",
    "Khartana River",
    "New Mombasa",
    "Voi",
    "Cleveland",
    "Cascadia",
    "Corinth",
    "Castile",
    "Kenya",
    "United States",
    "UNSC (United Nations Space Command)",
    "Covenant",
    "Forerunners",
    "Flood",
    "Banished",
    "Prometheans",
    "Insurgents",
    "Sangheili",
    "Jiralhanae",
    "Forerunner",
    "Human (English, Russian, etc.)",
    "Kig-Yar",
    "Warthog",
    "Scorpion",
    "Pelican",
    "Phantom",
    "Banshee",
    "Wraith",
    "Phaeton",
    "Scarab",
    "Earth",
    "Reach",
    "Harvest",
    "Onyx",
    "Eridanus II",
    "Sanghelios",
    "Te"
]

print(f"We're located in {places_things_elements[1].title()}\n")
print(f"This planet is known as {places_things_elements[-3].upper()}\n")
print(f"That vehicle is called {places_things_elements[-11].lower()}\n")

popped_element = places_things_elements.pop()
print(f"The popped element is {popped_element}\n")

print(f"Now the list has length of {len(places_things_elements)}\n")

specific_popped_element = places_things_elements.pop(4)
print(f"{specific_popped_element} has been popped out from the list\n")

new_vehicle = "Cyclops"
places_things_elements.insert(7, new_vehicle)
print(f"{new_vehicle} has been added to the list\n")

new_halo_ring = "Alpha Halo (Installation 04)"
places_things_elements.append(new_halo_ring)
print(f"We've adde a new location, it is called {places_things_elements[-1]}\n")

del places_things_elements[13]
print(f"The flood has been deleted from the species. The new length of the list is of {len(places_things_elements)}\n")

print(sorted(places_things_elements))
print("\n")
print(sorted(places_things_elements, reverse=True))
print("\n")

places_things_elements.reverse()

print(places_things_elements)

print("\n")

places_things_elements.sort()
print(places_things_elements)

print("\n")

places_things_elements.sort(reverse=True)
print(places_things_elements)

# print(places_things_elements[37])
'''
Traceback (most recent call last):
  File "path/to/file/Python_crash_course/part_1/lists/exercises/3.10_every_function.py", line 83, in <module>
    print(places_things_elements[37])
          ~~~~~~~~~~~~~~~~~~~~~~^^^^
IndexError: list index out of range
'''