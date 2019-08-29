# A program to print characters at even position and odd position for the given string.

s = input('Enter a string: ')
print('Characters at even position : {} '.format(s[0::2]))
print('Characters at odd position : {} '.format(s[1::2]))

s = input('\nEnter a string: ')
i = 0
l = len(s)
print('Characters at even position :')
while i < l:
    print(s[i], end = ' ')
    i = i + 2

i = 1
l = len(s)
print('\nCharacters at odd position :')
while i < l:
    print(s[i], end = ' ')
    i = i + 2

# Enter a string: Ram is a good boy
# Characters at even position : Rmi  odby                  
# Characters at odd position : a sago o 

# Enter a string: Ram is a good boy
# Characters at even position :
# R m i     o d b y 
# Characters at odd position :
# a   s a g o   o 
