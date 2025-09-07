"""
Same as previous file but with a While loop
"""
while True or numerator == -1:
    try:
        numerator = input("Insert numerator: ")
        denominator = input("Insert denominator: ")
        sum = int(numerator) + int(denominator)
    except ValueError:
        print("Numerator or Denominator are not numbers")
    else:
        print(sum)
        try:
            numerator = int(input("Insert number != -1 to continue, else to break. "))
            if numerator == -1:
                break
        except ValueError:
            print("Numerator must be a number")
        else:
            continue