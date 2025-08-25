sandwich_orders = [ 
    "Grilled Cheese",
    "BLT",
    "Club Sandwich",
    "Reuben",
    "Pastrami",
    "Italian Sub",
    "Philly Cheesesteak",
    "Cuban",
    "Pastrami",
    "French Dip",
    "Pastrami on Rye",
    "Pastrami",
    "Meatball Sub",
    "Pastrami",
    "Tuna Melt",
    "Pastrami",
    "Pulled Pork",
    "Pastrami",
    "Chicken Salad",
    "Egg Salad",
    "Gyro",
    "Pastrami",
    "Quesadilla",
    "Patty Melt",
    "Monte Cristo",
    "Pastrami",
    "Bánh Mì",
    "Pastrami",
]

finished_sandwiches = []
n = 1
while "Pastrami" in sandwich_orders :
    sandwich_orders.remove("Pastrami")
    print(f"\nRemoving pastrami order Nº{n}...")
    n += 1
# removing all the appearances of "pastrami"

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"\nI made your {current_sandwich} sandwich!")

    finished_sandwiches.append(current_sandwich)

print("List of finished sandwiches")

for sandwich in finished_sandwiches:
    print(sandwich)