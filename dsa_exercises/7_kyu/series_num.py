def series_sum(n):
    if n == 0 :
        return "0.00"

    total_sum = 0.0
    
    for i in range(n):
        total_sum += 1 /(1 + 3*i)

    # formatting the output with f-strings
    return f"{total_sum:.2f}"

print(series_sum(59))