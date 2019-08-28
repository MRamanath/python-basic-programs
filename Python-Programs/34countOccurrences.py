# A program to count the number of occurrences of an element.

x = []
y = int(input('Enter how many numbers: '))
for i in range(y):
    print('Enter number: ')
    x.append(int(input()))
print('The list is : ', x)

s = int(input('Enter the element to count occurrences: '))
c = 0
for m in x:
    if s == m:
        c = c + 1
print('{} is occurred {} times'.format(s, c))

# Enter how many numbers: 4
# Enter number:
# 12
# Enter number:
# 12
# Enter number:
# 23
# Enter number:
# 34
# The list is :  [12, 12, 23, 34]
# Enter the element to count occurrences: 12
# 12 is occurred 2 times