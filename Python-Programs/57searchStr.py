# A python program to search for the position of a string in a given group of strings.

s = []
a = int(input('How many strings ? '))
for x in range(a):
    print('Enter string : ', end = ' ')
    s.append(input())
print(s)

search = input('Enter the searching string : ')
for i in s:
    if search == i:
        print('{} is found at {}'.format(search, s.index(search)))
        break
else:
    print('{} is not found'.format(search))

# How many strings ? 5
# Enter string :  A
# Enter string :  B
# Enter string :  C
# Enter string :  D
# Enter string :  A
# ['A', 'B', 'C', 'D', 'A']
# Enter the searching string : A
# A is found at 0

s = input('Enter a string: ')

search = input('Enter the searching string : ')
for i in s:
    if search == i:
        print('{} is found at {}'.format(search, s.index(search)))
        break
else:
    print('{} is not found'.format(search))

# Enter a string: Ramanath
# Enter the searching string : h
# h is found at 7