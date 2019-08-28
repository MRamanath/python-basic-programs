# A program to sort the list elements using bubble sort technique.

x = []
y = int(input('How many numbers: '))
for i in range(y):
    print('Enter number: ', end = '')
    x.append(int(input()))
print('The list is : ', x)

flag = False
for j in range(y-1):
    for k in range(y-j-1):
        if x[k] > x[k + 1]:
            temp = x[k]
            x[k] = x[k + 1]
            x[k + 1] = temp
            flag = True
    if flag == False:
        break
    else:
        flag = False
print('Sorted List is : ', x)

# Output
# How many numbers: 5
# Enter number: 12
# Enter number: 23
# Enter number: 2
# Enter number: 45
# Enter number: 11
# The list is :  [12, 23, 2, 45, 11]
# Sorted List is :  [2, 11, 12, 23, 45]