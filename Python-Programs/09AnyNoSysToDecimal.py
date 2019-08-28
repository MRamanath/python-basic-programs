# A program to convert numbers from other systems to decimal system.

str = input('Enter a hexadecimal number : ')
print('Hexadecimal to decimal is {}'.format(int(str, 16)))

str = input('Enter a octal number : ')
print('Octal to decimal is {}'.format(int(str, 8)))

str = input('Enter a binary number : ')
print('Binary to decimal is {}'.format(int(str, 2)))

# Output
# Enter a hexadecimal number : abface123
# Hexadecimal to decimal is 46165451043
# Enter a octal number : 1237
# Octal to decimal is 671
# Enter a binary number : 1101101
# Binary to decimal is 109