# A program to check whether a number is odd or even.

a = int(input('Enter a number : '))
if a % 2 == 0:
    print('{} is even number'.format(a))
else:
    print('{} is odd number'.format(a))

# Output
# Enter a number : 12
# 12 is even number

# Enter a number : 11
# 11 is odd number