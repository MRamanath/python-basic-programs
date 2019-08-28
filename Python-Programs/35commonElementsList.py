# A program to find common element in two lists.

l1 = set([12, 23, 34, 45])
l2 = set([34, 45, 90, 45])

l3 = list(l1.intersection(l2))
print(l3)

# Output
# [34, 45]