# A program to find the number of occurrences of each letter in a given string.

word = input('Enter a string : ')
d = {}
for i in word:
    d[i] = d.get(i, 0) + 1
print(d)
for k,v in d.items():
    print('Key = {} Values = {} '.format(k, v))

# Enter a string : mississippi
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
# Key = m Values = 1 
# Key = i Values = 4 
# Key = s Values = 4 
# Key = p Values = 2 

# Unique Vowels Store into a dictionary
word = input('Enter a string : ')
d = {}
vowels = {'a', 'e', 'i', 'o', 'u'}
for i in word:
    if i in vowels:
        d[i] = d.get(i, 0) + 1
print(d)
for k,v in d.items():
    print('Key = {} Values = {} '.format(k, v))

# Enter a string : mississippi
# {'i': 4}
# Key = i Values = 4 