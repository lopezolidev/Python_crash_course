def nb_year(p0, percent, aug, p):
    # your code
    percent = percent / 100.0

    count = 0
    
    while p0 <= p:
        p0 += p0*percent + aug
        p0 = int(p0)
        count += 1
        
    return count

print(nb_year(1500, 5, 100, 5000))