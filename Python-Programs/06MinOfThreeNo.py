# Read Three numbers from the keyboard and print the minimum value.

a = int(input('Entar First number : '))
b = int(input('Enter Second number : '))
c = int(input('Enter Third number : '))
min = a if a < b and a < c else b if b < c else c
print('Minimum of {}, {}, {} is {}'.format(a, b, c, min))

# Output
# Entar First number : 200
# Enter Second number : 120
# Enter Third number : 90
# Minimum of 200, 120, 90 is 90