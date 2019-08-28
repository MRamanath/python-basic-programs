# A program to check wheather two numbers are equal, or less than or greater than 
# to each other.

a = int(input('Enter First Number : '))
b = int(input('Enter Second Number : '))
print('Both Number are Equal' if a == b else 'First Number is greater than Second Number' if a > b else 'First Number is less than Second Number')

# Output
# Enter First Number : 300
# Enter Second Number : 400
# First Number is less than Second Number

# Enter Second Number : 100
# First Number is greater than Second Number

# Enter First Number : 200
# Enter Second Number : 200
# Both Number are Equal