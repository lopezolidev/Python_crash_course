'''
**Task:** Manage and audit a collection of unstructured chronological or data tracking entries.

**Concepts Covered:** Permanent Sorting (`sort()`), Reverse Permanent Sorting (`sort(reverse=True)`), Temporary Sorting (`sorted()`), Reversing Order (`reverse()`), and Finding Length (`len()`).
'''

locations = ["Tokyo", "Antarctica", "New York", "London", "Cairo"]
print(f"Current list: {locations}")

#sorting temporarily
print(f"In alphabetical (temporary) order: {sorted(locations)}")

#reversing the order of the list
locations.reverse()

print(f"Reversed list: {locations}")

#re-reversing the list
locations.reverse()
print(f"Re-reversed list: {locations}")

#sorting permanently
locations.sort()
print(f"Sorted list permanently: {locations}")

#sorting backwards
locations.sort(reverse=True)
print(f"Sorting list backwards: {locations}")

#printing size of list wrapped in-line
print(f"Audit complete. Total elements structurally tracked: {len(locations)}.")