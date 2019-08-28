# A program to check whether a number is positive, negative or zero.

a = int(input('Enter a number : '))
if a == 0:
    print('{} is Zero'.format(a))
elif a > 0:
    print('{} is Positive'.format(a))
else:
    print('{} is Negative'.format(a))

# Output
# Enter a number : 0
# 0 is Zero

# Enter a number : 12
# 12 is Positive

# Enter a number : -19
# -19 is Negative