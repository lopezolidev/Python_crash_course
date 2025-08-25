sandwich_orders = [ 
    "Grilled Cheese",
    "BLT",
    "Club Sandwich",
    "Reuben",
    "Italian Sub",
    "Philly Cheesesteak",
    "Cuban",
    "French Dip",
    "Pastrami on Rye",
    "Meatball Sub",
    "Tuna Melt",
    "Pulled Pork",
    "Chicken Salad",
    "Egg Salad",
    "Gyro",
    "Quesadilla",
    "Patty Melt",
    "Monte Cristo",
    "Bánh Mì"
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"\nI made your {current_sandwich} sandwich!")

    finished_sandwiches.append(current_sandwich)

print("List of finished sandwiches")

for sandwich in finished_sandwiches:
    print(sandwich)