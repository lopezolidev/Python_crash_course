def sort_by_length(arr):
    return sorted(arr, key=len)

arg = ["i", "to", "beg", "life"]

print(sort_by_length(arg))