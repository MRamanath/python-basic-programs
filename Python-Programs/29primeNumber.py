# A python program to to generate prime number series.

min, max = [int(x) for x in input('Enter minimum and maximum range value : ').split()]
flag = 0
sum = 0
for i in range(min, max + 1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end = '\t')
        sum = sum + i
print('\nSum is :', sum)

# Output
# Enter minimum and maximum range value : 21 51
# 23      29      31      37      41      43      47
# Sum is : 251
