# Present in 1st list but not in 2nd list.

l1 = [10, 20, 30]
l2 = [30, 40, 50]

l3 = [i for i in l1 if i not in l2]
print(l3)

l3 = []
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)

# [10, 20]
# [10, 20]