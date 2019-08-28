# Read Two numbers from the keyboard and print the Maximum value.

a = int(input('Entar First number : '))
b = int(input('Enter Second number : '))
max = a if a > b else b
print('Maximum of {} and {} is {}'.format(a, b, max))

# Output
# Entar First number : 300
# Enter Second number : 123
# Maximum of 300 and 123 is 300

# Entar First number : 100
# Enter Second number : 200
# Maximum of 100 and 200 is 200