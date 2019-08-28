# A program to find the length of a string without using len() function.

str = input('Enter a string: ')
i = 0
for x in str:
    print(str[i], end = ' ')
    i = i + 1
print('\nNo of Characters : ', i)

# Enter a string: ramanath
# r a m a n a t h
# No of Characters :  8

str = input('Enter a string: ')
i = 0
while i < len(str):
    print(str[i], end = ' ')
    i = i + 1
print('\nNo of Characters : ', i)

# Enter a string: ramanath
# r a m a n a t h
# No of Characters :  8