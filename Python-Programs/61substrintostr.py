# Inserting a sub string into a string

str = input('Enter a string: ')
sub = input('Enter a sub string: ')
n = int(input('Enter position no: '))
n=n-1

l1 = len(str)
l2 = len(sub)

str1 = []

for i in range(n):
    str1.append(str[i])
print(str1)

for i in range(l2):
    str1.append(sub[i])
print(str1)

for i in range(n, l1):
    str1.append(str[i])
print(str1)

str1 = ''.join(str1)
print(str1)

# Enter a string: it is summer
# Enter a sub string: hot
# Enter position no: 7
# ['i', 't', ' ', 'i', 's', ' ']
# ['i', 't', ' ', 'i', 's', ' ', 'h', 'o', 't']
# ['i', 't', ' ', 'i', 's', ' ', 'h', 'o', 't', 's', 'u', 'm', 'm', 'e', 'r']
# it is hotsummer