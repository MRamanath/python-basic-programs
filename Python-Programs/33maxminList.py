# A program to find the maximum and minimum from a list.

x = int(input('Enter how many numbers: '))
l = []
for i in range(x):
    print('Enter Number: ', end = ' ')
    l.append(int(input()))
print('The List is : ', l)

big = l[0]
small = l[0]

for m in range(1, x):
    if l[m] > big:
        big = l[m]
    if l[m] < small:
        small = l[m]
print('Big element: ', big)
print('Small element: ', small)

# Enter how many numbers: 4
# Enter Number:  23
# Enter Number:  32
# Enter Number:  11
# Enter Number:  45
# The List is :  [23, 32, 11, 45]
# Big element:  45
# Small element:  11