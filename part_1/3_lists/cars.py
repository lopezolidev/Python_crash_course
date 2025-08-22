cars = ["bmw", "subaru", "toyota", "kia"]

cars.sort()
# this method affects the original order of the list

print(cars)
# ['bmw', 'kia', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars)
# ['toyota', 'subaru', 'kia', 'bmw']

covenant_vehicles = [
    "Ghost",
    "Banshee",
    "Wraith",
    "Revenant",
    "Spectre",
]

print("Original covenant vehicles list: ")
print(f"\n {covenant_vehicles}")

print("\nNow it looks revers sorted: ")
print(sorted(covenant_vehicles, reverse=True))
# doesn't affect the original list. We can sort it reversed

print("\nOriginal list again")
print(covenant_vehicles)

# reversing the order of a list

covenant_vehicles.reverse()
# affects the original list
print("\nReversed list:")
print(covenant_vehicles)

# length of a list
print(f"Length of covenant vehicles list: {len(covenant_vehicles)}")

