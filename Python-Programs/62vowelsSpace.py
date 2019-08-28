# A program to count the no. of vowels and spaces in a string.

string = input('Enter a string : ')
spaces = 0
vowels = 0
digit = 0

for i in string:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'O' or i == 'I' or i == 'U'):
        vowels = vowels + 1
    elif i == ' ':
        spaces = spaces + 1     

print('No of vowels {}'.format(vowels))
print('No of spaces {}'.format(spaces))

# Enter a string : ramanath mandal
# No of vowels 5
# No of spaces 1

