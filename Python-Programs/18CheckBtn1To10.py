# A program to check whether a number is in between 1 to 10.

a = int(input('Enter a number : '))
if a >= 1 and a <= 10:
    print('{} is in between 1 to 10'.format(a))
else:
    print('{} is not in between 1 to 10'.format(a))

# Output
# Enter a number : 10
# 10 is not in between 1 to 10

# Enter a number : 10
# 10 is in between 1 to 10

# Enter a number : 11
# 11 is not in between 1 to 10

# Enter a number : 5
# 5 is in between 1 to 10