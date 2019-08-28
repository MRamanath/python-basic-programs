# A program to display characters of a string.

a = input('Enter a string : ')
for i in a:
    print(i, end = '\t')

# Output
# Enter a string : Ramanath
# R       a       m       a       n       a       t       h

# Using Sequence Index for loop
a = input('Enter a string : ')
x = len(a)
i = 0
for n in range(x):
    print(a[i], end = '\t')
    i = i + 1

# Output
# Enter a string : Ramanath
# R       a       m       a       n       a       t       h

# Using Sequence Index while loop
a = input('Enter a string : ')
i = 0
while i < len(a):
    print(a[i], end = '\t')
    i = i + 1

# Output
# Enter a string : Ramanath
# R       a       m       a       n       a       t       h