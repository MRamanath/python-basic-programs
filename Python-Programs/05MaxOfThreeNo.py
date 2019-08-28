# Read Three numbers from the keyboard and print the maximum value.

a = int(input('Entar First number : '))
b = int(input('Enter Second number : '))
c = int(input('Enter Third number : '))
max = a if a > b and a > c else b if b > c else c
print('Maximum of {}, {}, {} is {}'.format(a, b, c, max))

# Output
# Entar First number : 300
# Enter Second number : -11
# Enter Third number : 800
# Maximum of 300, -11, 800 is 800             
