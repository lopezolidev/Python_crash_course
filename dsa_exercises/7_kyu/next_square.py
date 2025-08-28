def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if (sq ** 0.5) % 1 > 0.0:
        return -1
    else :
        return int((((sq ** 0.5) + 1) ** 2))

print(find_next_square(81))