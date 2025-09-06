from random import randint, choice

my_list = ['a', 53, 16, 'c', 4, 'w', 71, 'k', 4, 9, 13, 'z', 'r', 26, 'g', 75, 'b', 0]

winning_ticket = [9, 'w', 'a', 4]

count = 0

while True:
    first = choice(my_list)
    second = choice(my_list)
    third = choice(my_list)
    fourth = choice(my_list)
    
    cond1 = first == winning_ticket[0]
    cond2 = second == winning_ticket[1]
    cond3 = third == winning_ticket[2]
    cond4 = fourth == winning_ticket[3]

    if cond1 and cond2 and cond3 and cond4:
        print("LOTTO!!!")
        print(f"Count: {count}")
        break
        """
        LOTTO!!!
        Count: 11855
        """
    else:
        count += 1
