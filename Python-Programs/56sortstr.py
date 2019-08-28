# A program to sort a string.

str = []
n = int(input('How many strings ? '))

for i in range(n):
    print('Enter String: ', end = ' ')
    str.append(input())

str1 = sorted(str)
print(str1)
for x in str1:
    print(x)
print()

str.sort()
print(str)
for x in range(len(str)):
    print(str[x])
print()

str.sort(reverse = True)
print(str)
for x in str:
    print(x)

# How many strings ? 3
# Enter String:  zz
# Enter String:  aa
# Enter String:  mm
# ['aa', 'mm', 'zz']
# aa
# mm
# zz

# ['aa', 'mm', 'zz']
# aa
# mm
# zz

# ['zz', 'mm', 'aa']
# zz
# mm
# aa