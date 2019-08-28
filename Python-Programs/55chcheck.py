# A program to know the type of character present in the given string.

str = input('Enter a character : ')
ch = str[0]

if ch.isalnum():
    print('It is alphabetic or numeric character')
    if ch.isalpha():
        print('It is aplphabet')
        if ch.islower():
            print('It is lowercase')
        else:
            print('It is uppercase')
    else:
        print('It is numeric digit')
elif ch.isspace():
    print('It is a space')
else:
    print('It may be a special character')

# Enter a character : A
# It is alphabetic or numeric character
# It is aplphabet
# It is uppercase

# Enter a character : a
# It is alphabetic or numeric character
# It is aplphabet
# It is lowercase

# Enter a character : 32
# It is alphabetic or numeric character
# It is numeric digit