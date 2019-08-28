# A program to accept 3 numbers from the kyb in the same line and disply sum of them.

a, b, c = [int(x) for x in input('Enter three numbers with space in between : ').split()]
print('The sum of {}, {}, {} is {}'.format(a, b, c, a+b+c))

# Output
# Enter three numbers with space in between : 12 23 34
# The sum of 12, 23, 34 is 69