height = input("How tall are you? ")
height = int(height) # now the input became an integer

if height >= 48: # the comparisson can be made
    print(f"\nYou're tall enough to ride!")
else:
    print(f"\nYou'll be able to ride when you're a little older.")