age = 18

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
# each elif statement responds to a specific condition
print(f"Your admision cost is ${price}.")