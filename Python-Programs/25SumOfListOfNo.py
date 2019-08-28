# A Program to print sum of list of numbers.

list  = eval(input('Enter a list of numbers : '))
s = 0
for x in list:
    s = s + x
print('The sum of list of Numbers : ', s)

# Output
# Enter a list of numbers : [12, 34, 45, 56]
# The sum of List of Numbers :  147


# Using Sequence Index for loop
list  = eval(input('Enter a list of numbers : '))
s = 0
i = 0
for x in list:
    s = s + list[i]
    i = i + 1
print('The sum of list of Numbers : ', s)

# Output
# Enter a list of numbers : [22, 23, 34, 45]
# The sum of list of Numbers :  124

# Using Sequence Index while loop
list  = eval(input('Enter a list of numbers : '))
i = 0
sum = 0
while i < len(list):
    sum = sum + list[i]
    i += 1
print('The sum of list of numbers : ', sum)

# Output
# Enter a list of numbers : [12, 12, 12, 23]
# The sum of list of numbers :  59