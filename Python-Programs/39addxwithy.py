# We want to add each element of 'x' with each element of 'y'.

l1 = [10, 20, 30]
l2 = [1, 2, 3]
lst = []

for i in l1:
    for j in l2:
        lst.append(i + j)
print(lst)

lst = [i + j for i in l1 for j in l2]
print(lst)

lst = [i + j for i in 'ABC' for j in 'DE']
print(lst)

# [11, 12, 13, 21, 22, 23, 31, 32, 33]
# [11, 12, 13, 21, 22, 23, 31, 32, 33]
# ['AD', 'AE', 'BD', 'BE', 'CD', 'CE']